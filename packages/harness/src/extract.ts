// Turns uploaded handouts and module sheets into plain text for parseInputs.
// Handles text formats, .docx (mammoth), .pdf (unpdf) and .xlsx (exceljs). Anything else is refused.
import type { InputFile } from "@cg/core";

const TEXT_EXT = /\.(txt|md|markdown|csv|tsv|json)$/i;
const ext = (f: InputFile) => f.meta.filename.toLowerCase().split(".").pop() ?? "";
const buf = (f: InputFile) => Buffer.from(f.bytes.buffer, f.bytes.byteOffset, f.bytes.byteLength);

/** Hard cap on extracted text, so a small compressed file can't expand into a huge prompt. */
export const MAX_EXTRACTED_CHARS = 400_000;

async function docx(f: InputFile): Promise<string> {
  const mammoth = await import("mammoth");
  return (await mammoth.extractRawText({ buffer: buf(f) })).value;
}

async function pdf(f: InputFile): Promise<string> {
  const { extractText, getDocumentProxy } = await import("unpdf");
  const doc = await getDocumentProxy(new Uint8Array(f.bytes));
  const { text } = await extractText(doc, { mergePages: true });
  return Array.isArray(text) ? text.join("\n") : text;
}

/** One block per sheet; each row as tab-separated cell text, so module tables keep their columns. */
async function xlsx(f: InputFile): Promise<string> {
  const { default: ExcelJS } = await import("exceljs");
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.load(buf(f) as never);
  const out: string[] = [];
  wb.eachSheet((ws) => {
    out.push(`## Sheet: ${ws.name}`);
    ws.eachRow((row) => {
      const cells = (row.values as unknown[]).slice(1).map((_, i) => row.getCell(i + 1).text.replace(/\s+/g, " ").trim());
      if (cells.some(Boolean)) out.push(cells.join("\t"));
    });
  });
  return out.join("\n");
}

export async function extractText(f: InputFile): Promise<string> {
  try {
    return await read(f);
  } catch (e) {
    const msg = (e as Error).message ?? String(e);
    throw new Error(msg.startsWith(f.meta.filename) ? msg : `${f.meta.filename}: could not read the file (${msg.slice(0, 120)})`);
  }
}

async function read(f: InputFile): Promise<string> {
  const e = ext(f);
  const m = f.meta.mime;
  let text: string;
  if (m.startsWith("text/") || m === "application/json" || TEXT_EXT.test(f.meta.filename)) text = new TextDecoder("utf-8").decode(f.bytes);
  else if (e === "docx" || m === "application/vnd.openxmlformats-officedocument.wordprocessingml.document") text = await docx(f);
  else if (e === "pdf" || m === "application/pdf") text = await pdf(f);
  else if (e === "xlsx" || m === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") text = await xlsx(f);
  else throw new Error(`${f.meta.filename}: unsupported file type. Upload .docx, .pdf, .xlsx, .txt, .md or .csv.`);
  text = text.trim();
  if (!text) throw new Error(`${f.meta.filename}: no text found (a scanned PDF needs OCR first).`);
  return text.length > MAX_EXTRACTED_CHARS ? text.slice(0, MAX_EXTRACTED_CHARS) : text;
}
