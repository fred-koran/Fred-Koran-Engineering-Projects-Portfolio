# Fred's profile: everything a tailored resume may draw on

This is the memory for tailoring Fred's resume. **Only facts recorded here, in the
portfolio write-ups (`portfolio.py`), in `resume/index.html`, or in Fred's own
messages may appear on a resume.** If a job asks for something not covered here,
ask Fred; never fill the gap with a plausible guess.

When Fred tells you a new fact (a job, a date, a tool, his role on a team), add it
under "Learned from Fred" at the bottom, with the date, in the same session.

---

## Identity and contact

- Name: **Frederic Koran** (goes by Fred)
- Email: frederic13287@icloud.com (personal, listed first) · frederic.koran@mail.mcgill.ca
- Phone: 413-241-0775
- Locations: Longmeadow, MA (home) · Montreal, QC (school)
- Portfolio: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/
- Resume (master): https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/resume/

## Education

- **McGill University**, Montreal, QC · Expected May 2028
- B.Eng. in Bioengineering, Biomolecular & Cellular Engineering
- Minor in Economics · Fourth year of five · Major GPA 3.5/4.0
- Relevant coursework (as listed on the resume): Biomolecular Engineering & Protein Design ·
  Cell Culture Engineering & Bioprocess Scale-Up · Diagnostic Biodevice Design &
  High-Throughput Screening · Transport Phenomena & Mass Transfer · Biosignals & Control
  Theory · Molecular, Cellular & Tissue Biomechanics
- Course codes seen in the portfolio: BIEN 219 (structural case studies), BIEN 220 (group
  design project), BIEN 290 (lab modules: calibration, DOE, mechanical testing), BIEN 350
  (biosignals, MATLAB), BIEN 390 (lab modules: nanomaterials, microfluidic fabrication,
  lateral flow assays), WCOM 206 (written research proposal: P08), SEAD 510 (energy
  analysis: P14)

## Experience (wording is Fred's; keep it unless a job calls for re-ordering or trimming)

**Product Development Engineer** · Apr 2026 – Aug 2026
*Ruffian — TipTopSpin* · Student-run engineering startup
- Designed and prototyped TipTopSpin, a forearm-mounted wrist trainer that resists
  ulnar-to-radial deviation with a rod-stabilized compression spring, preloaded by a
  threaded knob and slider for a 10× adjustable resistance range.
- Developed mechanical concepts and CAD in Fusion 360, iterating geometry with a student
  engineering team to balance ergonomics, range of motion, and manufacturability.

**Founder and Operator** · Apr 2024 – Aug 2026
*Independent Landscaping Business*
- Founded a residential landscaping business and doubled profit from $5K in 2024 to $10K
  in 2025.
- Served ~20 residential clients and retained 7 as repeat clients every summer; managed
  customer acquisition, pricing, scheduling, equipment, and service delivery.

**Track and Field Assistant Coach** · Apr 2024 – Jun 2025
*Longmeadow High School*
- Personally coached three athletes to podium finishes at the conference championship,
  where the team placed first.
- Planned practices, provided event-specific instruction, and coordinated meet-day
  execution.

## Technical skills (as on the resume)

- **Computation:** MATLAB · Python · JMP (design of experiments) · AlphaFold · ImageJ
- **Engineering:** Fusion 360 (CAD, FEA) · LCD stereolithography · PDMS soft lithography
  and microfluidic device fabrication
- **Laboratory:** Mammalian cell culture (aseptic technique) · Molecular cloning · Protein
  extraction and purification · Western blotting · Immunofluorescence microscopy · HPLC ·
  GC–MS and LC–MS · UV-Vis and fluorescence spectroscopy

Also evidenced in the project write-ups (fine to name when a job asks for them):
UV-Vis absorbance and fluorescence calibration curves (Beer-Lambert) · cyclic voltammetry
(three-electrode cell) · contact angle goniometry · tensile and compression testing ·
analytical balance, micropipette and pH meter calibration · spectrophotometric loading
assays · ChemiDoc imaging · ELEGOO Mars LCD 3D printer · PDMS casting and Shrinky Dink
masters · lateral flow assay assembly · urea-formaldehyde microencapsulation (literature
design) · Welch / Butterworth / spectrogram / cross-correlation / coherence / transfer
function analysis in MATLAB · full factorial DOE and JMP prediction profiler · kinetic
model fitting (zero-order, first-order, Higuchi) · protein structure prediction and RMSD
analysis · Fusion 360 static FEA.

## Athletics

- Varsity Track and Field, McGill University · 2023 – Present
- Varsity Lacrosse, McGill University · 2025 – Present

---

## Project bank

Each project links to its full write-up. Read the full write-up
(`python3 .claude/skills/tailor-resume/portfolio.py N`) before writing bullets for it.
"Ready bullets" are factual starting points; trim or re-word them toward the job's
vocabulary without adding claims. "Don't claim" lists the ways each project is easy to
overstate.

Team projects: the portfolio does not say which part Fred did. Use plain action verbs
for the project's work, show the team size on the role line, and never write "led",
"managed" or "supervised" unless Fred confirms it.

### P01 · Sickle cell point-of-care device: channel geometry study
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p01
- When: Winter 2026 · Device design study · Four-person team
- Domain: diagnostics, microfluidics, point-of-care, medical device design, global health
- Methods/tools: 2×2 design matrix (serpentine vs spiral, square vs U cross-section);
  channels 3D-printed in 405 nm resin and sealed; BSA/PBS base fluid; *S. cerevisiae*
  culture as a cell-scale blood surrogate (OD600); flow and clog-point measurement
- Results: aggregation onset ranged 17%–64% of channel length across four devices
  differing only in shape; the literature-favoured spiral-U geometry clogged first (after
  20%), serpentine-square travelled ~3× further; geometry adds $0 per unit
- Ready bullets:
  - Designed and 3D-printed four microfluidic channel geometries for a sickle cell
    point-of-care device and tested them under matched conditions with a cell-scale
    blood surrogate.
  - Showed geometry alone shifted aggregation onset from 17% to 64% of channel length at
    no added unit cost; the literature-predicted best design clogged first.
- Don't claim: a validated device, statistics or replicates (single runs, pipette-loaded).

### P02 · Low-cost microfluidic fabrication: PDMS Shrinky Dink vs LCD stereolithography
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p02
- When: February 2026 · BIEN 390, Module 3
- Domain: microfabrication, microfluidics, soft lithography, 3D printing, surface wetting
- Methods/tools: shrunk-thermoplastic masters (shrink factor 0.45); PDMS 1:10 cast,
  degassed and cured; ELEGOO Mars LCD SLA printing from CAD; contact angle; flow rate from
  video in ImageJ
- Results: PDMS devices sealed without leaks or bubbles; 0.1 mm printed channel did not
  form (printable floor); 95.9° PDMS contact angle explained the lack of capillary flow;
  flow 0.33–8.3 mm/s under applied pressure; hypothesis reported as inconclusive
- Ready bullets:
  - Fabricated microfluidic channels by two low-cost routes (PDMS soft lithography on
    shrunk-thermoplastic masters and LCD stereolithography) and compared them under
    matched conditions.
  - Identified the process limits (a 0.1 mm printable floor and a 95.9° PDMS contact angle
    that prevented capillary filling) and set the pump, wettability and sizing
    requirements for the follow-on device study.
- Don't claim: mixing achieved, or a positive finding (it was reported as inconclusive).

### P03 · Lateral flow assays: commercial teardown and lab-built benchmark
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p03
- When: February–March 2026 · BIEN 390, Module 4
- Domain: in vitro diagnostics, immunoassays, rapid tests, reverse engineering
- Methods/tools: ran and dismantled 3 commercial LFAs (hCG urine, mononucleosis blood,
  Strep A swab); assembled a universal LFA from modular conjugation reagents; thermal
  contrast readout of gold-nanoparticle lines (green laser + IR camera)
- Results: commercial hCG cassette read positive at 8× dilution; lab-built strip gave 2 of
  2 false negatives with the control line present, isolating the failure to conjugation
  chemistry rather than flow
- Ready bullets:
  - Tore down and benchmarked three commercial lateral flow assays across urine, blood
    and swab matrices, comparing pad architecture and recognition chemistry.
  - Assembled a lateral flow assay from modular reagents; used control-line evidence to
    trace its false negatives to antibody conjugation rather than capillary flow.
- Don't claim: a working lab-built assay, or a detection limit for it.

### P04 · Functional nanomaterials: AgNP-diatom composites, protein adhesive, carbon nanodots
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p04
- When: January–February 2026 · BIEN 390, Modules 1 and 2
- Domain: nanomaterials, biomaterials, materials characterization, electrochemistry
- Methods/tools: citrate-reduction AgNP synthesis; hydrothermal carbon nanodots;
  silver-diatom biocomposite; egg albumin adhesive; UV-Vis (300–800 nm), fluorescence
  scans, stereoscopy, cyclic voltammetry (ferricyanide, Ag/AgCl), contact angle, tensile
  testing
- Results: 4 materials, 5 instruments; plasmon peak at 435 nm matched literature; nanodots
  emitted at 370 nm; albumin adhesive ~40× weaker than commercial glue on leather (0.237
  vs 9.8 MPa); Ag-modified electrode showed worse reversibility, traced to non-uniform
  deposition
- Ready bullets:
  - Synthesized four functional nanomaterials (silver nanoparticles, carbon nanodots, a
    silver-diatom composite and a protein adhesive) and characterized them on five
    instruments, including UV-Vis, fluorescence and cyclic voltammetry.
  - Traced an electrode result that contradicted the literature to non-uniform
    deposition, using bright-field imaging, rather than attributing it to the material.

### P05 · PDMS crosslinker ratio and mechanical tunability
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p05
- When: October–November 2025 · BIEN 290, Module 3
- Domain: mechanical testing, polymers, biomaterials, test method validation, QA mindset
- Methods/tools: PDMS at 20:1, 10:1, 5:1 cast and cured; tensile and compression testing;
  validation of the testing kit against 7 reference materials
- Results: the instrument deviated 2%–587% from literature moduli, so it was validated
  before any data were used; the PDMS trend inverted the hypothesis; recommended
  re-testing on a calibrated universal testing machine
- Ready bullets:
  - Cast PDMS at three crosslinker ratios and characterized it in tension and
    compression, validating the test apparatus against seven reference materials first.
  - Identified a 2–587% instrument deviation from literature values and withheld the
    dataset from design use pending re-test on a calibrated machine.
- Don't claim: a reliable PDMS modulus trend.

### P06 · Alginate bead release kinetics: full factorial DOE
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p06
- When: September–October 2025 · BIEN 290, Module 2
- Domain: drug delivery, encapsulation, formulation, design of experiments, process
  optimization, statistics
- Methods/tools: 2³ full factorial DOE (alginate %, Tween 80, extrusion geometry); four
  responses; JMP prediction profiler; ChemiDoc imaging + ImageJ circularity;
  spectrophotometric loading capacity; release study in PBS at 37 °C, 200 rpm; zero-order,
  first-order and Higuchi model fits
- Results: release time 480 s → 1080 s across the design space (2.25×); optimum confirmed
  at 92% mean circularity, inside the predicted interval; loading 23.9% and 23.1%;
  Higuchi (Fickian diffusion) fit R² = 0.968 and 0.949
- Ready bullets:
  - Optimized alginate bead encapsulation with a 2³ full factorial design in JMP, more
    than doubling release time (480 s to 1080 s); the confirmation run landed inside the
    predicted interval at 92% mean circularity.
  - Ran a 77-minute release study at 37 °C and identified Fickian diffusion (Higuchi model,
    R² = 0.968) as the release mechanism over zero- and first-order kinetics.

### P07 · Analytical instrument calibration and traceability
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p07
- When: September 2025 · BIEN 290, Module 1
- Domain: metrology, QA/QC, GLP, analytical chemistry, assay development
- Methods/tools: analytical and precision balances, 200 µL micropipette (gravimetric), pH
  meter (3-point); 10× PBS preparation; absorbance (Beer-Lambert) and fluorescence
  calibration curves
- Results: balance calibration R² = 0.9999; pipette <1% deviation on water and a
  quantified 3% overdelivery on 50% glycerol; PBS at pH 7.408 against 7.40; avoided the
  fluorescence inner-filter region to solve an unknown at 40.9 µM (R² = 0.9698)
- Ready bullets:
  - Calibrated balances, micropipettes and a pH meter against reference standards
    (balance R² = 0.9999) and quantified a 3% pipetting bias for viscous reagents.
  - Built absorbance and fluorescence calibration curves and solved unknown
    concentrations within the validated linear range, avoiding inner-filter error.

### P08 · Tipping the Needle: dissolving microneedle patch to replace daily injections (design proposal)
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p08
- When: September–October 2026 · WCOM 206 · Design proposal · **Sole-authored**
- Domain: drug delivery, transdermal delivery, medical device design, peptide therapeutics,
  osteoporosis, technical and scientific writing
- Methods/tools: literature-based design (written proposal plus a one-slide pitch); cone-geometry
  calculation of the drug left outside the skin at 80% insertion; tip-loaded two-layer dissolving
  needle concept; four evaluation criteria (delivered dose and consistency, needle fracture force
  against insertion force, application force within ~20 N, teriparatide stability)
- Results: proposed a 14 × 14 array (196 conical needles, 700 µm tall, 250 µm base, 600 µm
  centre spacing) with drug in the distal four-fifths of each needle; showed uniform loading leaves
  48.8% of each needle's volume above the skin at 80% insertion; ~0.1 N per needle at 20 N
- Ready bullets:
  - Proposed a tip-loaded dissolving microneedle patch to replace daily teriparatide injections
    for osteoporosis, specifying a 196-needle array (700 µm tall, 600 µm spacing) from published
    delivery data.
  - Showed by cone geometry that uniform loading leaves 48.8% of each needle's drug above the
    skin at 80% insertion, and set four evaluation criteria: delivered dose, strength margin,
    application force and drug stability.
- Don't claim: fabrication, testing or delivery data (it is a written proposal).

### P09 · In-situ substrate stiffness calibration for traction force microscopy
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p09
- When: April 2026 · Method development · Three-person team
- Domain: mechanobiology, biophysics, imaging methods, error analysis, inverse problems
- Methods/tools: critical review of a foundational TFM paper; proposed magnetic-bead
  in-situ modulus calibration; elastic-sphere and magnetic-force relations; Tikhonov
  regularization context; error propagation
- Results: the error budget reduces to ΔE/E = Δu/u, which bounds achievable modulus
  uncertainty at 1–10% and gives a design rule (larger induced displacement, lower error)
- Ready bullets:
  - Developed an in-situ method to calibrate hydrogel stiffness during traction force
    microscopy using magnetically actuated beads, replacing an assumed bulk modulus.
  - Derived an error analysis reducing modulus uncertainty to displacement uncertainty,
    bounding achievable error at 1–10% and setting the method's operating range.
- Don't claim: experimental validation (it is a method design and analysis).

### P10 · Reduced-alphabet redesign of a TIM barrel protein (20 → 5 amino acids)
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p10
- When: Fall 2025 · Computational protein design · **Sole-authored**
- Domain: protein engineering, computational biology, de novo design, structural biology
- Methods/tools: residue-by-residue redesign of a 247-residue TIM barrel at 15 and then 5
  amino acids; structure prediction against a wild-type baseline (~1 Å); RMSD and
  confidence analysis. The write-up says "structure prediction" without naming the tool;
  AlphaFold is on the skills list, but confirm with Fred before naming it here.
- Results: five-letter design changed 55% of the sequence, removed 75% of the alphabet,
  kept the barrel topology; core aligned to 1 Å with deviation confined to loops (3–5 Å)
- Ready bullets:
  - Redesigned a 247-residue TIM barrel enzyme with a reduced 5-amino-acid alphabet,
    changing 55% of the sequence while preserving the fold (core aligned to 1 Å by
    structure prediction).
  - Engineered salt-bridge pairs to substitute for proline's turn rigidity, and justified
    every substitution against burial, charge and catalytic constraints.
- Don't claim: expression, stability or activity data (designs are predicted, not tested).

### P11 · Bilayer magnesium-reinforced bioglass implant coating
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p11
- When: Fall 2024 · Biomaterials design study · Four-person team
- Domain: orthopedic implants, biomaterials, medical device design inputs/outputs,
  controlled release, cost analysis
- Methods/tools: specification against cortical bone (100–200 MPa, 15–25 GPa); survey and
  rejection of 6 reinforcement strategies; Mg-rod scaffold in bioglass/Mg-phosphate cement;
  mesoporous bioactive glass for pH-responsive antibiotic release; electrophoretic
  deposition route; materials costing
- Results: specified 180 MPa scaffold strength degrading to 100 MPa over 6 weeks (inside the
  cortical range as bone regrows); ~$278 materials vs an $8,000–13,000 implant
- Ready bullets:
  - Specified a bilayer magnesium-reinforced bioglass hip-implant coating to cortical bone
    requirements (180 MPa, degrading into the 100–200 MPa range over six weeks) from
    literature data.
  - Designed a mesoporous glass layer for pH-triggered antibiotic release and costed the
    materials at ~$278 against an $8,000–13,000 implant.
- Don't claim: fabrication or testing (it is a literature-supported specification).

### P12 · Bacterial self-healing concrete: FEA of cracked vs healed prism
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p12
- When: Fall 2024 · BIEN 220 group design project · Five-person team
- Domain: engineered living materials, microencapsulation, FEA, structural modelling
- Methods/tools: *B. subtilis* spore + urea/Ca(NO₃)₂ in pH-triggered urea-formaldehyde
  microcapsules (design from literature); Fusion 360 FEA of a 40×40×160 mm prism, cracked
  vs 80% healed, 1–5 kN loads in two directions; literature material properties
- Results: healed model displaced ~6× less per unit load; von Mises stress 1.7× lower;
  porous-microstructure model was attempted and failed, so solids were idealized
- Ready bullets:
  - Modelled cracked and healed self-healing concrete in Fusion 360 FEA under 1–5 kN loads
    in two directions; the healed prism displaced ~6× less per unit load with 1.7× lower
    von Mises stress.
  - Designed the healing mechanism around pH-triggered urea-formaldehyde microcapsules
    releasing *Bacillus subtilis* spores for calcium carbonate precipitation.
- Don't claim: lab-made concrete or measured healing (modelling and design from literature).

### P13 · Biosignal analysis: EEG and cerebral hemodynamics (MATLAB)
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p13
- When: date not stated in the portfolio (ask Fred) · BIEN 350 · Four-person team
- Domain: signal processing, neuroengineering, physiological modelling, data analysis
- Methods/tools: MATLAB; Welch vs periodogram; 5-band 2nd-order Butterworth filter bank
  with zero-phase filtering; spectrograms; beta/alpha vigilance index; cross-correlation
  connectivity (~1,700 pairs × 6 segments × 6 bands = 36 matrices); pressure–flow
  correlation, coherence and inverse-FFT transfer-function model
- Results: two-block broadband connectivity did not survive band decomposition (gamma
  sharpest front-back split, alpha hemispheric); pressure–flow correlation 0.968 with
  0.065 s lag; low-frequency decoupling consistent with autoregulation
- Ready bullets:
  - Analyzed resting-state EEG in MATLAB (Welch spectra, Butterworth filter bank,
    spectrograms) and computed 36 band-specific connectivity matrices, showing the
    broadband two-lobe structure does not survive band decomposition.
  - Modelled cerebral autoregulation with pressure-to-flow coherence and a
    transfer-function model (r = 0.968, 0.065 s lag) and identified where a linear model
    fails.

### P14 · Energy Footprint: seven-day personal energy and carbon audit, annualized
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p14
- When: September–October 2026 · SEAD 510 · Energy audit · **Sole-authored**
- Domain: energy analysis, sustainability, carbon accounting and GHG emissions, building energy
  modelling, embodied (life-cycle) energy, cost analysis
- Methods/tools: daily activity and appliance log (Sep 10–16, 2026); building heat modelled from
  utility bills (Hydro-Québec Rate D), heating degree days and heat loss coefficients; McGill
  building energy allocated per occupant-hour from the campus GHG inventory; emission factors
  (Canada National Inventory Report, ECCC, US EPA eGRID); embodied food energy (production plus
  transport); cost and human-labour equivalence
- Results: 273 kWh in the audit week (39.0 kWh/day); 22,700 kWh/yr annualized (62.2 kWh/day);
  3.76 t CO₂/yr, 69% from car trips and flights (45% of energy); Montreal residence 24% of energy
  but 0.3% of CO₂; beef ~15× the energy per food calorie of potatoes
- Ready bullets:
  - Audited a week of personal energy use across buildings, travel and appliances and annualized
    it to 22,700 kWh and 3.76 t CO₂, modelling building heat from utility bills, heating degree
    days and McGill's campus energy inventory.
  - Showed that grid carbon intensity, not energy use, drove emissions: the Montreal residence was
    24% of energy but 0.3% of CO₂, while car trips and flights were 45% of energy and 69% of CO₂.
- Don't claim: metered measurements (building and appliance energy are modelled from bills,
  ratings and inventories).

### P15 · Published chapter: "Unlocking Locust Survival: A Chemical Analysis of Locusts"
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p15 ·
  published at bioengineering.hyperbook.mcgill.ca/unlocking-locust-survival-a-chemical-analysis-of-locusts
- When: 2025 · Literature review · Co-authored, four authors (Koran, F., Leader, C.,
  Stoilova, A., & Weng, A.), McGill Bioengineering Hyperbook
- Domain: scientific writing, publications, molecular/chemical biology, endocrinology
- Ready bullets:
  - Co-authored a published review chapter in McGill's Bioengineering Hyperbook
    synthesizing the hormonal, neurochemical and pheromone control of locust phase change.
- Citation form for a Publications line: Koran, F., Leader, C., Stoilova, A., & Weng, A.
  (2025). Unlocking Locust Survival: A Chemical Analysis of Locusts. *Bioengineering
  Hyperbook*, McGill University.
- Don't claim: original experiments (it is a review).

### P16 · N370S glucocerebrosidase mutation and Gaucher disease (structural case study)
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p16
- When: date not stated (ask Fred) · BIEN 219
- Domain: structural biology, disease mechanism, enzyme therapy, biopharma
- Methods/tools: PDB structure comparison (1OGS wild type vs 3KE0 N370S)
- Results: mutation sits 13 Å from the catalytic centre on helix 7; deficiency explained as
  reduced activity × reduced lysosomal delivery; links to ERT and SRT mechanisms
- Ready bullets:
  - Compared wild-type and N370S glucocerebrosidase crystal structures (PDB 1OGS, 3KE0) to
    explain how a mutation 13 Å from the active site causes type 1 Gaucher disease.

### P17 · Insulin structural analysis (PDB 4INS)
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p17
- When: date not stated (ask Fred) · BIEN 219
- Domain: structural biology, protein therapeutics, diabetes
- Results: traced disulfide bridges, the hinge-like receptor binding surface (Phe-B24) and
  zinc hexamer storage to physiological function
- Ready bullets:
  - Analyzed the 1.5 Å insulin crystal structure (PDB 4INS), linking disulfide bonding,
    receptor-binding conformational change and zinc hexamer storage to function.

### P18 · Nanopore sequencing signal and sensing limits (analytical derivation)
- Link: https://fred-koran.github.io/Fred-Koran-Engineering-Projects-Portfolio/#p18
- When: date not stated (ask Fred) · Analytical derivation · Four-person team
- Domain: biosensors, sequencing, electrochemistry/biophysics, modelling
- Methods/tools: channel + access resistance model from pore geometry and electrolyte
  conductivity; blockade as a resistance ratio; Nernst and Goldman-Hodgkin-Katz
- Results: three physical limits (5–6 bases in the sensing window; translocation ratcheted
  to 1–100 nt/s; 1/f noise floor below 1–10 kHz) and their trade-offs
- Ready bullets:
  - Derived nanopore current-blockade signal from pore geometry and electrolyte physics
    and quantified three physical limits on sequencing: spatial resolution, translocation
    speed and noise floor.

---

## Which projects to reach for

| The job mentions… | Strongest evidence |
|---|---|
| medical devices, point-of-care, diagnostics, IVD | P01, P03, P02, P18, P11, P08 |
| microfluidics, microfabrication, soft lithography, 3D printing | P02, P01 (+ Fusion 360 / SLA skills) |
| mechanical design, CAD, prototyping, product development | Ruffian/TipTopSpin, P01, P12, P11 |
| FEA, mechanical testing, materials characterization | P12, P05, P04, P11 |
| biomaterials, implants, tissue engineering | P11, P06, P05, P04 |
| drug delivery, formulation, encapsulation | P08, P06, P11 (pH-triggered release) |
| DOE, statistics, JMP, process optimization | P06, P07 |
| QA/QC, calibration, metrology, GLP, test method validation | P07, P05 |
| analytical chemistry, spectroscopy, assay development | P07, P04, P03, P06 |
| protein engineering, computational biology, structural biology | P10, P16, P17 |
| signal processing, MATLAB, data analysis, neuro | P13, P09 |
| mechanobiology, biophysics, imaging, modelling | P09, P18, P13 |
| scientific writing, research, publications | P15, P08 (written proposal), P09 (critical review) |
| design controls, requirements, cost analysis | P11, P01 |
| sustainability, energy, carbon accounting, environmental | P14 |
| business, operations, customer-facing work | Landscaping business |
| leadership, coaching, teamwork | Assistant coach, team projects (3–5 people) |

## Not known yet (ask Fred when a job needs it)

- Work authorization (US and Canada) and whether sponsorship is needed
- Internship or co-op availability windows
- Overall GPA (only the major GPA, 3.5/4.0, is known)
- Fred's individual role on each team project
- Dates for P13, P16, P17 and P18
- The structure-prediction tool used in P10
- Ruffian details beyond the resume (team size, outcomes, testing)
- Languages, certifications, lab safety training, other software

## Fred's preferences

- One Letter page, built to be read by applicant-tracking systems (see SKILL.md rules).
- Keep the current design (black and white, matching Fred's own PDF of Oct 2026). Tailoring
  changes content, not styling.
- Dates as "Apr 2026 – Aug 2026"; years only where months are unknown.
- Don't change information: tailoring selects, orders and trims; new facts come from Fred.
- Fred reviews a preview, then usually says "merge" to publish.

## Learned from Fred

- 2026-10-11: Job months. Ruffian Apr 2026 – Aug 2026 (no longer current), landscaping
  Apr 2024 – Aug 2026, assistant coach Apr 2024 – Jun 2025.
- 2026-10-22: New master resume from Fred's PDF. Job titles lead each entry (Product
  Development Engineer at Ruffian; Founder and Operator; Track and Field Assistant Coach).
  New facts: landscaping profit doubled from $5K (2024) to $10K (2025), ~20 residential
  clients with 7 repeat every summer; coached three athletes to conference-championship
  podiums, team placed first. Header now lists only the iCloud email, phone, Longmeadow MA
  and https://fred-koran.github.io; degree line is "B.Eng. in Bioengineering".
- 2026-10-11: Two new portfolio projects, both September–October 2026 and sole-authored: the
  WCOM 206 microneedle patch proposal ("Tipping the Needle", P08) and the SEAD 510 energy
  footprint audit (P14). Adding them renumbered the portfolio: old P08–P12 are now P09–P13 and
  old P13–P16 are now P15–P18.
