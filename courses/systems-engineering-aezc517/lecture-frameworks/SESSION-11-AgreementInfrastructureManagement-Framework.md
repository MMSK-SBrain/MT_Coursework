# Session 11: Agreement and Infrastructure Management
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Business/Organizational
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Understand the strategic importance of supplier engagement and contract management in automotive systems
- Apply vendor selection criteria and evaluation frameworks systematically
- Conduct make vs buy decision analysis using structured methods
- Define infrastructure requirements for system lifecycle support
- Develop lifecycle management plans including maintenance, support, and technology refresh strategies
- Recognize the organizational and business aspects of systems engineering

**Mapped Learning Outcomes:** LO3 (Recognize important systems engineering and systems thinking strategies and practices), LO4 (Apply systems engineering practices and methods in automotive systems)

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Hidden Half of Systems Engineering** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Professional title slide with network diagram showing OEM-supplier ecosystem
**Instructor Script:**
> "Welcome to Session 11. Today we explore what I call the 'hidden half' of systems engineering: Agreement and Infrastructure Management.
>
> So far, we've focused on the technical core - requirements, design, verification. But here's reality: **No automotive OEM builds 100% of their vehicle in-house.**
>
> Today, we learn how to engineer the business and organizational relationships that make complex systems possible."

#### Slide 2: Connection to Previous Sessions
**Visual:** Progression diagram showing Sessions 9→10→11→12
**Instructor Script:**
> "Let's connect this to our journey:
>
> **Session 9 (Project and Risk Management)**: We learned to plan and manage projects. But those projects involve SUPPLIERS and INFRASTRUCTURE.
>
> **Session 10 (Decision and Quality Management)**: We learned decision-making frameworks. Today's biggest decision? MAKE vs BUY.
>
> **Today (Session 11)**: How do we manage the supplier agreements and infrastructure that enable our systems?
>
> **Session 12 (Safety & Security)**: Safety and security requirements flow down to suppliers through agreements we'll discuss today.
>
> **The integration**: Technical excellence means nothing if you can't execute through suppliers, contracts, and infrastructure."

#### Slide 3: Why This Matters - The Modern Automotive Reality
**Visual:** Statistics showing supplier involvement in modern vehicles
**Instructor Script:**
> "Let me give you the numbers that define modern automotive engineering:
>
> **Industry Statistics:**
> - Average vehicle has **30,000+ parts**
> - Typical OEM manufactures only **20-30% in-house**
> - Modern vehicle involves **250-400 Tier 1 suppliers**
> - Tier 2 and Tier 3 suppliers: **2,000-3,000 companies**
> - OEM R&D spending: 30% in-house, **70% through suppliers**
>
> **Examples:**
> - **Tesla Model 3**:
>   - Battery: Panasonic/LG/CATL (suppliers)
>   - Infotainment: AMD chips (supplier)
>   - Cameras/sensors: Multiple suppliers
>   - Motors: Tesla in-house (strategic make decision)
>
> - **Toyota Prius**:
>   - Hybrid system: Toyota + Denso collaboration
>   - Electronics: Denso, Bosch (suppliers)
>   - Manufacturing equipment: Fanuc, KUKA (infrastructure)
>
> **The reality**: You're not just engineering a system. You're engineering a SUPPLY CHAIN and INFRASTRUCTURE ECOSYSTEM.
>
> Today I'll show you how professionals manage this complexity."

#### Slide 4: Real-World Example - The Semiconductor Crisis (2021-2023)
**Visual:** Timeline showing automotive production impacts
**Instructor Script:**
> "Remember the 2021-2023 chip shortage? Perfect case study for today's topics.
>
> **What happened:**
> - COVID-19 disrupted semiconductor production
> - Automotive industry couldn't get chips
> - Global vehicle production down 10 million units
> - $210 billion in lost revenue
>
> **Agreement Management Failures:**
> - OEMs had **just-in-time** contracts with chip suppliers
> - No guaranteed allocation clauses
> - Consumer electronics outbid automotive (higher margins)
> - Automotive lost priority
>
> **Infrastructure Management Failures:**
> - No redundancy in supplier base (single source dependencies)
> - No buffer inventory (lean manufacturing gone too far)
> - No alternative sourcing strategy
>
> **Who survived better?**
> - **Toyota**: Had 2-4 month chip inventory (infrastructure planning)
> - **Tesla**: Direct relationships with chip makers, flexible architecture (supplier engagement)
> - **Others**: Production halted for months
>
> **Lessons:**
> - Agreements aren't just legal documents - they're strategic risk management
> - Infrastructure isn't overhead - it's resilience
> - Make vs buy decisions have long-term consequences
>
> This is what we're learning today: How to avoid being the next cautionary tale."

#### Slide 5: Learning Journey for Today
**Visual:** Roadmap with 6 key areas
**Instructor Script:**
> "Today's journey covers six critical areas:
>
> **Part 1**: Supplier Engagement - Building strategic partnerships
> **Part 2**: Contract Management - Structuring agreements that protect and enable
> **Part 3**: Vendor Selection - Systematic evaluation and decision-making
> **Part 4**: Make vs Buy Decisions - Strategic analysis framework
> **Part 5**: Infrastructure Requirements - Planning for lifecycle support
> **Part 6**: Lifecycle Management - Maintenance, support, technology refresh
>
> By the end, you'll understand how to manage the organizational ecosystem that enables complex automotive systems."

---

### **TRIGGER: The Supplier Dilemma** (Slides 6-7, ~5 minutes)

#### Slide 6: A Real Engineering Decision
**Visual:** Split-screen showing in-house vs supplier options
**Instructor Script:**
> "Let me put you in a real scenario. You're the systems engineer for a new electric vehicle program.
>
> **Your manager asks**: 'Should we develop the battery management system (BMS) in-house or buy it from a supplier?'
>
> **Sounds simple, right? Let's see what happens with different approaches:**
>
> **Scenario 1 - Quick decision (no analysis):**
> 'Let's build it in-house. We want control.'
> **Result**: 3 years later, you're 18 months behind schedule, $50M over budget, and the BMS still doesn't meet safety certification. Your competitor bought from an established supplier and launched 2 years earlier.
>
> **Scenario 2 - Opposite quick decision:**
> 'Let's buy from the cheapest supplier.'
> **Result**: Supplier delivers on time, but BMS doesn't integrate well with your vehicle architecture. Requires expensive re-work. Supplier owns the IP - you can't modify or improve it. You're locked in.
>
> **Scenario 3 - Rushing supplier selection:**
> 'This supplier has good brochures and low prices.'
> **Result**: After production starts, supplier can't meet volume requirements. Quality issues emerge. They go bankrupt, leaving you with no source for critical components.
>
> **The reality**: These aren't hypothetical - these scenarios happen constantly in automotive.
>
> Today I'll show you the systematic approach that prevents these failures."

#### Slide 7: What We're Really Managing
**Visual:** System diagram showing multiple layers of agreements and infrastructure
**Instructor Script:**
> "Here's what agreement and infrastructure management actually involves for a typical automotive system:
>
> **Agreement Layers:**
> - **Development Contracts**: Who designs what? Who owns IP?
> - **Supply Agreements**: Volume commitments, pricing, delivery schedules
> - **Quality Agreements**: Defect rates, warranty terms, liability
> - **Service Agreements**: Support during production, end-of-life
> - **Technology Transfer**: If supplier transitions to second source
> - **Confidentiality/NDA**: Protecting proprietary information
>
> **Infrastructure Requirements:**
> - **Manufacturing**: Equipment, tooling, facilities
> - **Testing**: Environmental chambers, HIL systems, validation equipment
> - **IT Systems**: PLM, requirements management, testing databases
> - **Service Support**: Diagnostic tools, training programs, spare parts networks
> - **Technology Refresh**: Obsolescence management, upgrade paths
>
> **Stakeholders to Manage:**
> - **Direct suppliers** (Tier 1)
> - **Suppliers' suppliers** (Tier 2, Tier 3)
> - **Manufacturing partners** (contract manufacturers)
> - **Infrastructure providers** (equipment vendors, IT providers)
> - **Service networks** (dealers, service centers)
> - **Regulatory bodies** (for supplier qualification)
>
> **This is why we need systematic approaches.**
>
> Today, I'll give you frameworks that handle this complexity professionally."

---

### **RISING ACTION: Building the Management Framework** (Slides 8-24, ~52 minutes)

#### **Part 1: Supplier Engagement Strategy** (Slides 8-11, ~10 minutes)

##### Slide 8: Strategic Supplier Relationships
**Visual:** Supplier relationship pyramid showing different tiers
**Instructor Script:**
> "First principle: **Not all suppliers are equal. Different relationships require different engagement strategies.**
>
> **Supplier Relationship Tiers:**
>
> **Tier 1 - Strategic Partners** (5-10% of suppliers, 60-70% of value)
> - Long-term relationships (10+ years)
> - Co-development partnerships
> - Shared technology roadmaps
> - Example: Bosch (powertrain), Denso (hybrid systems), Continental (ADAS)
> - **Engagement**: Joint engineering teams, executive sponsorship, technology sharing
>
> **Tier 2 - Preferred Suppliers** (20-30% of suppliers, 25-35% of value)
> - Multi-year contracts
> - Proven performance
> - Moderate technical complexity
> - Example: Seat manufacturers, lighting systems, HVAC
> - **Engagement**: Regular business reviews, performance metrics, quality partnerships
>
> **Tier 3 - Transactional Suppliers** (60-70% of suppliers, 5-10% of value)
> - Commodity components
> - Short-term contracts
> - Price-driven selection
> - Example: Fasteners, basic wiring, standard connectors
> - **Engagement**: Competitive bidding, price negotiation, quality inspection
>
> **Key insight**: You can't have 400 strategic partners. You must segment and apply appropriate engagement level.
>
> **Automotive example:**
> - Toyota treats Denso as Tier 1 strategic partner (partially owned, co-developed hybrid system)
> - Ford treats Bosch similarly for powertrains
> - But fastener suppliers? Tier 3 - competitive bidding every year"

##### Slide 9: Supplier Development and Collaboration Models
**Visual:** Collaboration framework diagram
**Instructor Script:**
> "For strategic suppliers, engagement goes beyond transactions. We use structured collaboration models.
>
> **1. Black Box Approach** (Supplier responsible for complete solution)
> - **OEM provides**: Functional requirements, interface specifications, validation criteria
> - **Supplier delivers**: Complete subsystem design, testing, documentation
> - **Example**: Infotainment system - specify features and interfaces, supplier designs everything
> - **Pros**: Leverages supplier expertise, reduces OEM workload
> - **Cons**: Less control, dependency on supplier, potential IP limitations
>
> **2. Gray Box Approach** (Shared responsibility)
> - **OEM provides**: Architecture, key requirements, some design constraints
> - **Supplier contributes**: Detailed design, manufacturing process, component selection
> - **Joint activities**: Design reviews, testing, validation
> - **Example**: Electric motor - OEM defines performance curves and mounting, supplier designs internals
> - **Pros**: Balanced control and expertise utilization
> - **Cons**: Requires tight coordination, clear interface definitions
>
> **3. White Box Approach** (OEM-led design)
> - **OEM provides**: Complete design specifications, potentially reference design
> - **Supplier provides**: Manufacturing capability, process expertise
> - **Example**: Proprietary ECU - OEM designs, supplier manufactures
> - **Pros**: Full control, IP ownership
> - **Cons**: Requires OEM expertise, higher engineering burden
>
> **Hybrid Model - Most Common in Automotive:**
> - Strategic components: Gray/White box (e.g., battery packs, safety systems)
> - Standard components: Black box (e.g., seat heaters, mirrors)
> - Critical safety: White box (e.g., brake ECU design)
>
> **Selection criteria**: Technology maturity, competitive differentiation, IP strategy, capability gaps"

##### Slide 10: Supplier Performance Management
**Visual:** Scorecard showing key metrics
**Instructor Script:**
> "Engagement isn't one-time - it's ongoing performance management. Here's how professionals do it:
>
> **Supplier Scorecard - Key Performance Indicators (KPIs):**
>
> **Quality Metrics (40% weight):**
> - PPM (Parts Per Million defect rate): Target <50 PPM
> - Field failure rate: Target <10 failures per 10,000 vehicles
> - Warranty cost per vehicle: Target <$5
> - First-time quality pass rate: Target >99%
>
> **Delivery Metrics (30% weight):**
> - On-time delivery: Target >98%
> - Schedule adherence: Deviation <±1 week
> - Volume flexibility: Ability to adjust ±20% on 4-week notice
>
> **Cost Metrics (15% weight):**
> - Year-over-year cost reduction: Target 3-5% annually
> - Total cost of ownership (not just piece price)
> - Value engineering contributions
>
> **Development Metrics (10% weight):**
> - Engineering change request response time
> - Design validation completion on schedule
> - Innovation proposals submitted
>
> **Responsiveness Metrics (5% weight):**
> - Issue resolution time
> - Communication effectiveness
> - Management engagement
>
> **Scoring System:**
> - 90-100: Excellent (Strategic partner candidates)
> - 70-89: Good (Maintain relationship)
> - 50-69: Needs improvement (Performance plan required)
> - <50: Unacceptable (Consider replacement)
>
> **Real example - Toyota Supplier Management:**
> - Quarterly scorecards sent to all Tier 1 suppliers
> - Annual supplier convention - top performers recognized
> - Low performers: Joint improvement teams (kaizen events)
> - Persistent low performers: Phased replacement
>
> **Best practice**: Make metrics transparent. Supplier should know score before you do (self-assessment)."

##### Slide 11: Early Supplier Involvement (ESI)
**Visual:** Timeline showing traditional vs ESI development process
**Instructor Script:**
> "One of the most powerful strategies: involve suppliers EARLY in development.
>
> **Traditional Approach (Waterfall):**
> 1. OEM completes design (18 months)
> 2. OEM creates specifications
> 3. OEM sends RFQ (Request for Quote) to suppliers
> 4. Suppliers bid (3 months)
> 5. OEM selects supplier
> 6. Supplier discovers design is difficult/expensive to manufacture
> 7. Extensive rework required (6-12 months delay)
> **Total time**: 27-30 months + delays
>
> **Early Supplier Involvement (ESI) Approach:**
> 1. OEM defines concept and high-level requirements
> 2. OEM invites strategic suppliers to co-develop (Month 3)
> 3. Joint engineering teams design for manufacturability
> 4. Supplier input on cost optimization, process capability
> 5. Design validated with supplier's manufacturing process
> 6. Smooth transition to production
> **Total time**: 20-24 months, fewer surprises
>
> **ESI Benefits:**
> - **Design for Manufacturing (DFM)**: Supplier brings manufacturing expertise early
> - **Cost optimization**: Avoid expensive features with marginal value
> - **Risk reduction**: Manufacturing issues caught in design phase, not production
> - **Faster time-to-market**: Parallel development, no rework loops
> - **Innovation**: Supplier brings latest technologies and ideas
>
> **ESI Challenges:**
> - **IP concerns**: Sharing designs before supplier selection finalized
> - **Multiple supplier management**: Can't involve all bidders (too many)
> - **Commitment risk**: Supplier invests time before contract awarded
>
> **Solutions:**
> - Use NDAs and limited technical disclosure
> - Involve 2-3 pre-selected suppliers (competitive ESI)
> - Compensate suppliers for ESI participation (development fees)
> - Clear communication on selection criteria
>
> **Automotive examples:**
> - **Tesla + Panasonic**: Co-developed Gigafactory battery technology
> - **GM + LG**: Joint development of Ultium battery platform
> - **Ford + Bosch**: Co-development of electric drive units
>
> **Recommendation**: For complex, strategic components, ESI is no longer optional - it's competitive necessity."

---

#### **Part 2: Contract Management** (Slides 12-14, ~8 minutes)

##### Slide 12: Types of Contracts in Automotive Systems
**Visual:** Contract type comparison matrix
**Instructor Script:**
> "Contracts are the legal framework for agreements. Choose wrong contract type, and you're exposed to risk.
>
> **1. Fixed-Price Contracts (Firm Fixed Price - FFP)**
> - **Description**: Supplier agrees to deliver for fixed price, regardless of costs
> - **When to use**: Well-defined scope, mature technology, low risk
> - **Risk allocation**: Supplier bears cost risk
> - **Example**: Commodity components (fasteners, standard connectors)
> - **Pros**: Predictable cost, supplier incentivized to be efficient
> - **Cons**: Supplier may cut corners on quality to preserve margin
>
> **2. Cost-Plus Contracts (Cost Plus Fixed Fee - CPFF)**
> - **Description**: OEM reimburses supplier's costs + fixed fee/margin
> - **When to use**: Uncertain scope, new technology, high development risk
> - **Risk allocation**: OEM bears cost risk
> - **Example**: First-of-kind autonomous driving sensor development
> - **Pros**: Encourages innovation, doesn't penalize supplier for unknowns
> - **Cons**: No cost control, supplier has limited incentive to optimize
>
> **3. Cost-Plus-Incentive Fee (CPIF)**
> - **Description**: Reimbursement + performance-based incentives
> - **When to use**: Development with measurable objectives
> - **Risk allocation**: Shared
> - **Example**: Battery development with range targets (bonus for exceeding targets)
> - **Pros**: Aligns incentives, rewards performance
> - **Cons**: Complex to administer, requires clear metrics
>
> **4. Time & Materials (T&M)**
> - **Description**: Pay for labor hours and materials at agreed rates
> - **When to use**: Scope cannot be defined, consulting/support services
> - **Risk allocation**: OEM bears risk of hours expanding
> - **Example**: Software debugging support, prototype development
> - **Pros**: Flexibility, easy to start
> - **Cons**: Open-ended cost, requires close monitoring
>
> **5. Licensing Agreements**
> - **Description**: Pay for right to use technology/IP
> - **Forms**: Per-unit royalty, lump-sum, subscription
> - **Example**: Qualcomm chips (per-vehicle license), AUTOSAR licenses
>
> **Automotive standard practice:**
> - **Development phase**: Cost-plus or T&M (uncertainty high)
> - **Production phase**: Fixed price (volume known, mature design)
> - **Transition**: Move from cost-plus to fixed price as uncertainty reduces
>
> **Risk management**: Contract type is a systems engineering decision, not just procurement."

##### Slide 13: Critical Contract Clauses for Systems Engineers
**Visual:** Checklist of essential contract elements
**Instructor Script:**
> "As systems engineers, you'll work with contracts departments, but YOU must ensure these technical clauses are included:
>
> **1. Technical Requirements and Specifications**
> - Reference to requirements documents (with version control)
> - Performance criteria and acceptance tests
> - Compliance with standards (ISO 26262, ASPICE, etc.)
> - **Why it matters**: These are YOUR requirements - verify they're correctly captured
>
> **2. Intellectual Property (IP) Ownership**
> - **Background IP**: What supplier brings (they own)
> - **Foreground IP**: What's developed under contract (negotiated ownership)
> - **License rights**: Can OEM modify? Share with other suppliers?
> - **Example clause**: 'OEM owns all IP developed specifically for this project. Supplier retains IP on standard platform components but grants OEM perpetual license.'
> - **Why it matters**: Affects your ability to change suppliers, modify designs, reuse across programs
>
> **3. Change Control Process**
> - Engineering Change Order (ECO) procedure
> - Who can authorize changes? What's the approval process?
> - Cost and schedule impact assessment required
> - **Why it matters**: Prevents scope creep, ensures traceable changes
>
> **4. Quality and Inspection Rights**
> - Quality standards and acceptance criteria (e.g., PPAP - Production Part Approval Process)
> - OEM right to audit supplier facilities
> - First article inspection requirements
> - Corrective action process (8D methodology)
> - **Why it matters**: Your verification and validation plans depend on this
>
> **5. Delivery and Performance Schedules**
> - Milestone dates with deliverables defined
> - Penalties for late delivery (liquidated damages)
> - Early delivery incentives
> - Force majeure clauses (what happens in crisis like chip shortage?)
>
> **6. Warranty and Liability**
> - Warranty period (typically 3-5 years automotive)
> - Defect correction obligations
> - Liability caps and indemnification
> - Recall cost sharing (critical in automotive!)
> - **Example**: 'Supplier warrants components will be free from defects for 5 years/100,000 km. In event of recall due to supplier defect, supplier bears 70% of recall costs up to $10M.'
>
> **7. Transition and Exit Provisions**
> - What happens at end of contract or if supplier is replaced?
> - Transition assistance required
> - Documentation and tooling handover
> - **Why it matters**: Ensures business continuity
>
> **8. Cybersecurity and Data Protection (Increasingly Critical)**
> - Security requirements compliance (ISO 21434, SAE J3061)
> - Data ownership and protection
> - Incident reporting and response
>
> **9. Continuous Improvement**
> - Year-over-year cost reduction commitments
> - Value engineering participation
> - Technology roadmap alignment
>
> **Red flags to watch for:**
> - Vague technical specifications ('industry standard quality')
> - No IP clarity (disputes later)
> - No change control (chaos)
> - Unlimited supplier liability (supplier won't sign) or zero liability (OEM fully exposed)
>
> **Best practice**: Systems engineers should review contracts BEFORE signature to ensure technical feasibility and requirement coverage."

##### Slide 14: Contract Monitoring and Performance Tracking
**Visual:** Dashboard showing contract health indicators
**Instructor Script:**
> "Signing contract is just the beginning. Active management is essential.
>
> **Contract Health Dashboard - Key Indicators:**
>
> **1. Schedule Performance Index (SPI)**
> - Formula: SPI = Earned Value / Planned Value
> - SPI < 1.0: Behind schedule
> - **Action trigger**: SPI < 0.9 → escalate to management
>
> **2. Cost Performance Index (CPI)**
> - Formula: CPI = Earned Value / Actual Cost
> - CPI < 1.0: Over budget
> - **Action trigger**: CPI < 0.95 → review cost drivers
>
> **3. Requirements Compliance Rate**
> - % of requirements verified and passing
> - **Target**: >95% at major milestones
> - **Action trigger**: <90% → root cause analysis
>
> **4. Change Request Volume**
> - Number of ECOs per month
> - High volume indicates poor initial requirements or scope creep
> - **Action trigger**: >10% change rate → process review
>
> **5. Risk Status**
> - Number of open risks and trends
> - Risk exposure (probability × impact)
> - **Action trigger**: High risks not mitigated → escalation
>
> **6. Payment Status**
> - Milestone payments vs deliverables completed
> - Ensures payment tied to verified delivery
>
> **Review Cadence:**
> - **Weekly**: Working-level team (technical progress)
> - **Monthly**: Management review (schedule, cost, risks)
> - **Quarterly**: Executive business review (strategic alignment, scorecard)
> - **Ad-hoc**: Triggered by red indicators
>
> **Real example - Automotive Program:**
> - Supplier contracted to deliver ADAS camera module
> - Monthly reviews showed SPI declining (1.0 → 0.85 over 6 months)
> - Root cause: Supplier underestimated software complexity
> - **Action**: Moved from fixed-price to T&M for software completion + added resource
> - **Outcome**: Recovered schedule, but cost increased 15%
> - **Lesson**: Early detection through monitoring prevented complete failure
>
> **Governance structure**: Clear roles - who monitors, who escalates, who decides on corrective actions."

---

#### **Part 3: Vendor Selection Criteria and Process** (Slides 15-17, ~10 minutes)

##### Slide 15: Systematic Vendor Selection Process
**Visual:** Flowchart showing selection process stages
**Instructor Script:**
> "Vendor selection is a structured process, not a popularity contest or 'who has the best brochure.'
>
> **Phase 1: Market Research and RFI (Request for Information)** (2-4 weeks)
> - Identify potential suppliers through market research
> - Send RFI to 8-12 candidates requesting:
>   - Company background and financial stability
>   - Relevant experience and references
>   - Technical capabilities and capacity
>   - Quality certifications (IATF 16949, ISO 9001)
> - **Output**: Shortlist of 4-6 qualified candidates
>
> **Phase 2: RFP/RFQ (Request for Proposal/Quote)** (6-8 weeks)
> - Send detailed requirements and specifications to shortlist
> - Request:
>   - Technical approach and proposed solution
>   - Project plan and timeline
>   - Detailed pricing (development + production)
>   - Quality plan and test strategy
>   - Risk assessment
> - **Output**: Detailed proposals from each candidate
>
> **Phase 3: Evaluation and Scoring** (4-6 weeks)
> - Cross-functional evaluation team (engineering, quality, procurement, manufacturing)
> - Systematic scoring against weighted criteria (see next slide)
> - **Supplier presentations**: Allow suppliers to present and answer questions
> - **Site visits**: Visit supplier facilities (critical for high-value contracts)
> - **Reference checks**: Contact other OEM customers
> - **Output**: Scored comparison matrix
>
> **Phase 4: Negotiation and Selection** (3-4 weeks)
> - Negotiate with top 2-3 candidates
> - Clarify technical details, pricing, terms
> - Final business case comparison
> - **Decision**: Select supplier or split award (multiple sources for risk mitigation)
>
> **Phase 5: Contract Award and Kick-off** (2 weeks)
> - Execute contract
> - Kick-off meeting with supplier
> - Establish governance structure
> - **Output**: Active contract with defined working relationships
>
> **Total timeline**: 4-6 months for strategic components
>
> **Automotive example:**
> - New EV program needs battery pack supplier
> - RFI sent to 12 battery manufacturers
> - Shortlist: 5 companies (based on capacity, safety record, technology)
> - RFP with detailed specs (energy density, safety, cost targets)
> - Evaluation: Technical, cost, production readiness
> - Final negotiation with top 2
> - **Decision**: Dual source (70% primary, 30% secondary for risk mitigation)
>
> **Critical success factor**: Defined criteria BEFORE receiving proposals (prevents bias)."

##### Slide 16: Vendor Evaluation Criteria and Scoring
**Visual:** Weighted scoring matrix with example
**Instructor Script:**
> "How do you compare vendors objectively? Use weighted multi-criteria scoring.
>
> **Evaluation Criteria Framework:**
>
> **Technical Capability (35% weight):**
> - Solution meets requirements (10 points)
> - Technical maturity/readiness level (8 points)
> - Innovation and value-add (5 points)
> - Compliance with standards (ISO 26262, ASPICE) (7 points)
> - Scalability and future-proofing (5 points)
> - **Subtotal**: 35 points
>
> **Quality and Reliability (25% weight):**
> - Quality certifications (IATF 16949, ISO 9001) (5 points)
> - Historical quality metrics (PPM, field failures) (8 points)
> - Quality management processes (7 points)
> - Warranty and support terms (5 points)
> - **Subtotal**: 25 points
>
> **Cost and Commercial (20% weight):**
> - Total cost of ownership (not just piece price) (10 points)
> - Development cost and payment terms (5 points)
> - Cost reduction roadmap (3 points)
> - Commercial terms favorability (2 points)
> - **Subtotal**: 20 points
>
> **Delivery and Capacity (15% weight):**
> - Production capacity and scalability (6 points)
> - Timeline and schedule confidence (5 points)
> - Supply chain robustness (4 points)
> - **Subtotal**: 15 points
>
> **Business and Relationship (5% weight):**
> - Financial stability (Dun & Bradstreet rating) (2 points)
> - Geographic presence and localization (1 point)
> - Relationship and cultural fit (1 point)
> - Sustainability and ESG performance (1 point)
> - **Subtotal**: 5 points
>
> **Total possible**: 100 points
>
> **Example Scoring - Battery Supplier Selection:**
>
> | Criteria | Weight | Supplier A | Supplier B | Supplier C |
> |----------|--------|------------|------------|------------|
> | Technical | 35% | 30/35 (86%) | 33/35 (94%) | 28/35 (80%) |
> | Quality | 25% | 22/25 (88%) | 20/25 (80%) | 24/25 (96%) |
> | Cost | 20% | 18/20 (90%) | 15/20 (75%) | 16/20 (80%) |
> | Delivery | 15% | 12/15 (80%) | 14/15 (93%) | 13/15 (87%) |
> | Business | 5% | 4/5 (80%) | 5/5 (100%) | 3/5 (60%) |
> | **TOTAL** | **100%** | **86/100** | **87/100** | **84/100** |
>
> **Analysis:**
> - Supplier B: Highest overall score (87) - strong technical, excellent delivery
> - Supplier C: Highest quality, but weaker business stability
> - Supplier A: Balanced, strong cost position
>
> **Decision considerations:**
> - If quality is paramount: Supplier C (despite lower total)
> - If cost-sensitive: Supplier A
> - If balanced risk: Supplier B
> - **Dual source option**: B (primary, 70%) + C (secondary, 30% for quality benchmark)
>
> **Key principles:**
> - Weights reflect program priorities (safety-critical = higher quality weight)
> - Score with cross-functional team (not engineering alone)
> - Document rationale for scores (auditable)
> - Use same criteria for all vendors (fairness)
>
> **Common mistake**: Choosing based on cost alone. Remember: 'Bitterness of poor quality lasts long after sweetness of low price is forgotten.'"

##### Slide 17: Due Diligence and Risk Assessment
**Visual:** Risk assessment matrix for suppliers
**Instructor Script:**
> "Before finalizing selection, conduct thorough due diligence. Suppliers can look good on paper but fail in reality.
>
> **Technical Due Diligence:**
>
> **1. Facility Visit and Audit**
> - Manufacturing capability (equipment, processes)
> - Quality systems (inspection, testing, calibration)
> - Engineering capability (design tools, staff expertise)
> - Cleanliness and organization (5S methodology)
> - **Red flags**: Outdated equipment, poor housekeeping, undertrained staff
>
> **2. Reference Checks**
> - Contact 3-5 existing customers
> - Questions:
>   - Quality performance (PPM rates)
>   - Delivery reliability
>   - Responsiveness to issues
>   - Would you use them again?
> - **Red flag**: Reluctance to provide references or references are lukewarm
>
> **3. Technology Demonstration**
> - Request working prototype or proof-of-concept
> - Test against key requirements
> - Validate claims made in proposal
> - **Red flag**: Inability to demonstrate claimed capabilities
>
> **Financial Due Diligence:**
>
> **1. Financial Health Assessment**
> - Review financial statements (balance sheet, cash flow)
> - Dun & Bradstreet credit rating
> - Debt-to-equity ratio (high debt = risk)
> - **Red flags**: Negative cash flow, declining revenue, high debt
>
> **2. Supply Chain Assessment**
> - Are they dependent on single sources?
> - Do they have inventory buffers?
> - Geographic concentration risk (e.g., all in one country)
> - **Red flag**: Brittle supply chain (learned from chip shortage)
>
> **3. Business Continuity Planning**
> - Disaster recovery plans
> - Backup production capacity
> - Insurance coverage (product liability, recall)
>
> **Legal and Compliance Due Diligence:**
> - Litigation history (being sued by other customers?)
> - Regulatory compliance (environmental, labor)
> - Cybersecurity posture (ISO 27001, incident history)
> - IP ownership clarity (do they own what they claim?)
>
> **Risk Assessment Matrix:**
>
> | Risk Category | Example | Probability | Impact | Mitigation |
> |---------------|---------|-------------|--------|------------|
> | Technical | Cannot meet performance specs | Medium | High | Require proof-of-concept before award |
> | Financial | Supplier bankruptcy | Low | Critical | Financial monitoring, dual source |
> | Supply Chain | Sub-tier shortage | High | High | Require supply chain transparency, buffer inventory |
> | Quality | High defect rates | Medium | High | Enhanced quality agreement, resident engineer |
> | Capacity | Cannot scale to volume | Medium | Medium | Validate capacity plan, backup supplier |
>
> **Real example - Automotive Supplier Failure:**
> - OEM selected low-cost supplier for safety sensors
> - Due diligence was minimal (cost-driven decision)
> - 6 months into production: supplier quality collapsed (PPM >5000)
> - Root cause: Supplier took on too many customers, overextended capacity
> - **Result**: OEM had to qualify new supplier mid-production ($20M cost, 4-month delay)
> - **Lesson**: Thorough due diligence prevents costly surprises
>
> **Decision rule**: If due diligence uncovers major red flags, **do not proceed regardless of score**. No supplier is worth program failure."

---

#### **Part 4: Make vs Buy Decision Analysis** (Slides 18-20, ~10 minutes)

##### Slide 18: Make vs Buy Decision Framework
**Visual:** Decision tree showing analysis factors
**Instructor Script:**
> "One of the most strategic decisions in systems engineering: Should we make this in-house or buy from supplier?
>
> **This isn't just about cost** - it's about strategy, capability, risk, and competitive advantage.
>
> **Framework for Make vs Buy Analysis:**
>
> **1. Strategic Importance**
> - **Core competency?** Is this technology central to our competitive differentiation?
> - **IP value?** Do we need to own the intellectual property?
> - **Customer visibility?** Do customers care who makes this?
>
> **Decision guidance:**
> - **Strategic/Core**: Bias toward MAKE
> - **Non-strategic/Commodity**: Bias toward BUY
>
> **Examples:**
> - Tesla: MAKE battery management, autonomous driving algorithms (core differentiation)
> - Tesla: BUY seats, lighting, fasteners (commodity, no differentiation)
>
> **2. Technical Capability**
> - **Do we have expertise?** In-house engineering capability and experience
> - **Can we acquire expertise?** Time and cost to build capability
> - **Supplier expertise?** Are suppliers more capable than we could become?
>
> **Decision guidance:**
> - **Have capability**: MAKE feasible
> - **Capability gap + long time to acquire**: BUY
> - **Capability gap + strategic**: Acquire/develop + MAKE
>
> **Example:**
> - Traditional OEM entering EV market lacks battery expertise
> - **Short-term**: BUY battery packs from LG/CATL (faster time-to-market)
> - **Long-term**: Develop in-house expertise (strategic importance)
> - **Transition**: Move from BUY to MAKE over 5-7 years
>
> **3. Capacity and Scale**
> - **Production volume?** Do we have volume to justify investment?
> - **Utilization?** Will our facilities run efficiently?
> - **Scalability?** Can we scale up/down with demand?
>
> **Decision guidance:**
> - **High volume + stable demand**: MAKE (economies of scale)
> - **Low volume + variable demand**: BUY (supplier spreads costs across customers)
>
> **Example:**
> - Tesla Gigafactory produces millions of battery cells → MAKE justified
> - Low-volume supercar (1000 units/year) → BUY from supplier
>
> **4. Cost Analysis (Total Cost of Ownership)**
> - **Make costs**: R&D, tooling, facilities, labor, materials, overhead, opportunity cost
> - **Buy costs**: Supplier price, transaction costs, quality assurance, management overhead
> - **Hidden costs**: Both sides have hidden costs!
>
> **Decision guidance:**
> - If MAKE cost < BUY cost by >20%: MAKE
> - If BUY cost < MAKE cost by >20%: BUY
> - If within 20%: Decide based on strategic factors
>
> **5. Risk Assessment**
> - **Supply risk**: What if supplier fails, raises prices, or becomes competitor?
> - **Technology risk**: What if we invest in making but technology changes?
> - **Quality risk**: Where is quality more controllable?
> - **Flexibility risk**: Which option preserves future options?
>
> **Decision guidance:**
> - **High supply risk** (e.g., single source): MAKE
> - **High technology risk** (rapidly evolving): BUY (avoid obsolete investment)
> - **Critical quality**: MAKE (more control)
>
> **6. Time to Market**
> - **How quickly do we need this?**
> - **Make timeline**: Facility build, equipment procurement, ramp-up (2-4 years)
> - **Buy timeline**: Supplier selection, development, production (6-18 months)
>
> **Decision guidance:**
> - **Urgent**: BUY (faster)
> - **Long-term roadmap**: MAKE (if strategic)
>
> **Recommendation**: Evaluate ALL factors, not just one. Use weighted decision matrix (from Session 10)."

##### Slide 19: Make vs Buy Decision Matrix Example
**Visual:** Completed decision analysis for automotive component
**Instructor Script:**
> "Let's work through a real example: Should an automotive OEM make or buy electric motor for new EV?
>
> **Component**: Electric Traction Motor (250 kW for midsize EV)
>
> **Evaluation Criteria and Scoring:**
>
> | Criterion | Weight | MAKE Score | BUY Score | MAKE Weighted | BUY Weighted |
> |-----------|--------|------------|-----------|---------------|--------------|
> | **Strategic Importance** | 25% | 8/10 (Important for EV differentiation) | 4/10 (Commodity from supplier) | 2.0 | 1.0 |
> | **Technical Capability** | 20% | 5/10 (Limited experience, would need to acquire) | 9/10 (Suppliers very capable) | 1.0 | 1.8 |
> | **Cost** | 20% | 6/10 (High initial investment, lower long-term) | 7/10 (No upfront, but ongoing supplier margin) | 1.2 | 1.4 |
> | **Quality & Reliability** | 15% | 7/10 (Full control once established) | 8/10 (Suppliers proven track record) | 1.05 | 1.2 |
> | **Time to Market** | 10% | 3/10 (3-4 years to build capability) | 9/10 (Supplier ready in 12-18 months) | 0.3 | 0.9 |
> | **Risk** | 10% | 7/10 (Technology risk, but supply chain secure) | 5/10 (Supply risk, price risk) | 0.7 | 0.5 |
> | **Total** | 100% | - | - | **6.25/10** | **6.8/10** |
>
> **Analysis:**
> - **BUY scores higher (6.8 vs 6.25)** - but it's close!
> - **MAKE strengths**: Strategic control, long-term cost, supply chain security
> - **BUY strengths**: Technical capability, time to market, immediate quality
>
> **Decision factors to consider:**
>
> **If OEM chooses BUY:**
> - Faster to market (competitive advantage in fast-moving EV market)
> - Leverage supplier expertise
> - Lower upfront investment
> - **Risk**: Dependent on supplier, less differentiation, ongoing costs
> - **Strategy**: Dual-source motors to mitigate supply risk
>
> **If OEM chooses MAKE:**
> - Long-term cost advantage (if volume >100k units/year)
> - Technology ownership and differentiation
> - Complete control over roadmap
> - **Risk**: 3-4 year delay, need to acquire expertise
> - **Strategy**: Partner with motor specialist initially, bring in-house over time
>
> **Actual industry examples:**
>
> **Tesla - MAKE decision:**
> - Designed proprietary motor (permanent magnet synchronous motor)
> - Rationale: Core differentiation, high volume (500k+ units/year), vertical integration strategy
> - Built in-house motor production at Gigafactories
>
> **Ford - BUY decision:**
> - Sources motors from suppliers (e.g., BorgWarner, Hitachi)
> - Rationale: Faster to market, leverage supplier expertise, lower volume per model
> - Focus internal resources on battery and software (higher strategic value)
>
> **Hybrid approach - GM:**
> - Initially bought motors (Volt, Bolt)
> - Developed in-house motor expertise over time
> - Now manufactures Ultium platform motors in-house (high volume, strategic)
>
> **Key insight**: Make vs Buy is **NOT permanent**. Can transition over time as volumes, capabilities, and strategies evolve."

##### Slide 20: Make vs Buy Special Considerations in Automotive
**Visual:** Automotive-specific decision factors
**Instructor Script:**
> "Automotive industry has unique factors that influence make vs buy decisions:
>
> **1. Safety Certification Requirements (ISO 26262)**
> - Safety-critical components require ASIL certification
> - **Make**: Full control over safety process, but need internal ASIL capability
> - **Buy**: Supplier responsible for ASIL certification, but OEM still liable
> - **Example**: Brake systems typically bought from certified suppliers (Bosch, Continental) - they have decades of ASIL expertise
>
> **2. Recall Liability**
> - OEM is ultimately responsible for recalls, even if supplier defect
> - **Make**: Direct control over root cause and fix
> - **Buy**: Dependent on supplier for corrective action, but OEM faces public blame
> - **Strategy**: Critical safety items often made in-house or dual-sourced to mitigate risk
>
> **3. Regulatory and Homologation**
> - Vehicles must be certified in each market (FMVSS in US, ECE in Europe, etc.)
> - **Make**: OEM manages entire certification
> - **Buy**: Supplier provides compliance documentation, OEM integrates
> - **Complexity**: Global OEMs sell in 100+ countries - homologation is massive effort
>
> **4. Platform Sharing and Economies of Scale**
> - Modern OEMs share platforms across multiple vehicle models
> - **Make**: Easier to standardize across platform (design once, use everywhere)
> - **Buy**: Can still standardize by using same supplier part across models
> - **Example**: VW Group MQB platform - shared components across VW, Audi, Skoda, Seat
> - **Decision**: Platform components often made in-house for maximum reuse
>
> **5. Technology Lifecycle (Automotive is Long)**
> - Vehicles have 10-15 year production lifecycle
> - Component must be available for production + 10-15 years service parts
> - **Make**: Full control over obsolescence management
> - **Buy**: Require supplier to commit to 25-year availability (challenge for electronics)
> - **Risk**: Suppliers discontinue components, forcing costly redesigns
> - **Strategy**: End-of-life buy agreements, escrow of designs/tooling
>
> **6. Competitive Dynamics**
> - If you BUY from supplier, do they also sell to your competitors?
> - **Risk**: No differentiation, supplier gains leverage
> - **Example**: Multiple OEMs use same Bosch radar sensors → limited differentiation
> - **Strategy**: Exclusive agreements (costly), or MAKE for differentiation
>
> **7. Vertical Integration Trends**
> - **Traditional OEMs**: Low vertical integration (20-30%) - focus on assembly, powertrain
> - **Tesla model**: High vertical integration (50%+) - batteries, motors, software, even seats
> - **Rationale**:
>   - Tesla: Speed, cost control, vertical integration = competitive advantage
>   - Traditional: Flexibility, asset-light, focus on brand/distribution
> - **No universal answer** - depends on company strategy
>
> **8. Software-Defined Vehicles (Emerging Factor)**
> - Modern vehicles are 'computers on wheels' - software is differentiator
> - **MAKE decision increasingly common for software**: In-house control over updates, features, user experience
> - **BUY for hardware, MAKE for software**: Hybrid approach
> - **Example**: OEMs buy hardware from suppliers but develop software stacks in-house
>
> **Decision framework summary:**
>
> **MAKE when:**
> - Strategic/core technology
> - High volume (>100k units/year)
> - Critical safety/quality control needed
> - IP ownership essential
> - Long-term cost advantage clear
>
> **BUY when:**
> - Commodity/non-differentiating
> - Low volume or variable demand
> - Supplier has superior expertise
> - Time to market critical
> - Technology rapidly evolving (avoid obsolete investment)
>
> **HYBRID (Partner/Co-develop) when:**
> - Strategic but capability gap exists
> - Shared risk/investment makes sense
> - Want to develop in-house expertise over time
>
> **Remember**: This is a **strategic decision** that should involve executive leadership, not just engineering."

---

#### **Part 5: Infrastructure Requirements Planning** (Slides 21-22, ~6 minutes)

##### Slide 21: Infrastructure Lifecycle Support Requirements
**Visual:** Infrastructure ecosystem diagram
**Instructor Script:**
> "Systems don't exist in isolation - they require infrastructure throughout their lifecycle. Often overlooked until it's too late.
>
> **Infrastructure Categories:**
>
> **1. Development Infrastructure**
>
> **Engineering Tools:**
> - CAD/CAE software (CATIA, Siemens NX)
> - Simulation tools (MATLAB/Simulink, ANSYS)
> - Requirements management (DOORS, Jama)
> - Model-based systems engineering (SysML tools)
> - **Requirements**: Licenses, training, IT support, interoperability
>
> **Testing Equipment:**
> - Hardware-in-the-loop (HIL) test systems
> - Environmental chambers (temperature, humidity, vibration)
> - Electromagnetic compatibility (EMC) test chambers
> - Dynamometers (powertrain testing)
> - Crash test facilities
> - **Requirements**: Calibration schedules, maintenance, operator training
>
> **IT Infrastructure:**
> - PLM (Product Lifecycle Management) systems
> - Version control (Git, SVN)
> - Collaboration platforms (SharePoint, Confluence)
> - High-performance computing (for simulation)
> - **Requirements**: Cybersecurity, backups, disaster recovery, access control
>
> **2. Manufacturing Infrastructure**
>
> **Production Equipment:**
> - Assembly lines and robotics
> - Machining centers (CNC)
> - Welding and joining equipment
> - Paint and coating systems
> - **Requirements**: Maintenance schedules, spare parts, operator training, safety systems
>
> **Quality Control:**
> - Coordinate measuring machines (CMM)
> - Non-destructive testing (X-ray, ultrasound)
> - In-process inspection systems
> - **Requirements**: Calibration, statistical process control (SPC), traceability
>
> **Logistics:**
> - Warehouse management systems (WMS)
> - Material handling equipment
> - Inventory tracking (RFID, barcodes)
> - **Requirements**: Integration with ERP systems, real-time visibility
>
> **3. Service and Support Infrastructure**
>
> **Diagnostic Tools:**
> - Scan tools and diagnostic software
> - Specialized test equipment for service centers
> - Remote diagnostic capabilities (telematics)
> - **Requirements**: Regular updates, backward compatibility, dealer training
>
> **Service Networks:**
> - Dealer service centers
> - Training facilities for technicians
> - Technical support hotlines
> - **Requirements**: Geographic coverage, response time SLAs, escalation paths
>
> **Spare Parts Management:**
> - Parts warehousing and distribution
> - Forecasting and inventory optimization
> - Obsolescence management
> - **Requirements**: 10-15 year availability, cost-effective storage
>
> **4. IT and Cybersecurity Infrastructure (Increasingly Critical)**
>
> **Connected Vehicle Backend:**
> - Cloud infrastructure for OTA (over-the-air) updates
> - Telematics data collection and analysis
> - Customer apps and portals
> - **Requirements**: Scalability (millions of vehicles), security, uptime (99.9%+)
>
> **Cybersecurity:**
> - Security Operations Center (SOC)
> - Intrusion detection systems
> - Incident response capabilities
> - **Requirements**: ISO 21434 compliance, 24/7 monitoring, threat intelligence
>
> **Infrastructure Planning Challenges:**
>
> **Challenge 1: Long Lead Times**
> - Major test equipment: 12-18 months procurement and installation
> - Manufacturing lines: 24-36 months design and commissioning
> - **Implication**: Infrastructure planning must start EARLY in system development (not afterthought)
>
> **Challenge 2: Obsolescence**
> - IT systems evolve every 3-5 years
> - Vehicle lifecycle is 10-15 years
> - **Strategy**: Modular architecture, open standards, technology refresh plans
>
> **Challenge 3: Cost**
> - Infrastructure is capital-intensive (not always visible in product cost)
> - Example: Full vehicle development program infrastructure cost: $500M - $2B
> - **Strategy**: Shared infrastructure across programs, cloud/SaaS where possible
>
> **Best practice**: Develop Infrastructure Requirements Document alongside System Requirements - ensure infrastructure is engineered, not assumed."

##### Slide 22: Infrastructure Requirements Specification
**Visual:** Example infrastructure requirements template
**Instructor Script:**
> "Infrastructure requirements should be as rigorous as system requirements. Here's how to specify them:
>
> **Infrastructure Requirement Structure:**
> Same format as system requirements (from Session 4)
>
> **Example - Testing Infrastructure Requirements:**
>
> **Functional Requirements:**
> - INF-TEST-001: 'The HIL test system shall support simulation of 8 ECU nodes simultaneously'
> - INF-TEST-002: 'The environmental chamber shall accommodate test articles up to 2m × 1m × 1m'
> - INF-TEST-003: 'The test data management system shall store 10 years of test results with traceability to requirements'
>
> **Performance Requirements:**
> - INF-TEST-010: 'The HIL system shall execute real-time simulations with maximum 1ms latency'
> - INF-TEST-011: 'The environmental chamber shall achieve temperature range -40°C to +125°C with ±2°C accuracy'
> - INF-TEST-012: 'The EMC chamber shall provide shielding effectiveness >100 dB from 10 kHz to 40 GHz'
>
> **Availability Requirements:**
> - INF-TEST-020: 'Test equipment shall have minimum 95% uptime during business hours'
> - INF-TEST-021: 'Calibration shall be performed annually per ISO 17025 standards'
> - INF-TEST-022: 'Backup systems shall be available for critical test equipment (maximum 24-hour switchover)'
>
> **Integration Requirements:**
> - INF-TEST-030: 'HIL system shall integrate with test management tool (JIRA, TestRail) via API'
> - INF-TEST-031: 'Test data shall be automatically uploaded to PLM system upon test completion'
>
> **Support and Maintenance Requirements:**
> - INF-TEST-040: 'Vendor shall provide 24/7 technical support with 4-hour response time'
> - INF-TEST-041: 'Spare parts for critical equipment shall be stocked on-site (max 4-hour replacement)'
> - INF-TEST-042: 'Equipment shall include remote diagnostics capability for vendor support'
>
> **Lifecycle Requirements:**
> - INF-TEST-050: 'Equipment shall be supported by vendor for minimum 15 years'
> - INF-TEST-051: 'Software/firmware updates shall be provided quarterly at no additional cost for first 5 years'
> - INF-TEST-052: 'Technology refresh path shall be defined with backward compatibility for existing test scripts'
>
> **Example - IT Infrastructure Requirements:**
>
> **Cloud Infrastructure (for connected vehicles):**
> - INF-IT-001: 'Cloud platform shall support 5 million concurrent vehicle connections'
> - INF-IT-002: 'System shall scale automatically to handle 10× traffic spikes (e.g., mass OTA updates)'
> - INF-IT-003: 'Data storage shall provide 99.999% durability (S3 equivalent)'
> - INF-IT-004: 'System uptime shall be ≥99.9% (max 8.76 hours downtime per year)'
> - INF-IT-005: 'Disaster recovery: Recovery Time Objective (RTO) ≤4 hours, Recovery Point Objective (RPO) ≤15 minutes'
>
> **Cybersecurity Infrastructure:**
> - INF-SEC-001: 'Security Operations Center shall provide 24/7/365 monitoring'
> - INF-SEC-002: 'Intrusion detection system shall analyze 100% of inbound/outbound traffic'
> - INF-SEC-003: 'Security incident response shall be initiated within 1 hour of threat detection'
>
> **Total Cost of Ownership (TCO) Considerations:**
>
> Infrastructure costs include:
> - **Capital expenditure (CAPEX)**: Equipment purchase, installation
> - **Operating expenditure (OPEX)**: Maintenance, calibration, energy, staffing
> - **Lifecycle costs**: Upgrades, obsolescence management, decommissioning
>
> **Example TCO - HIL Test System:**
> - Initial purchase: $500k
> - Installation and commissioning: $100k
> - Annual maintenance: $50k
> - Calibration: $10k/year
> - Software licenses: $20k/year
> - Operator training: $15k/year
> - **10-year TCO**: $500k + $100k + ($95k × 10) = $1.55M
> - **Often, OPEX over 10 years exceeds initial CAPEX!**
>
> **Infrastructure Requirements Review:**
> - Cross-functional team: Engineering, IT, manufacturing, service, finance
> - Verify infrastructure supports ALL lifecycle phases (development, production, service)
> - Ensure scalability (can infrastructure grow with program?)
> - Validate vendor support commitments
> - Assess risks (single points of failure, vendor lock-in)
>
> **Common mistake**: Specifying infrastructure at last minute → delays, gaps, suboptimal solutions. **Start infrastructure planning in concept phase.**"

---

#### **Part 6: Lifecycle Management Plans** (Slides 23-24, ~8 minutes)

##### Slide 23: Lifecycle Management Strategy
**Visual:** Lifecycle timeline showing phases and management activities
**Instructor Script:**
> "Systems engineering doesn't end at production launch. Most of a system's lifecycle happens AFTER launch.
>
> **Automotive System Lifecycle Phases:**
>
> **1. Development Phase** (3-5 years)
> - Concept, design, validation, industrialization
> - **Management focus**: Requirements, design, verification
>
> **2. Production Phase** (5-10 years)
> - Active manufacturing and sales
> - **Management focus**: Quality, cost reduction, running changes
>
> **3. Service Phase** (15-20 years)
> - Active vehicle fleet in field
> - **Management focus**: Warranty, recalls, spare parts, software updates
>
> **4. End-of-Life Phase** (5+ years)
> - Production ended, but service continues
> - **Management focus**: Spare parts availability, obsolescence, phase-out
>
> **Total lifecycle**: 25-30+ years from concept to complete phase-out
>
> **Lifecycle Management Plan Components:**
>
> **A. Maintenance Strategy**
>
> **Preventive Maintenance:**
> - Scheduled inspections and service
> - **Example**: Battery pack inspection every 2 years, coolant replacement every 4 years
> - **Requirements**: Service intervals, procedures, special tools
>
> **Predictive Maintenance:**
> - Condition-based using sensor data and analytics
> - **Example**: Monitor battery degradation, predict failure before it happens
> - **Requirements**: Sensors, telematics, analytics algorithms
>
> **Corrective Maintenance:**
> - Repair after failure
> - **Requirements**: Fault diagnostics, repair procedures, spare parts availability
>
> **Design for Maintainability:**
> - Modular design for easy replacement
> - Accessible components (no 'service position' acrobatics)
> - Self-diagnostics and prognostics
> - **Example**: Tesla battery pack initially required lifting car → redesigned for easier access
>
> **B. Support Strategy**
>
> **Tiered Support Structure:**
>
> **Tier 1 - Dealer/Service Center:**
> - Routine maintenance and common repairs
> - Diagnostic scan and code reading
> - **Requirements**: Basic training, diagnostic tools, common spare parts
>
> **Tier 2 - Regional Technical Center:**
> - Complex diagnostics and repairs
> - Specialized equipment (e.g., battery pack repair)
> - **Requirements**: Advanced training, specialized tools, expert technicians
>
> **Tier 3 - OEM Engineering:**
> - Novel issues, software bugs, design defects
> - Root cause analysis and engineering fixes
> - **Requirements**: Access to design data, simulation tools, engineering expertise
>
> **Support Channels:**
> - **Phone/email support**: Technical assistance hotline
> - **Remote diagnostics**: Over-the-air data collection and analysis
> - **Field service engineers**: Deploy to dealer for complex issues
> - **Training programs**: Regular updates to dealers on new technologies
>
> **C. Software and Update Strategy (Critical for Modern Vehicles)**
>
> **Over-the-Air (OTA) Updates:**
> - Capability to update vehicle software remotely
> - **Use cases**: Bug fixes, feature additions, performance improvements, security patches
> - **Requirements**: Secure update mechanism, rollback capability, customer notification
> - **Example**: Tesla pushes updates monthly, adding features and fixing bugs
>
> **Update Lifecycle:**
> - **How long will vehicles receive updates?** Define commitment (e.g., 8 years from production)
> - **What types of updates?** Security (mandatory), features (optional), performance
> - **Backward compatibility**: Ensure new software works on old hardware
>
> **Software Obsolescence:**
> - Older vehicles may not have hardware for new features
> - **Strategy**: Define 'end of support' date, communicate clearly to customers
> - **Example**: 10-year-old vehicle may not get latest autonomous features (sensor limitations)
>
> **D. Technology Refresh Planning**
>
> **Component Obsolescence:**
> - Electronics have short lifecycles (2-5 years) vs vehicle lifecycle (15+ years)
> - **Challenge**: Semiconductor, sensors, displays discontinued before vehicle end-of-life
> - **Strategies**:
>   - **Last-time buy**: Purchase lifetime supply before obsolescence
>   - **Redesign**: Substitute with newer equivalent component
>   - **Aftermarket**: Third-party suppliers for obsolete parts
>   - **Software emulation**: Use newer hardware with compatibility software
>
> **Proactive Obsolescence Management:**
> - Track component lifecycles from suppliers
> - Monitor obsolescence bulletins (component end-of-life notices)
> - Design for replaceability (modular, open interfaces)
> - **Tools**: Obsolescence tracking databases (IHS Markit, Z2Data)
>
> **Technology Insertion:**
> - Mid-cycle refreshes to keep product competitive
> - **Example**: Update infotainment system after 3-4 years to latest tech
> - **Requirements**: Design architecture for upgradability
>
> **Real example - Automotive Infotainment Obsolescence:**
> - 2015 vehicle with built-in navigation using Qualcomm chipset
> - 2020: Qualcomm discontinues chipset
> - Options:
>   1. Last-time buy (expensive, storage costs)
>   2. Redesign with new chip (engineering cost, re-certification)
>   3. End production (acceptable if nearing end-of-life)
>   4. Smartphone integration (Android Auto/CarPlay) - make built-in navigation optional
> - Many OEMs chose option 4 - strategic shift away from proprietary infotainment
>
> **Lifecycle Cost Impact:**
> - Service and support typically **2-3× the development cost**
> - Poor lifecycle planning → customer dissatisfaction, warranty costs, brand damage
> - **Best practice**: Lifecycle cost modeling during design phase (Session 13 topic)"

##### Slide 24: Lifecycle Management Plan Documentation
**Visual:** Lifecycle management plan template outline
**Instructor Script:**
> "Lifecycle management requires a formal plan - not ad-hoc reactions to problems.
>
> **Lifecycle Management Plan (LMP) - Standard Structure:**
>
> **1. Executive Summary**
> - System overview
> - Lifecycle strategy summary
> - Key metrics and targets
>
> **2. System Description**
> - What is being supported
> - Architecture and key subsystems
> - Interfaces and dependencies
>
> **3. Lifecycle Phases and Timelines**
> - Development, production, service, end-of-life phases
> - Expected durations and transition criteria
> - **Example**: Production phase: 2025-2033 (8 years), Service phase: 2025-2045 (20 years)
>
> **4. Maintenance Strategy**
> - Preventive, predictive, corrective maintenance approach
> - Service intervals and procedures
> - Maintainability requirements and design features
> - **Metrics**: Mean Time Between Failures (MTBF), Mean Time To Repair (MTTR)
>
> **5. Support Strategy**
> - Support tiers and escalation process
> - Training programs for service personnel
> - Technical documentation and knowledge management
> - Customer support channels (hotline, online, mobile app)
> - **Metrics**: First-time fix rate, customer satisfaction scores
>
> **6. Spare Parts Strategy**
> - Parts forecasting methodology
> - Stocking levels and locations (central vs regional vs dealer)
> - Obsolescence management approach
> - Service parts availability commitment (e.g., 15 years after end of production)
> - **Metrics**: Parts availability rate (target: >95%), inventory turns
>
> **7. Software and Updates Strategy**
> - OTA update capability and frequency
> - Software support lifecycle (how long will updates be provided?)
> - Cybersecurity patch process
> - Backward compatibility approach
> - **Metrics**: Update success rate, time to patch critical vulnerabilities
>
> **8. Technology Refresh Plan**
> - Component obsolescence monitoring process
> - Refresh triggers (obsolescence, competitive gap, customer feedback)
> - Budget and resources for mid-cycle updates
> - **Example**: Infotainment refresh every 4 years, battery chemistry upgrade every 6 years
>
> **9. End-of-Life Strategy**
> - Criteria for ending production
> - Service parts wind-down plan
> - Customer communication strategy
> - Recycling and disposal (environmental regulations)
> - **Example**: 'Production ends when sales <5000 units/year. Service parts available for 10 years after production end.'
>
> **10. Roles and Responsibilities**
> - Who manages each aspect of lifecycle?
> - Escalation paths for critical issues
> - Governance structure (Lifecycle Management Board)
>
> **11. Lifecycle Cost Model**
> - Development, production, service, and disposal costs
> - Revenue from service and spare parts
> - Total Cost of Ownership (TCO) for customer
> - **Linkage**: Connects to Session 13 (Lifecycle Cost Analysis)
>
> **12. Metrics and KPIs**
> - Reliability: MTBF, failure rates
> - Availability: System uptime, parts availability
> - Maintainability: MTTR, maintenance manhours
> - Supportability: Customer satisfaction, first-call resolution
> - Cost: Warranty cost per vehicle, service revenue
> - **Review cadence**: Monthly metrics review, quarterly business review
>
> **13. Risk Management**
> - Lifecycle risks (obsolescence, quality issues, supplier failure)
> - Mitigation strategies
> - Contingency plans
> - **Linkage**: Connects to Session 9 (Risk Management)
>
> **14. Continuous Improvement**
> - Field data collection and analysis
> - Lessons learned process
> - Service feedback to design teams (next-generation improvements)
>
> **Example Lifecycle Management Plan - Electric Vehicle Battery:**
>
> **System**: Lithium-ion battery pack (75 kWh, 400V)
>
> **Lifecycle phases:**
> - Production: 2024-2032 (8 years)
> - Service: 2024-2044 (20 years)
>
> **Maintenance strategy:**
> - Inspection every 2 years or 30,000 km
> - Battery health monitoring via BMS with predictive analytics
> - Coolant replacement every 4 years
>
> **Support strategy:**
> - Tier 1 (Dealer): Diagnostics, minor repairs
> - Tier 2 (Regional): Module replacement, thermal system repairs
> - Tier 3 (OEM): Pack design issues, software updates
>
> **Spare parts:**
> - Battery modules: Stocked regionally (90-day supply)
> - BMS ECU: Central stock (30-day supply)
> - Coolant, seals: Dealer stock
> - **Commitment**: Parts available through 2042 (10 years after production end)
>
> **Software updates:**
> - BMS software updates via OTA every 6 months
> - Critical safety/security patches within 30 days of discovery
> - Update support through 2034 (10 years from start of production)
>
> **Technology refresh:**
> - Battery chemistry upgrade in 2028 (lithium iron phosphate option for cost reduction)
> - BMS hardware refresh in 2030 (new microcontroller for enhanced features)
>
> **End-of-life:**
> - Production ends when next-gen battery launched (2032)
> - Recycling program established (recover lithium, cobalt, nickel)
> - Second-life program (used EV batteries for stationary storage)
>
> **Metrics:**
> - Target reliability: <1% battery failure in first 8 years/150,000 km
> - Warranty: 8 years/150,000 km (industry standard)
> - Customer satisfaction: >90% satisfaction with battery service
>
> **Lifecycle cost:**
> - Development: $200M (NRE)
> - Production unit cost: $8,000 per pack
> - Warranty reserve: $500 per vehicle
> - Service revenue: $50M over lifecycle (replacement modules, diagnostics)
>
> **Governance:**
> - Battery Lifecycle Management Board meets quarterly
> - Cross-functional: Engineering, Service, Quality, Finance
>
> This level of planning prevents surprises and ensures customer satisfaction throughout vehicle life."

---

### **CLIMAX: Integration and Strategic Thinking** (Slides 25-27, ~12 minutes)

#### Slide 25: Integrating Agreements and Infrastructure into Systems Engineering
**Visual:** System engineering V-model with agreements and infrastructure overlaid
**Instructor Script:**
> "Let's integrate everything we've learned into the systems engineering process.
>
> **Agreements and Infrastructure in the V-Model:**
>
> **Left Side (Development):**
>
> **Concept Phase:**
> - **Make vs Buy decisions**: Which components in-house vs supplier?
> - **Supplier engagement strategy**: Identify strategic partners for ESI
> - **Infrastructure planning begins**: What facilities, tools, equipment needed?
>
> **Requirements Phase:**
> - **Supplier requirements**: Flow-down requirements to suppliers
> - **Infrastructure requirements**: Define test equipment, manufacturing, IT needs
> - **Contract negotiation**: Align contracts with technical requirements
>
> **Design Phase:**
> - **Supplier collaboration**: ESI for co-development
> - **Interface specifications**: Define OEM-supplier boundaries
> - **Infrastructure procurement**: Long-lead items (test chambers, production lines)
>
> **Implementation Phase:**
> - **Supplier development**: Monitor supplier progress, support as needed
> - **Infrastructure deployment**: Install and commission equipment
> - **Contract management**: Track milestones, manage changes
>
> **Right Side (Verification and Validation):**
>
> **Integration:**
> - **Supplier deliveries**: Receive and inspect components
> - **Infrastructure validation**: Verify equipment ready for testing
>
> **Verification:**
> - **Use infrastructure**: Test equipment, HIL systems
> - **Supplier witnessing**: Invite suppliers to verification events
>
> **Validation:**
> - **Field testing**: Use service infrastructure (dealer diagnostics)
>
> **Production and Operations:**
> - **Supplier performance management**: Scorecards, business reviews
> - **Infrastructure operations**: Manufacturing lines, service networks
> - **Lifecycle management**: Execute LMP, manage obsolescence, updates
>
> **Key insight**: Agreements and infrastructure are NOT separate from technical work - they're ENABLERS of technical work. Integrate from day one.
>
> **Cross-functional Integration:**
>
> Systems engineering doesn't work in isolation. This session's topics require collaboration:
>
> | Activity | Systems Engineering Role | Collaborates With |
> |----------|-------------------------|-------------------|
> | Supplier selection | Define technical evaluation criteria | Procurement, Quality, Finance |
> | Make vs Buy | Technical feasibility and risk assessment | Strategy, Finance, Manufacturing |
> | Contract negotiation | Technical requirements verification | Legal, Procurement |
> | Infrastructure planning | Define technical requirements | Manufacturing, IT, Facilities |
> | Lifecycle management | Define support strategy | Service, Quality, Customer Support |
>
> **Systems engineer as integrator**: You ensure technical, business, and operational aspects align."

#### Slide 26: Real-World Example - Tesla Vertical Integration Strategy
**Visual:** Tesla's make vs buy decisions mapped
**Instructor Script:**
> "Let's analyze a real case study: Tesla's vertical integration strategy - bold make vs buy decisions.
>
> **Tesla's MAKE Decisions (High Vertical Integration):**
>
> **1. Battery Packs and BMS**
> - **Decision**: MAKE (design in-house, co-manufacture with Panasonic/LG)
> - **Rationale**:
>   - Core strategic differentiator (range, performance)
>   - Proprietary technology (cylindrical cells, structural pack)
>   - Cost control (batteries = 30% of vehicle cost)
> - **Infrastructure**: Gigafactories (Nevada, Texas, Berlin, Shanghai)
> - **Outcome**:
>   - Leading battery technology
>   - Cost advantage over competitors
>   - BUT: Massive capital investment ($5B+ per Gigafactory)
>
> **2. Electric Drive Units (Motors, Inverters)**
> - **Decision**: MAKE (in-house design and manufacturing)
> - **Rationale**:
>   - Performance differentiation
>   - Tight integration with battery and vehicle controls
>   - IP ownership
> - **Infrastructure**: Motor production lines at Fremont, Nevada
> - **Outcome**: Industry-leading efficiency, performance
>
> **3. Autonomous Driving Software and Hardware**
> - **Decision**: MAKE (Full Self-Driving software, FSD computer chip)
> - **Rationale**:
>   - Ultimate competitive differentiator
>   - No supplier had capability Tesla needed
>   - Recurring revenue model (FSD subscriptions)
> - **Infrastructure**: AI training supercomputers (Dojo), massive fleet data collection
> - **Outcome**: Leading autonomous capability, but still pending full autonomy
>
> **4. Supercharger Network**
> - **Decision**: MAKE (proprietary charging infrastructure)
> - **Rationale**:
>   - Enable long-distance EV travel (infrastructure didn't exist)
>   - Customer experience control
>   - Brand differentiation
> - **Infrastructure**: 50,000+ Superchargers globally
> - **Outcome**: Competitive moat, but now opening to other OEMs (new revenue stream)
>
> **Tesla's BUY Decisions (Still Rely on Suppliers):**
>
> **1. Semiconductors**
> - **Decision**: BUY (from suppliers like Infineon, NXP, AMD)
> - **Rationale**: Not core competency, massive capital to enter
> - **Partnership**: Close collaboration with AMD (infotainment), Nvidia (early autonomy)
> - **Challenge**: Affected by chip shortage, but recovered faster than traditional OEMs
>
> **2. Cameras and Sensors**
> - **Decision**: BUY (cameras from suppliers, no lidar - strategic choice)
> - **Rationale**: Sensor manufacturing not core, focus on software
>
> **3. Seats, HVAC, Interior**
> - **Decision**: BUY (though more vertical than traditional OEMs)
> - **Rationale**: Lower strategic value, cost-effective to outsource
>
> **Comparison to Traditional OEM (e.g., Ford, GM):**
>
> | Component | Tesla | Traditional OEM |
> |-----------|-------|-----------------|
> | Batteries | MAKE (strategic) | BUY (LG, CATL, Panasonic) - transitioning to MAKE |
> | Motors | MAKE | BUY (Bosch, ZF, BorgWarner) |
> | Software | MAKE (core) | Historically BUY, now transitioning to MAKE |
> | Infotainment | MAKE | BUY (suppliers) |
> | Body/Chassis | MAKE (Gigacasting) | MAKE (core competency) |
> | Final Assembly | MAKE | MAKE (core competency) |
>
> **Tesla vertical integration**: ~50% (much higher than industry average of 20-30%)
>
> **Tradeoffs of Tesla's Strategy:**
>
> **Advantages:**
> - Speed (no negotiations, aligned incentives)
> - Control (quality, IP, roadmap)
> - Cost (no supplier margins, economies at scale)
> - Innovation (rapid iteration, less complexity)
>
> **Disadvantages:**
> - Capital intensity (billions in infrastructure)
> - Risk concentration (if in-house fails, no fallback)
> - Capability requirements (must hire/build expertise)
> - Scalability challenges (stretched during ramp-ups)
>
> **Results:**
> - Tesla achieved industry-leading margins (25%+ vs 5-10% for traditional OEMs)
> - Faster innovation cycles (OTA updates, rapid design changes)
> - BUT: Production hell during Model 3 ramp (too much in-house, not enough expertise)
>
> **Traditional OEMs Responding:**
> - GM: Ultium battery platform (moving toward MAKE for batteries)
> - Ford: In-house software (Ford Blue Oval Embedded Software - MAKE decision)
> - VW: Cariad software unit (MAKE for software)
> - **Trend**: Strategic components (batteries, software) moving to MAKE
>
> **Lessons for systems engineers:**
> - Make vs Buy is strategic, CEO-level decision
> - Vertical integration is a spectrum, not binary
> - Infrastructure investment is enormous - assess ROI carefully
> - Beware of vertical integration for its own sake - align with core competencies
> - Hybrid approaches exist (co-develop, strategic partnerships)
>
> **No universal answer** - depends on company strategy, capabilities, market position."

#### Slide 27: Common Pitfalls and Best Practices
**Visual:** Checklist with warning signs and best practices
**Instructor Script:**
> "Let me share the most common mistakes in agreement and infrastructure management - and how to avoid them.
>
> **Pitfall #1: Single-Source Dependency (No Redundancy)**
> ❌ **Example**: Only one supplier for critical safety component
> - **Risk**: Supplier failure, natural disaster, bankruptcy → production halt
> - **2021 chip shortage**: Many OEMs had single-source chips
> - **Fix**: Dual-source strategy for critical components (70/30 split), backup suppliers qualified
>
> **Pitfall #2: Choosing Based on Cost Alone**
> ❌ **Example**: Selecting cheapest supplier without quality/capability assessment
> - **Risk**: Poor quality, delivery failures, hidden costs
> - **Real case**: OEM saved $5/unit by switching suppliers, spent $50M on recalls
> - **Fix**: Total Cost of Ownership (TCO) analysis, weighted scoring matrix
>
> **Pitfall #3: Late Infrastructure Planning**
> ❌ **Example**: Waiting until production phase to plan test equipment
> - **Result**: 12-month delay waiting for environmental chamber, missed launch date
> - **Fix**: Infrastructure requirements in concept phase, long-lead procurement
>
> **Pitfall #4: Vague Contracts ('Industry Standard Quality')**
> ❌ **Example**: Contract says 'supplier will deliver good quality'
> - **Result**: Disputes over what 'good' means, no enforceable standards
> - **Fix**: Quantified requirements (PPM <50, MTBF >100,000 hours), explicit standards (ISO 26262 ASIL-B)
>
> **Pitfall #5: No Change Control Process**
> ❌ **Example**: Informal emails to request changes, no impact assessment
> - **Result**: Scope creep, cost overruns, misaligned expectations
> - **Fix**: Formal ECO process, change control board, documented approvals
>
> **Pitfall #6: Ignoring IP Ownership**
> ❌ **Example**: Unclear who owns design IP developed by supplier
> - **Result**: Cannot change suppliers, locked in, supplier controls roadmap
> - **Real case**: OEM wanted to modify supplier's ECU software, discovered they had no license rights
> - **Fix**: Explicit IP clauses in contracts, escrow for critical designs
>
> **Pitfall #7: No Obsolescence Management**
> ❌ **Example**: Critical chip discontinued 5 years into 15-year vehicle lifecycle
> - **Result**: Emergency redesign ($5M+), production delay, or last-time buy (expensive inventory)
> - **Fix**: Proactive obsolescence monitoring, design for replaceability, long-term availability agreements
>
> **Pitfall #8: Under-Investing in Service Infrastructure**
> ❌ **Example**: Launch vehicle without adequate diagnostic tools for dealers
> - **Result**: High warranty costs (unnecessary part replacements), customer dissatisfaction
> - **Fix**: Service infrastructure as system requirement, dealer beta testing before launch
>
> **Pitfall #9: Treating Suppliers as Adversaries**
> ❌ **Mindset**: 'Beat suppliers down on price, never share information'
> - **Result**: Suppliers protect themselves with hidden margin, adversarial relationship, no innovation
> - **Better approach**: Strategic partnerships, transparent cost models, shared value creation
> - **Example**: Toyota treats suppliers as partners (joint kaizen, shared cost savings)
>
> **Pitfall #10: No Lifecycle Cost Modeling**
> ❌ **Example**: Optimizing for low development cost, ignoring service/support costs
> - **Result**: High warranty costs, customer complaints, brand damage
> - **Fix**: Lifecycle cost analysis (Session 13), design for serviceability
>
> **Best Practices Summary:**
>
> ✓ **Strategic Segmentation**: Not all suppliers are equal - tier your relationships
> ✓ **Early Supplier Involvement**: Co-develop complex components, leverage expertise
> ✓ **Systematic Selection**: Weighted criteria, cross-functional evaluation, due diligence
> ✓ **Clear Contracts**: Quantified requirements, explicit IP terms, change control
> ✓ **Make vs Buy Analysis**: Structured decision framework, not gut feel
> ✓ **Dual-Source Critical Components**: Mitigate supply chain risk
> ✓ **Infrastructure as Requirements**: Specify, budget, procure early
> ✓ **Active Contract Management**: Scorecards, reviews, escalation processes
> ✓ **Lifecycle Planning**: Maintenance, support, obsolescence from day one
> ✓ **Partner Mindset**: Win-win relationships with strategic suppliers
>
> **Remember**: Agreement and infrastructure management is SYSTEMS ENGINEERING, not just procurement. You're engineering relationships and ecosystem, not just buying parts."

---

### **RESOLUTION: Consolidation and Practice** (Slides 28-30, ~8 minutes + Q&A)

#### Slide 28: Key Takeaways
**Visual:** Summary with visual metaphors
**Instructor Script:**
> "Let's consolidate what you've learned today:
>
> **1. Supplier Relationships are Strategic**
> - Tier suppliers by strategic importance (strategic partners vs transactional)
> - Engagement models: Black box, gray box, white box
> - Performance management through scorecards and reviews
> - Early Supplier Involvement (ESI) for complex components
>
> **2. Contracts Enable and Protect**
> - Choose contract type based on risk and certainty (FFP, cost-plus, T&M)
> - Essential clauses: Technical specs, IP ownership, change control, quality, warranty
> - Active contract management: SPI/CPI tracking, milestone reviews
>
> **3. Vendor Selection is Systematic**
> - Structured process: RFI → RFQ → Evaluation → Negotiation → Award
> - Weighted multi-criteria scoring (technical, quality, cost, delivery, business)
> - Due diligence: Site visits, reference checks, financial health, risk assessment
>
> **4. Make vs Buy is Strategic Decision**
> - Framework: Strategic importance, capability, cost, risk, time-to-market
> - Not permanent - can transition over time (buy initially, make later)
> - Automotive-specific factors: Safety certification, recall liability, long lifecycle
>
> **5. Infrastructure Enables Lifecycle**
> - Development infrastructure: Tools, test equipment, IT systems
> - Manufacturing infrastructure: Production lines, quality control
> - Service infrastructure: Diagnostics, training, spare parts
> - Plan early (long lead times), specify as requirements
>
> **6. Lifecycle Management is Long-Term**
> - Phases: Development, production, service, end-of-life (25-30 years total)
> - Maintenance: Preventive, predictive, corrective
> - Support: Tiered structure, training, documentation
> - Technology refresh: Obsolescence management, software updates
>
> **The Big Picture**: Modern systems engineering is 70% about managing suppliers, contracts, and infrastructure. Technical brilliance is necessary but not sufficient. Master the organizational ecosystem."

#### Slide 29: Connection to Other Sessions and Systems Engineering Framework
**Visual:** Course roadmap highlighting Session 11's integration
**Instructor Script:**
> "Let's connect today's learning to our broader systems engineering journey:
>
> **Foundation from Earlier Sessions:**
>
> **Session 2 (SE Fundamentals)**: ISO/IEC 15288 includes Agreement and Enabling Processes
> - Today's content is from those process groups
> - Agreement Processes: Acquisition, supply
> - Enabling Processes: Infrastructure management, asset management
>
> **Session 4 (Requirements)**: Supplier requirements and infrastructure requirements
> - Flow-down to suppliers
> - Traceability across organizational boundaries
>
> **Session 5 (Architecture)**: Make vs buy decisions shape architecture
> - Interface definitions between OEM and supplier
> - Allocation of requirements to suppliers
>
> **Integration with Parallel Sessions:**
>
> **Session 9 (Project and Risk Management)**:
> - Supplier risks in risk register
> - Schedule dependencies on supplier deliveries
> - Infrastructure dependencies in project plan
>
> **Session 10 (Decision and Quality Management)**:
> - Make vs buy uses decision analysis frameworks (MCDA)
> - Supplier quality management (critical parameter management)
>
> **What Builds on Today:**
>
> **Session 12 (Safety and Security)**:
> - Safety requirements flow to suppliers (ISO 26262)
> - Cybersecurity in supplier components (ISO 21434)
> - Supplier audits for safety compliance
>
> **Session 13 (Lifecycle Cost and TCO)**:
> - Total Cost of Ownership includes supplier costs, infrastructure CAPEX/OPEX
> - Make vs buy cost modeling
> - Service and support cost analysis
>
> **Session 15 (Technical Management and Enabling Processes)**:
> - Configuration management across suppliers
> - Information management (data exchange with suppliers)
> - Infrastructure management processes
>
> **Systems Engineering as Integration Discipline:**
>
> Today's session highlights that systems engineers integrate:
> - **Technical**: Requirements, design, verification
> - **Organizational**: Suppliers, contracts, partnerships
> - **Operational**: Infrastructure, lifecycle support
>
> You're not just engineering a product - you're engineering an ECOSYSTEM that develops, produces, and supports that product for 25+ years.
>
> **Professional reality**: Senior systems engineers spend >50% of time on agreements and infrastructure. It's not 'overhead' - it's core SE."

#### Slide 30: Practice Exercise & Q&A
**Visual:** Exercise description
**Instructor Script:**
> "**Practical Exercise (Due before Session 12):**
>
> You are the systems engineer for a **Level 3 Autonomous Emergency Steering System** for highway use. The system will use cameras, radar, and lidar to detect obstacles and automatically steer to avoid collisions.
>
> **Part 1: Make vs Buy Analysis** (40%)
>
> Conduct make vs buy analysis for **three components**:
> 1. **Lidar sensor** (3D point cloud, 150m range, automotive-grade)
> 2. **Sensor fusion and decision algorithm software**
> 3. **Steering actuator** (electric motor for automated steering input)
>
> For EACH component, provide:
> - Evaluation against 6 criteria: Strategic importance, technical capability, cost, capacity, risk, time-to-market
> - Scoring (1-10 per criterion) with brief rationale
> - **MAKE or BUY decision with justification**
>
> **Part 2: Supplier Selection Plan** (35%)
>
> For the component(s) you decided to BUY:
> - Define evaluation criteria with weights (must include technical, quality, cost, delivery, business)
> - Outline selection process (RFI/RFQ/evaluation/award)
> - Identify 3-5 potential suppliers (real companies - research required)
> - List critical contract clauses needed (minimum 5)
>
> **Part 3: Infrastructure and Lifecycle Planning** (25%)
>
> Define infrastructure requirements for:
> - **Testing**: What test equipment needed? (e.g., HIL, vehicle-in-the-loop, proving ground)
> - **Service**: How will dealers diagnose and repair this system? What tools/training?
>
> Outline lifecycle management approach:
> - Maintenance strategy (how often inspected? What wear items?)
> - Software update strategy (how long will you support updates?)
> - Obsolescence risks and mitigation (sensors have 5-year lifecycle, vehicle is 15 years)
>
> **Deliverable Format:**
> - **Part 1**: Make vs buy decision matrix (1 page per component = 3 pages)
> - **Part 2**: Supplier selection plan (2 pages)
> - **Part 3**: Infrastructure and lifecycle plan (1-2 pages)
> - **Total**: 6-7 pages
>
> **Grading Criteria:**
> - Systematic use of decision frameworks (not gut feel)
> - Depth of analysis (rationale for scores/decisions)
> - Automotive realism (safety, regulations, cost)
> - Professional quality (industry-ready documentation)
>
> **Tips:**
> - Research real suppliers (Waymo for lidar, Mobileye for algorithms, ZF for actuators)
> - Consider ISO 26262 ASIL requirements (autonomous steering = ASIL-D, most stringent)
> - Think about the 2021 chip shortage - how does that affect your decisions?
> - Balance cost vs control vs time-to-market
>
> **Discussion Questions:**
> - Would your make vs buy decisions differ for a startup vs established OEM?
> - How does geopolitical risk (e.g., China-US tensions) affect supplier selection?
> - Should you single-source or dual-source lidar? Trade-offs?
> - What happens in 10 years when lidar technology has advanced - how do you handle obsolescence?
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional business aesthetic**: Clean, data-driven, enterprise-quality
- **Color coding**:
  - Blue for Supplier/Agreement topics
  - Green for Infrastructure topics
  - Orange for Lifecycle Management
  - Purple for Make vs Buy decisions
  - Red for pitfalls and risks
- **Use real industry examples**: Photos of supplier facilities, contract excerpts (anonymized), actual tools
- **Diagrams**: Supply chain networks, decision matrices, lifecycle timelines

### Key Slides to Emphasize:
1. **Slide 3** (Why This Matters - Automotive Statistics) - Industry reality
2. **Slide 4** (Chip Shortage Case Study) - Recent crisis everyone remembers
3. **Slide 9** (Collaboration Models) - Black/gray/white box framework
4. **Slide 16** (Vendor Evaluation Scoring) - Practical tool students will use
5. **Slide 18-19** (Make vs Buy Framework and Example) - Strategic decision-making
6. **Slide 26** (Tesla Case Study) - Real-world application
7. **Slide 27** (Pitfalls and Best Practices) - Students will reference this
8. **Slide 28** (Summary) - Students will photograph this

### Animations:
- **Slide 7**: Build supplier ecosystem diagram layer by layer
- **Slide 9**: Transition between black/gray/white box models with sliding graphics
- **Slide 16**: Animated scoring matrix filling in row by row
- **Slide 19**: Make vs buy decision matrix with weighted scores calculating live
- **Slide 23**: Lifecycle timeline with phases expanding to show detail

### Tables and Templates:
- **Slide 10**: Supplier scorecard with real metrics
- **Slide 12**: Contract types comparison table
- **Slide 16**: Full vendor evaluation matrix (3 suppliers compared)
- **Slide 19**: Make vs buy decision matrix with scoring
- **Slide 24**: Lifecycle Management Plan outline

### Real Examples to Include:
- Use actual automotive supplier names (Bosch, Continental, Denso, ZF, etc.)
- Reference real contracts clauses (anonymized but authentic)
- Show actual tools (DOORS screenshots, SAP supplier management, etc.)
- Include real case studies (chip shortage, Tesla vertical integration, Toyota supplier partnerships)

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Business + technical integration**: Show how agreements/infrastructure enable technical success
- **Real crisis examples**: Chip shortage, supplier bankruptcies - recent, memorable
- **Decision frameworks**: Emphasize systematic vs gut-feel approaches
- **Balance theory and practice**: Every framework illustrated with automotive example
- **Strategic thinking**: Elevate from tactical (contracts) to strategic (ecosystem design)

### Common Student Challenges:

**Challenge 1: "Why do engineers need to know about contracts and business?"**
**How to address:** Slide 3 statistics - 70% of vehicle is suppliers. Show Slide 4 - chip shortage was business/contract issue that halted production. Engineers must understand business context or technical brilliance is wasted. Reference Toyota unintended acceleration (Session 4) - supplier management failure, not just technical.

**Challenge 2: "Make vs buy seems simple - just compare costs"**
**How to address:** Slide 18-19 - show multi-criteria framework. Emphasize strategic, risk, capability factors. Use Tesla example (Slide 26) - they chose MAKE for batteries despite higher cost because strategic. Cost is ONE factor, not the only factor.

**Challenge 3: "Isn't this just procurement's job?"**
**How to address:** Distinguish roles: Procurement executes, but SYSTEMS ENGINEERS define technical requirements, evaluation criteria, make vs buy rationale. Show Slide 13 - technical clauses that engineers must verify. Procurement can't evaluate technical capability without SE input.

**Challenge 4: "How can we plan infrastructure 5 years in advance?"**
**How to address:** Acknowledge uncertainty, but emphasize long lead times (Slide 21 - test equipment takes 12-18 months). Planning ≠ perfect prediction. Use iterative approach: Rough planning early, refine as uncertainty reduces. Modularity and flexibility in infrastructure design.

**Challenge 5: "Tesla succeeds with high vertical integration. Should everyone do that?"**
**How to address:** Slide 26 trade-offs. Tesla's model works for them (high capital, tech company culture, investor patience). Traditional OEMs have different strengths (brand, dealer networks, manufacturing scale). No universal answer - align with company strategy and capabilities.

### Timing Flexibility:

**If running short:**
- Condense Slide 12 (Contract Types) - focus on FFP and cost-plus only
- Reduce Slide 21 (Infrastructure categories) to high-level overview
- Move some best practices from Slide 27 to backup slides

**If running long:**
- Extend Slide 26 (Tesla case) with more details on Gigafactory strategy
- Add interactive exercise: Give students a component, do quick make vs buy vote, discuss
- Show live demo of supplier scorecard tool or contract management system

**Core content (must cover - non-negotiable):**
- Slides 8-11 (Supplier engagement and collaboration)
- Slides 15-17 (Vendor selection process and criteria)
- Slides 18-20 (Make vs buy framework and examples)
- Slides 23-24 (Lifecycle management)
- Slide 26 (Tesla case study)
- Slide 27 (Pitfalls and best practices)
- Slide 28 (Summary)

### Engagement Points:

**Slide 4**: Ask class: "How many of you were affected by the chip shortage? Couldn't buy a car, or paid over MSRP?" (Personal connection)

**Slide 18**: Interactive - show a component (e.g., infotainment system), quick poll: "Make or Buy? Why?" Discuss different perspectives.

**Slide 19**: Work through scoring together - call on students to score each criterion, discuss reasoning.

**Slide 26**: "Tesla fans in the class? Critics? Let's debate vertical integration strategy." (Engagement through friendly debate)

**Slide 27**: Ask: "What's the worst supplier horror story you've heard?" Relate to pitfalls.

### Interactive Elements:

**Quick Poll (Slide 3)**: "Guess: What % of a typical vehicle is made in-house by the OEM?" (Answers usually way too high - reveals misconception)

**Case Discussion (Slide 4)**: "If you were an automotive OEM in 2020, what would you have done differently to avoid chip shortage impact?"

**Decision Exercise (Slide 19)**: Break into small groups, each group takes one make vs buy criterion, scores it, presents reasoning.

**Debate (Slide 26)**: Pro-vertical integration vs pro-outsourcing - students take sides, defend with evidence.

### Materials to Prepare:

**Before class:**
- [ ] Real supplier scorecard example (anonymized from industry if possible)
- [ ] Sample contract clauses (extract from public sources or templates)
- [ ] Make vs buy decision template (Excel)
- [ ] Chip shortage timeline and data (2021-2023)
- [ ] Tesla vs traditional OEM comparison data
- [ ] Exercise assignment handout with rubric

**Handouts:**
- [ ] Supplier evaluation criteria template
- [ ] Make vs buy decision matrix template
- [ ] Lifecycle management plan outline
- [ ] Contract checklist for systems engineers
- [ ] Infrastructure requirements template

**Post-class:**
- [ ] Share slides
- [ ] Post exercise assignment with due date
- [ ] Post templates (vendor evaluation, make vs buy, LMP)
- [ ] Post links to: ISO/IEC 15288 (Agreement and Enabling Processes), INCOSE Systems Engineering Handbook (Chapters on acquisition and supply)
- [ ] Create discussion forum: "Share examples of make vs buy decisions you've seen - what worked, what didn't?"

### Assessment Opportunities:

**During lecture:**
- Quick quiz (Slide 12): "Which contract type for uncertain scope: FFP or Cost-Plus?"
- Quick quiz (Slide 18): "Name three factors in make vs buy decision besides cost"

**Exercise assessment criteria:**
- Systematic use of decision frameworks (weighted scoring, criteria-based)
- Depth of analysis (not superficial - real research on suppliers)
- Automotive realism (considers safety, regulations, recall liability)
- Professional quality (could this be presented to management?)

**Common student mistakes to watch for:**
- Choosing make vs buy based on single criterion (usually cost)
- Generic supplier evaluation (not automotive-specific)
- Forgetting lifecycle phase (focus only on development/production, ignore 20-year service)
- No risk consideration (assuming everything goes perfectly)
- Unrealistic (trying to make everything in-house, or outsourcing critical strategic items)

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Develop supplier engagement strategies aligned with strategic importance
- ✓ Apply systematic vendor selection processes with weighted evaluation criteria
- ✓ Conduct make vs buy analysis using multi-criteria decision frameworks
- ✓ Specify infrastructure requirements for development, production, and service
- ✓ Create lifecycle management plans including maintenance, support, and obsolescence strategies
- ✓ Recognize that agreements and infrastructure are enabling elements of systems engineering

**Critical outcome:** Students understand that **systems engineering extends beyond technical design** to include strategic supplier relationships, infrastructure planning, and lifecycle management. They can apply structured decision frameworks to make vs buy and vendor selection decisions.

**Evidence of success:**
- Student can articulate criteria for make vs buy decision for a given component
- Student can develop weighted vendor evaluation matrix and justify scoring
- Student understands trade-offs of vertical integration (Tesla model vs traditional)
- Student can specify infrastructure requirements systematically
- Student recognizes lifecycle extends 25+ years beyond production

---

## 📚 Additional Resources for Students

**Standards and Guidelines:**
- ISO/IEC/IEEE 15288:2015: Systems and Software Engineering - System Life Cycle Processes (Section 4.2 Agreement Processes, Section 4.4 Enabling Processes)
- INCOSE Systems Engineering Handbook, Chapter 5: Agreement Processes
- ISO 10007:2017: Quality Management - Guidelines for Configuration Management
- ISO 55000:2014: Asset Management

**Automotive-Specific:**
- IATF 16949:2016: Automotive Quality Management System Standard
- VDA 6.3: Process Audit (German automotive industry supplier audit standard)
- AIAG PPAP Manual: Production Part Approval Process (supplier qualification)
- SAE J1739: Potential Failure Mode and Effects Analysis (FMEA) - supplier risk assessment

**Make vs Buy and Strategic Sourcing:**
- "Strategic Sourcing and Category Management" by Magnus Karlsson
- "Make or Buy: The Choice Between In-House Production and External Sourcing" (Harvard Business Review articles)
- "The Outsourcing Handbook: How to Implement a Successful Outsourcing Process" by Mark J. Power et al.

**Contract Management:**
- "A Guide to the Project Management Body of Knowledge (PMBOK)" - Chapter on Procurement Management
- "Contract Management Body of Knowledge (CMBOK)" by NCMA
- "Getting to Yes: Negotiating Agreement Without Giving In" by Fisher & Ury

**Infrastructure and Lifecycle:**
- "Total Productive Maintenance" by Seiichi Nakajima
- "Asset Management Excellence: Optimizing Equipment Life-Cycle Decisions" by John D. Campbell
- "Software Obsolescence in Defence Systems" by Peter Sandborn

**Online Resources:**
- Automotive Industry Action Group (AIAG): Supplier quality and PPAP resources
- Supply Chain Dive: News and analysis on automotive supply chain
- McKinsey Automotive & Assembly insights: Strategic sourcing articles

---

## 🔗 Connections to Other Sessions

**Builds on:**
- **Session 2**: ISO/IEC 15288 Agreement and Enabling Processes (theoretical foundation)
- **Session 4**: Requirements flow to suppliers, infrastructure requirements
- **Session 5**: Architecture decisions inform make vs buy
- **Session 9**: Supplier risks in project risk management
- **Session 10**: Decision analysis frameworks (MCDA for vendor selection, make vs buy)

**Leads to:**
- **Session 12**: Safety requirements in supplier contracts (ISO 26262), cybersecurity in supply chain (ISO 21434)
- **Session 13**: Total cost of ownership includes supplier costs, infrastructure CAPEX/OPEX, lifecycle costs
- **Session 15**: Configuration management across supply chain, infrastructure management processes
- **Session 16**: Future trends (digital supply chains, AI in supplier management, blockchain for traceability)

**Key concept thread:**
- **Session 2**: WHAT is systems engineering? (Process framework)
- **Session 9**: HOW do we manage projects? (Project management)
- **Session 10**: HOW do we make decisions and ensure quality? (Decision and quality)
- **Session 11**: HOW do we manage suppliers and infrastructure? (Organizational ecosystem) ← **TODAY**
- **Session 13**: What are the lifecycle costs? (Economic analysis)

**Recurring themes:**
- **Traceability**: Requirements traced to supplier deliverables
- **Risk management**: Supplier and infrastructure risks
- **Lifecycle thinking**: 25-30 year perspective
- **Standards**: ISO 26262, ASPICE flow to suppliers via contracts

---

## 🎬 Opening and Closing Strategies

### **Opening (First 2 minutes):**
Start with image of empty car factory (chip shortage) on screen as students enter. Begin:

> "Look at this image. This is a brand-new automotive factory sitting EMPTY in 2021. Not because of technical failure. Not because of poor design. But because tiny silicon chips - each costing $5 - were unavailable.
>
> The global automotive industry lost $210 billion. Millions of vehicles unbuilt. All because of supplier and infrastructure management failures.
>
> Today, we learn how to engineer the organizational ecosystem - suppliers, contracts, infrastructure - that enables complex systems. Because brilliant technical design is worthless if you can't source components or support the product.
>
> Welcome to Session 11: Agreement and Infrastructure Management - the 'other half' of systems engineering."

### **Closing (Last 2 minutes):**
Return to the opening image:

> "We started with empty factories - the cost of ignoring what we learned today. You now have the frameworks to prevent this:
>
> - You can segment suppliers strategically and engage them effectively
> - You can make systematic make vs buy decisions, not gut feel
> - You can select vendors using rigorous, weighted criteria
> - You can plan infrastructure requirements proactively
> - You can manage systems across 25-30 year lifecycles
>
> Remember: Modern vehicles are 70% supplier content. You're not engineering a car - you're engineering a supply chain and infrastructure ecosystem that develops, produces, and supports a car for decades.
>
> The exercise challenges you to apply these frameworks to autonomous driving systems. Approach it like a real program - research suppliers, analyze trade-offs, plan for the long term.
>
> Next session: We tackle Safety and Security - and you'll see how today's supplier agreements and infrastructure enable (or undermine) safety.
>
> See you in Session 12."

---

## 📈 Learning Objectives Mapping to Assessment

| Session Objective | Assessment Method | Success Criteria |
|-------------------|-------------------|------------------|
| Understand supplier engagement strategies | Exercise Part 2 | Identifies strategic vs transactional suppliers; appropriate engagement for each |
| Apply vendor selection criteria | Exercise Part 2 | Develops weighted evaluation matrix; systematically scores suppliers |
| Conduct make vs buy analysis | Exercise Part 1 | Uses multi-criteria framework; justifies decisions with data/reasoning |
| Define infrastructure requirements | Exercise Part 3 | Specifies test equipment, service tools with clear requirements |
| Develop lifecycle management plans | Exercise Part 3 | Addresses maintenance, updates, obsolescence with realistic timelines |
| Recognize organizational aspects of SE | In-class discussion + exercise | Integrates business, technical, and operational considerations |

---

**End of Session 11 Framework**
**Next:** Session 12 (Specialty Engineering: Safety & Security)
