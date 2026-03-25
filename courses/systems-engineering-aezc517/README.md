# Automotive Systems Engineering Course (AE ZG517 / AEL ZG517)

Complete coursework for the Systems Engineering course at BITS Pilani.

## Course Information

- **Course Title:** Automotive Systems Engineering
- **Course Code:** AE ZG517 / AEL ZG517
- **Credits:** 3 (32-0-0 model)
- **Instructor:** Sajeeth Kumar
- **Version:** 6.2 (12-Jan-2025)

## Directory Structure

```
systems-engineering-aezc517/
├── course-data.yaml                 # Complete course metadata
├── course-handout.txt               # Original course handout
├── lecture-frameworks/              # 16 instructor-led story frameworks
│   ├── SESSION-01-IntroductionToSystemsEngineering-Framework.md
│   ├── SESSION-02-SystemsEngineeringFundamentals-Framework.md
│   ├── ... (14 more sessions)
│   └── SESSION-16-EmergingTrends-Framework.md
├── presentations/
│   └── pptx/                        # 16 PowerPoint presentations (596 slides)
│       ├── SESSION-01-IntroductionToSystemsEngineering.pptx
│       ├── ... (15 more sessions)
│       └── SESSION-16-EmergingTrends.pptx
├── archive/                         # Historical files
└── README.md                        # This file
```

## Course Modules

### Module 1: Foundations of Systems Engineering (Sessions 1-4)
1. **Introduction to Systems Engineering** (36 slides)
   - Engineering failures case studies
   - Importance of systems engineering
   - Real-world examples: Apollo 13, Therac-25, Toyota recalls

2. **Systems Engineering Fundamentals** (38 slides)
   - INCOSE definition and systems thinking
   - ISO/IEC 15288 life cycle processes
   - V-Model and variations

3. **Traditional vs Model-Based Systems Engineering** (38 slides)
   - Document-centric vs MBSE
   - SysML, Simulink, MATLAB tools
   - Digital twin concepts

4. **Requirements Engineering** (44 slides)
   - Stakeholder analysis and needs vs requirements
   - Requirements types and attributes
   - Traceability and management

### Module 2: System Design and Analysis (Sessions 5-8)
5. **System Design and Architecture** (75 slides)
   - CONOPS and system context
   - Architecture development and patterns
   - Trade studies and design freeze

6. **Case Study 1: Boeing 737 MAX MCAS** (34 slides)
   - Real-world SE failure analysis
   - Requirements and design breakdown
   - Lessons learned

7. **Operational and Functional Analysis** (40 slides)
   - Operational scenarios and use cases
   - Functional decomposition
   - Requirements allocation

8. **Integration, Verification & Validation** (31 slides)
   - Integration strategies
   - Verification methods and testing levels
   - V&V planning and traceability

**Mid-Semester Exam Covers:** Sessions 1-8

### Module 3: Technical and Project Management (Sessions 9-12)
9. **Project and Risk Management** (33 slides)
   - Project estimation and WBS
   - Agile systems development
   - Risk identification and DFMEA

10. **Decision and Quality Management** (40 slides)
    - Multi-criteria decision analysis
    - Quality assurance vs control
    - Critical parameter management

11. **Agreement and Infrastructure Management** (39 slides)
    - Supplier engagement and contracts
    - Make vs buy decisions
    - Life cycle management

12. **Specialty Engineering: Safety & Security** (39 slides)
    - Safety analysis and HARA
    - ISO 26262 functional safety
    - Automotive cybersecurity

### Module 4: Life Cycle and Emerging Trends (Sessions 13-16)
13. **Life Cycle Cost & Total Cost of Ownership** (17 slides)
    - LCC analysis methods
    - TCO and affordability analysis
    - Cost-benefit and ROI

14. **Case Study 2: Advanced SE Analysis** (22 slides)
    - Safety, security, and specialty engineering
    - Complex automotive system analysis
    - Critical evaluation

15. **Technical Management & Enabling Processes** (31 slides)
    - Configuration management
    - Information and measurement
    - Enabling processes

16. **Emerging Trends in Systems Engineering** (39 slides)
    - Digital engineering and AI/ML in SE
    - DevOps and agile SE future
    - Autonomous systems challenges

## Presentation Features

All 16 PowerPoint presentations include:

- **Format:** 16:9 widescreen (1920x1080)
- **Total Slides:** 596 slides across all sessions
- **Style:** Professional engineering theme
  - Primary Blue: #4472C4
  - Dark Blue: #2E5090
  - Text Gray: #333333
- **Content:** Fully editable native PowerPoint text boxes
- **Structure:** Title slides, content slides, bullet points, code blocks

### Presentation Sizes
- **Smallest:** Session 13 (59 KB, 17 slides)
- **Largest:** Session 5 (136 KB, 75 slides)
- **Average:** ~90 KB, 37 slides per session

## Learning Outcomes

Students completing this course will be able to:

1. **LO1:** Describe processes, methods, and practices of systems engineering
2. **LO2:** Develop requirements, architectures, specifications, verifications, and tests
3. **LO3:** Recognize important SE and systems thinking strategies
4. **LO4:** Apply SE practices and methods in automotive systems
5. **LO5:** Analyze automotive systems using SE approaches to increase performance

## Key Topics Covered

### Foundational Concepts
- Systems thinking and emergence
- Life cycle processes (ISO/IEC 15288)
- V-Model and systems engineering frameworks
- MBSE and digital engineering

### Technical Processes
- Requirements engineering and traceability
- System architecture and design
- Functional and operational analysis
- Integration, verification, and validation

### Management Processes
- Project planning and risk management
- Decision analysis and quality management
- Supplier management and infrastructure
- Safety and security engineering

### Life Cycle Considerations
- Cost analysis (LCC, TCO)
- Configuration and information management
- Emerging trends (AI, DevOps, autonomous systems)

## Automotive Applications

Throughout the course, concepts are illustrated with automotive examples:
- **ADAS Systems:** Lane Keep Assist, Adaptive Cruise Control, AEB
- **Powertrain:** Battery Management Systems, ETCS
- **Safety:** ISO 26262, HARA, functional safety
- **Architecture:** Electrical/electronic architecture, AUTOSAR
- **Verification:** HIL testing, SIL testing, road testing

## Standards and References

### Primary Textbook
- **T1:** Systems Engineering Handbook, INCOSE, 4th Edition, 2015

### Key References
- **R1:** Systems Engineering and Analysis, Blanchard & Fabrycky, 5th Edition, 2013
- **R2:** Automotive Systems Engineering, Maurer & Winner (eds.), 2013

### Industry Standards
- ISO/IEC/IEEE 15288:2023 (Systems life cycle processes)
- ISO 26262:2018 (Automotive functional safety)
- Automotive SPICE v3.1 (Process assessment)
- SAE J3016 (Levels of driving automation)

## Evaluation Scheme

- **Quiz/Assignment:** 20% (Online)
- **Mid-Semester Test:** 30% (Closed book, Sessions 1-8)
- **Case Studies:** 20% (Project work)
- **Comprehensive Exam:** 30% (Open book, All sessions)

## How to Regenerate Presentations

If you need to update presentations after modifying frameworks:

```bash
cd /Volumes/Dev/Course_Generator/courses/systems-engineering-aezc517

# Preprocess frameworks
for file in lecture-frameworks/SESSION-*.md; do
    python3 ../../tools/presentation-tools/preprocess-framework.py \
        "$file" presentations/preprocessed/
done

# Convert to PowerPoint
for file in presentations/preprocessed/SESSION-*.md; do
    python3 ../../tools/presentation-tools/markdown-to-pptx.py \
        "$file" presentations/pptx/
done

# Clean up intermediate files
rm -rf presentations/preprocessed/
```

## Tools Used

- **Preprocessing:** Python script to convert frameworks to slide markdown
- **Conversion:** python-pptx library for PowerPoint generation
- **Format:** Marp-compatible markdown with custom processing

## Course Delivery

- **Contact Sessions:** 16 online lectures (90 minutes each)
- **Self-Study:** Additional 30 minutes per session
- **Case Studies:** 2 major case studies (Boeing 737 MAX, Advanced SE analysis)
- **Practical Exercises:** Hands-on SE practice with automotive systems

## Notes

- All frameworks follow instructor-led story arc format (Setup → Trigger → Rising Action → Climax → Resolution)
- Each session includes detailed instructor narration, visual descriptions, and PPT content
- Frameworks are designed for 28-30 slides target, actual presentations range 17-75 slides
- All content is tailored for M.Tech. Automotive Engineering students

## Version History

- **v6.2 (12-Jan-2025):** Complete course framework and presentations generated
- Based on official BITS Pilani course handout AEZG517/AELZG517

## Contact

For course-related queries, refer to the eLearn portal at https://elearn.bits-pilani.ac.in

---

**Generated:** 4 January 2026
**Status:** Course Complete - 16 Frameworks + 16 Presentations (596 slides total)
