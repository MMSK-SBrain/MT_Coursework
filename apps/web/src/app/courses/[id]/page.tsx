import { CourseApp } from "@/components/course-app";
import { STAGES, type StageId } from "@/lib/catalog";
import { HttpError } from "@/lib/errors";
import { loadCourse, monthUsage } from "@/lib/repo";
import { requireTeacherPage } from "@/lib/session";
import { usingMockStages } from "@/lib/stages";
import { notFound } from "next/navigation";

export const dynamic = "force-dynamic";

function firstOpenStage(c: Awaited<ReturnType<typeof loadCourse>>["course"]): StageId {
  if (!c.modules.length) return "inputs";
  if (!c.roles.some((r) => r.selected)) return "roles";
  if (!c.structureConfirmedAt) return "fit";
  if (!c.outcomesFrozenAt) return "outcomes";
  if (!c.plans.length) return "plans";
  return "build";
}

export default async function CoursePage({ params, searchParams }: { params: Promise<{ id: string }>; searchParams: Promise<{ stage?: string }> }) {
  const u = await requireTeacherPage();
  const { id } = await params;
  const { stage } = await searchParams;
  const data = await loadCourse(u.id, id).catch((e) => {
    if (e instanceof HttpError && e.status === 404) notFound();
    throw e;
  });
  const s = STAGES.some((x) => x.id === stage) ? (stage as StageId) : firstOpenStage(data.course);
  return <CourseApp initial={data} usage={await monthUsage(u.id)} stage={s} email={u.email} isAdmin={u.isAdmin} mock={usingMockStages()} />;
}
