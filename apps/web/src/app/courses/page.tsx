import { FREE_TIER } from "@cg/core";
import { desc, eq } from "drizzle-orm";
import Link from "next/link";
import { TopBar } from "@/components/top-bar";
import { db, schema } from "@/lib/db";
import { monthUsage } from "@/lib/repo";
import { requireTeacherPage } from "@/lib/session";
import { usingMockStages } from "@/lib/stages";
import { NewCourse } from "./new-course";

export const dynamic = "force-dynamic";

export default async function Courses() {
  const u = await requireTeacherPage();
  const rows = await db()
    .select({ id: schema.courses.id, title: schema.courses.title, updatedAt: schema.courses.updatedAt })
    .from(schema.courses)
    .where(eq(schema.courses.ownerId, u.id))
    .orderBy(desc(schema.courses.updatedAt));
  const usage = await monthUsage(u.id);
  const freeLeft = Math.max(0, FREE_TIER.coursesPerMonth - usage.coursesStarted);
  return (
    <>
      <TopBar email={u.email} isAdmin={u.isAdmin} mock={usingMockStages()}
        usage={<span className="usage">{usage.coursesStarted}/{FREE_TIER.coursesPerMonth} course · {usage.videoSeconds}/{FREE_TIER.videoSecondsPerMonth} s video</span>} />
      <div className="shell page">
        <main>
          <div className="wrap">
            <div className="head">
              <div>
                <span className="eyebrow">{u.profile.institution} · {u.profile.subject}</span>
                <h1>Your courses</h1>
                <p>{freeLeft ? `You can start ${freeLeft} more free course this month.` : "You have used this month's free course. Extra courses are paid per course."}</p>
              </div>
              <NewCourse />
            </div>
            <div className="panel list">
              {rows.length ? rows.map((c) => (
                <Link key={c.id} className="item" href={`/courses/${c.id}`}>
                  <b>{c.title}</b><span className="muted small">Updated {c.updatedAt.toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" })}</span>
                </Link>
              )) : <p className="muted" style={{ margin: 0 }}>No courses yet. Start one from a course handout or a module sheet.</p>}
            </div>
          </div>
        </main>
      </div>
    </>
  );
}
