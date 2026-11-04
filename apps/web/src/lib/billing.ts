// Quota reservations that must be atomic: the check and the increment happen in one conditional UPDATE,
// inside the same transaction as the work they pay for.
import type { Course } from "@cg/core";
import { newCourse } from "./course-logic";
import { db } from "./db";
import { HttpError } from "./errors";
import { FEATURE_LABEL } from "./quota";
import { consumeCredit, countPaidCourse, insertCourse, reserveFreeCourse, reserveFreeVideo, type Exec } from "./repo";

const paywall = (feature: "extraCourse" | "extraVideo", reason: string) =>
  new HttpError(402, reason, { paywall: { feature, reason } });

/** Take a free course slot (or an extraCourse credit) and insert the course, all or nothing. */
export async function startCourse(userId: string, id: string, title: string): Promise<Course> {
  return db().transaction(async (tx) => {
    if (!(await reserveFreeCourse(tx, userId))) {
      if (!(await consumeCredit(userId, "extraCourse", tx))) {
        throw paywall("extraCourse", "The free tier includes 1 course a month, and you have used it.");
      }
      await countPaidCourse(tx, userId);
    }
    return insertCourse(userId, newCourse(id, userId, title), tx);
  });
}

/**
 * Reserve video time: free seconds while they fit in the monthly allowance, otherwise one extraVideo credit.
 * `then` runs in the same transaction (e.g. inserting the render job), so a failure releases the reservation.
 */
export async function reserveVideo<T>(userId: string, seconds: number, then: (tx: Exec) => Promise<T>): Promise<T> {
  return db().transaction(async (tx) => {
    if (!(await reserveFreeVideo(tx, userId, seconds)) && !(await consumeCredit(userId, "extraVideo", tx))) {
      throw paywall("extraVideo", `${FEATURE_LABEL.extraVideo}: this ${seconds} s video does not fit in your free allowance this month.`);
    }
    return then(tx);
  });
}
