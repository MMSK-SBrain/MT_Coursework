// A maintained list of standards and bodies of knowledge the models may name.
// Supplied as context so models never have to recall standard names or numbers.
export interface StandardRef {
  id: string;
  title: string;
  sectors: string[];
}

export const STANDARDS: StandardRef[] = [
  { id: "ISO/IEC/IEEE 15288", title: "Systems and software engineering: system life cycle processes", sectors: ["systems", "automotive", "aerospace"] },
  { id: "INCOSE SE Handbook", title: "INCOSE Systems Engineering Handbook", sectors: ["systems"] },
  { id: "ISO 26262", title: "Road vehicles: functional safety", sectors: ["automotive"] },
  { id: "ISO 21448 (SOTIF)", title: "Road vehicles: safety of the intended functionality", sectors: ["automotive"] },
  { id: "ISO/SAE 21434", title: "Road vehicles: cybersecurity engineering", sectors: ["automotive"] },
  { id: "Automotive SPICE (ASPICE)", title: "Process assessment model for automotive software and systems", sectors: ["automotive"] },
  { id: "IATF 16949", title: "Automotive quality management systems", sectors: ["automotive", "manufacturing"] },
  { id: "AIAG-VDA FMEA Handbook", title: "Failure mode and effects analysis", sectors: ["automotive", "manufacturing"] },
  { id: "IEC 61508", title: "Functional safety of electrical/electronic/programmable safety-related systems", sectors: ["industrial", "systems"] },
  { id: "UN R100", title: "Battery electric vehicle safety requirements", sectors: ["automotive", "ev"] },
  { id: "AIS-156", title: "Indian requirements for EV traction battery safety", sectors: ["automotive", "ev"] },
  { id: "ISO 45001", title: "Occupational health and safety management", sectors: ["manufacturing", "workshop"] },
  { id: "ISO 9001", title: "Quality management systems", sectors: ["all"] },
];

export function standardsContext(): string {
  return STANDARDS.map((s) => `- ${s.id}: ${s.title}`).join("\n");
}
