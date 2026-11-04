// JavaScript source that ends up inside the generated scenes.js, one library per video look.
// It is plain explainroo scene code (see /Volumes/Dev/explainroo/AGENTS.md, "Scene API").
// Each visual type in outline.ts has one renderer: R.hook(s, data, meta), R.objectives(...), ...
// meta = { course, n, total } (slide number info). Written without backticks so it can live in a TS template string.

export const BASE_LIB = String.raw`
const U = (s) => Math.max(s.W, s.H) / 100;
const PALETTE = ['blue', 'green', 'orange', 'purple', 'teal'];
function wrap(text, width) {
  const out = []; let line = '';
  for (const w of String(text).split(/\s+/)) {
    if (line && (line + ' ' + w).length > width) { out.push(line); line = w; } else line = line ? line + ' ' + w : w;
  }
  if (line) out.push(line);
  return out.join('\n');
}
const marks = (s, prefix, n) => Array.from({ length: n }, (_, i) => s.mark(prefix + (i + 1)));

const BASE = {
  hook(s, d) {
    const u = U(s);
    s.icon('help-circle', { x: s.cx, y: s.cy - u * 13, size: u * 13, color: 'accent', at: 0.2 });
    s.text(d.text, { x: s.cx, y: s.cy + u * 6, size: u * (s.portrait ? 5 : 5.5), bold: true, maxWidth: s.safe.w * 0.9, at: '#q' });
  },
  objectives(s, d) {
    const u = U(s);
    const t = s.text(d.title, { x: s.safe.left, y: s.safe.top + u * 2, align: 'left', valign: 'top', size: u * 5.2, bold: true, at: 0.2 });
    const m = marks(s, 'i', d.items.length);
    s.list(d.items.map((text, i) => ({ text, at: m[i] })), { x: s.safe.left, y: t.bottom + u * 4, width: s.safe.w, size: u * (s.portrait ? 3.2 : 3.1), bullet: 'check', bulletColor: 'green' });
  },
  flow(s, d) {
    const u = U(s); const n = d.steps.length;
    s.text(d.title, { x: s.cx, y: s.safe.top + u * 4, size: u * 5, bold: true, at: 0.2 });
    const xs = s.portrait ? d.steps.map(() => s.cx) : s.row(n, { width: s.safe.w * (n > 3 ? 0.62 : 0.7) });
    const ys = s.portrait ? s.col(n, { height: s.safe.h * 0.7 }) : d.steps.map((_, i) => s.cy + u * 4 + (n > 3 ? (i % 2 ? u * 9 : -u * 9) : 0));
    const m = marks(s, 's', n);
    d.steps.forEach((label, i) => {
      s.box(wrap(label, n > 3 && !s.portrait ? 15 : 18), { id: 'st' + i, x: xs[i], y: ys[i], size: u * (n > 3 ? 2.1 : 2.4), color: PALETTE[i % PALETTE.length], at: m[i] });
      if (i) s.arrow('st' + (i - 1), 'st' + i, { at: m[i] });
    });
  },
  point(s, d) {
    const u = U(s);
    s.icon('lightbulb', { x: s.cx, y: s.cy - u * 17, size: u * 11, color: 'yellow', at: 0.2 });
    const t = s.text(d.title, { id: 'pt', x: s.cx, y: s.cy - u * 3, size: u * 5.4, bold: true, maxWidth: s.safe.w * 0.9, at: '#t' });
    s.annotate('pt', { type: 'underline', color: 'accent', at: '#c' });
    s.text(d.caption, { x: s.cx, y: t.bottom + u * 5, valign: 'top', size: u * 3, color: 'muted', maxWidth: s.safe.w * 0.82, at: '#c' });
  },
  example(s, d) {
    const u = U(s);
    s.icon('factory', { x: s.cx, y: s.cy - u * 17, size: u * 10, bg: 'circle', color: 'accent', at: '#e' });
    s.text(d.label, { x: s.cx, y: s.cy - u * 7, size: u * 3, color: 'accent', bold: true, at: '#e' });
    s.text(d.text, { x: s.cx, y: s.cy + u * 8, size: u * 3.3, maxWidth: s.safe.w * 0.8, bg: true, border: 'muted', padding: u * 2.2, at: s.mark('e') + 0.6 });
  },
  question(s, d) {
    const u = U(s);
    s.icon('timer', { x: s.cx, y: s.cy - u * 15, size: u * 11, color: 'orange', at: '#q' });
    s.text('Pause and think', { x: s.cx, y: s.cy - u * 5, size: u * 3, color: 'muted', at: '#q' });
    s.text(d.text, { x: s.cx, y: s.cy + u * 8, size: u * 4.6, bold: true, maxWidth: s.safe.w * 0.88, at: s.mark('q') + 0.8 });
  },
  recap(s, d, m) { BASE.objectives(s, { title: d.title, items: d.items }, m); },
  media(s, d) {
    const u = U(s);
    const w = Math.min(s.safe.w * 0.78, u * 72);
    const at = '#m';
    let box;
    if (d.src) {
      const o = { x: s.cx, y: s.cy - u * 4, w, frame: d.frame || 'window', at };
      if (o.frame === 'browser') o.url = d.url || '';
      box = /\.(mp4|mov|webm|m4v)$/i.test(d.src) ? s.clip(d.src, o) : s.image(d.src, o);
    } else {
      const what = d.frame === 'browser' ? 'screen recording' : 'clip';
      box = s.box('Your ' + what + ' goes here\n' + wrap(d.title, 28), { x: s.cx, y: s.cy - u * 4, w, h: w * 0.56, icon: d.frame === 'browser' ? 'monitor' : 'video', dashed: true, color: 'muted', size: u * 2.8, at });
    }
    s.text(d.caption, { x: s.cx, y: box.bottom + u * 4, valign: 'top', size: u * 3, color: 'muted', maxWidth: s.safe.w * 0.85, at: '#c' });
  },
};
`;

/** Whiteboard: same renderers, but drawn stroke by stroke (rough.js strokes, "draw" and "write" entrances) with stick figures. */
export const WHITEBOARD_LIB = String.raw`
// A stick figure drawn as five strokes, one after another from time "at" (seconds). Returns the time it finishes.
function person(s, x, y, k, at, color) {
  const t0 = s.time(at); const o = { color: color || 'ink', width: 6, sfx: false };
  const head = s.circle({ x, y: y - 100 * k, r: 26 * k, color: color || 'ink', at: t0 });
  s.line([[x, y - 72 * k], [x, y + 30 * k]], { ...o, at: t0 + 0.35 });
  s.line([[x - 48 * k, y - 36 * k], [x, y - 52 * k], [x + 48 * k, y - 36 * k]], { ...o, at: t0 + 0.65 });
  s.line([[x - 40 * k, y + 100 * k], [x, y + 30 * k], [x + 40 * k, y + 100 * k]], { ...o, at: t0 + 0.95 });
  return t0 + 1.3;
}
const WB = {
  hook(s, d) {
    const u = U(s);
    const k = u / 8.5;
    person(s, s.cx - u * (s.portrait ? 0 : 22), s.cy - u * 3, k, 0.2, 'blue');
    s.text('?', { x: s.cx + u * (s.portrait ? 0 : 6), y: s.cy - u * 14, size: u * 24, color: 'accent', font: 'hand', enter: 'write', dur: 1.2, at: 1.0 });
    s.text(d.text, { x: s.cx, y: s.cy + u * 14, size: u * (s.portrait ? 4.6 : 5), font: 'hand', maxWidth: s.safe.w * 0.9, enter: 'write', at: '#q' });
  },
  point(s, d) {
    const u = U(s);
    const t = s.text(d.title, { id: 'pt', x: s.cx, y: s.cy - u * 10, size: u * 5.4, font: 'hand', maxWidth: s.safe.w * 0.9, enter: 'write', at: '#t' });
    s.annotate('pt', { type: 'underline', color: 'red', at: '#c', dur: 0.8 });
    s.text(d.caption, { x: s.cx, y: t.bottom + u * 5, valign: 'top', size: u * 3.2, font: 'hand', color: 'blue', maxWidth: s.safe.w * 0.82, enter: 'write', at: '#c' });
    // light bulb doodle in the corner
    const bx = s.safe.right - u * 8, by = s.safe.top + u * 9;
    s.circle({ x: bx, y: by, r: u * 3.2, color: 'yellow', at: 0.3 });
    s.line([[bx - u * 1.6, by + u * 4.4], [bx + u * 1.6, by + u * 4.4]], { color: 'ink', at: 0.8 });
    [[-1, -1], [0, -1.4], [1, -1]].forEach(([dx, dy], i) => s.line([[bx + dx * u * 4.6, by + dy * u * 4.6], [bx + dx * u * 6, by + dy * u * 6]], { color: 'yellow', at: 1 + i * 0.15 }));
  },
  example(s, d) {
    const u = U(s);
    const k = u / 8;
    const px = s.portrait ? s.cx : s.safe.left + u * 14;
    person(s, px, s.cy + (s.portrait ? u * 20 : u * 4), k, 0.2, 'green');
    s.text(d.label, { x: s.cx, y: s.safe.top + u * 5, size: u * 4, font: 'hand', color: 'accent', enter: 'write', at: '#e' });
    s.box(d.text.slice(0, 120), { shape: 'ellipse', w: s.safe.w * (s.portrait ? 0.9 : 0.5), h: u * (s.portrait ? 26 : 24), x: s.portrait ? s.cx : s.cx + u * 14, y: s.portrait ? s.cy - u * 8 : s.cy, size: u * 2.5, font: 'hand', color: 'blue', at: s.mark('e') + 0.5 });
  },
  question(s, d) {
    const u = U(s);
    s.text('?', { x: s.cx, y: s.cy - u * 12, size: u * 20, color: 'accent', font: 'hand', enter: 'write', dur: 1.2, at: '#q' });
    s.text(d.text, { x: s.cx, y: s.cy + u * 12, size: u * 4.6, font: 'hand', maxWidth: s.safe.w * 0.88, enter: 'write', at: s.mark('q') + 0.8 });
  },
};
`;

/** Slides: a plain slide frame (title, rule, footer, slide number) with the content as lists. */
export const SLIDES_LIB = String.raw`
function chrome(s, m, title, at) {
  const u = U(s);
  s.line([[s.safe.left, s.safe.top + u * 9.5], [s.safe.right, s.safe.top + u * 9.5]], { color: 'accent', width: 6, at: -1, enter: 'none', sfx: false });
  s.text(m.course, { x: s.safe.left, y: s.safe.bottom, align: 'left', valign: 'bottom', size: u * 1.7, color: 'muted', at: -1, enter: 'none', sfx: false });
  s.text(m.n + ' / ' + m.total, { x: s.safe.right, y: s.safe.bottom, align: 'right', valign: 'bottom', size: u * 1.7, color: 'muted', at: -1, enter: 'none', sfx: false });
  return s.text(title, { x: s.safe.left, y: s.safe.top, align: 'left', valign: 'top', size: u * 5.2, bold: true, maxWidth: s.safe.w, at: at === undefined ? 0.2 : at });
}
function bullets(s, items, ats, top) {
  const u = U(s);
  s.list(items.map((text, i) => ({ text, at: ats[i] })), { x: s.safe.left, y: top, width: s.safe.w, size: u * (s.portrait ? 3.3 : 3.4), gap: u * 1.6, bullet: 'dot' });
}
const SL = {
  hook(s, d, m) {
    const u = U(s);
    s.text(d.text, { x: s.safe.left, y: s.cy - u * 4, align: 'left', size: u * 7, bold: true, maxWidth: s.safe.w * 0.9, at: '#q' });
    s.line([[s.safe.left, s.cy + u * 8], [s.safe.left + u * 20, s.cy + u * 8]], { color: 'accent', width: 8, at: s.mark('q') + 0.4 });
    s.text(m.course, { x: s.safe.left, y: s.cy + u * 12, align: 'left', valign: 'top', size: u * 2.6, color: 'muted', at: s.mark('q') + 0.6 });
  },
  objectives(s, d, m) {
    const t = chrome(s, m, d.title);
    bullets(s, d.items, marks(s, 'i', d.items.length), s.safe.top + U(s) * 14);
  },
  flow(s, d, m) {
    chrome(s, m, d.title);
    const u = U(s);
    s.list(d.steps.map((text, i) => ({ text, at: s.mark('s' + (i + 1)) })), { x: s.safe.left, y: s.safe.top + u * 14, width: s.safe.w, size: u * 3.6, gap: u * 2, bullet: 'number' });
  },
  point(s, d, m) {
    chrome(s, m, d.title, '#t');
    bullets(s, [d.caption], ['#c'], s.safe.top + U(s) * 14);
  },
  example(s, d, m) {
    const u = U(s);
    chrome(s, m, d.label, '#e');
    s.text(d.text, { x: s.safe.left, y: s.safe.top + u * 15, align: 'left', valign: 'top', size: u * 3.6, maxWidth: s.safe.w * 0.92, at: s.mark('e') + 0.6 });
  },
  question(s, d, m) {
    const u = U(s);
    chrome(s, m, 'Quick check', '#q');
    s.text(d.text, { x: s.safe.left, y: s.safe.top + u * 16, align: 'left', valign: 'top', size: u * 4.6, bold: true, maxWidth: s.safe.w * 0.92, at: s.mark('q') + 0.8 });
  },
  recap(s, d, m) {
    chrome(s, m, d.title);
    bullets(s, d.items, marks(s, 'i', d.items.length), s.safe.top + U(s) * 14);
  },
};
`;
