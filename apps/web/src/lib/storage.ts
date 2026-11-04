// File storage for uploads and generated files. Local disk for now; swap for object storage (S3/R2) behind the same two functions.
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join, normalize } from "node:path";

const root = () => process.env.STORAGE_DIR ?? ".data";

function pathFor(key: string): string {
  const p = normalize(key);
  if (p.startsWith("..") || p.startsWith("/")) throw new Error("Bad storage key");
  return join(root(), p);
}

export async function putFile(key: string, bytes: Uint8Array): Promise<void> {
  const p = pathFor(key);
  await mkdir(dirname(p), { recursive: true });
  await writeFile(p, bytes);
}

export async function getFile(key: string): Promise<Uint8Array> {
  return new Uint8Array(await readFile(pathFor(key)));
}
