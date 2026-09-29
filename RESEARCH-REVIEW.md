# Research review for the two skills

Checked September 28, 2026. This review identifies primary-source support, corrections, design inferences, and remaining evidence gaps. It is a targeted review, not a systematic review or a guarantee that every design choice is universally effective.

## Scope

| Area | Role in the package |
| --- | --- |
| Scientific workspaces | Research, laboratories, instruments, computation, simulation and visualization across disciplines. |
| Healthcare interfaces | Clinicians, patients, caregivers and care administration. |
| Executive public-health briefings | Optional healthcare reference, not the scope of either general skill. |
| CDC/USWDS integration | Optional reference for explicitly applicable agency/design-system work, not a default visual style. |

Evidence records link to public publications, specifications and official sources. Source findings, design proposals and unresolved questions are identified separately.

## Important corrections

**ELN survey denominator.** The 2026 study had 55 complete responses, but excluded three participants without prior electronic-notebook experience from the relevant analysis, leaving 52. Thus 90.38% corresponds to 47/52. A chart labeling those percentages simply “n=55” is misleading. Adoption findings from this sample do not predict adoption of all scientific software. [Original ELN study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0355558).

**Bioinformatics is one scientific domain.** The workflow-system scoping review examined 21 evaluation papers covering 55 systems and identified 12 themes. Its selection concerned sequencing-capable bioinformatics workflows. It supports domain-specific questions about usability and reproducibility, not a universal ranking of tools or proof for every scientific field. [Original review](https://academic.oup.com/bib/article/27/4/bbag396/8738527).

**Percentage points versus relative percent.** The ICU interface study reported accuracy of 98.70% versus 92.86%. That is **5.84 percentage points**, approximately **6.3% relative**, not a 6.3-percentage-point increase. The randomized crossover simulation involved 36 ICU nurses; it does not establish improved patient outcomes. [Study record](https://pubmed.ncbi.nlm.nih.gov/42486461/).

**Interface studies do not establish universal effects.** Twinlist, EHR implementation comparisons, alert tiering, and monitor positioning were recovered and qualified by study setting and outcome. Their reported time, click, error, workload, or intention effects are not promised benefits of these new skills. Details and retrieval limits are in the [healthcare evidence review](skills/healthcare-software-ux/references/sources.md).

**Cognitive findings are not layout quotas.** Working-memory, choice-reaction and pointing studies do not establish a universal number of cards, menu items, clicks, or seconds. The skills retain visible context, meaningful grouping and usable targets while requiring task-specific judgment.

**Scientific integrity needs actual recorded state.** A rerun control does not establish reproducibility. Inputs, transformations, units, parameters/defaults, versions, reference state and relevant instrument or simulation conditions must remain recoverable. The exact record depends on the domain; a biological coordinate convention is not a universal scientific data model. See the [scientific evidence review](skills/scientific-software-ux/references/evidence-and-evaluation.md).

**Requirements have scope.** HIPAA, GDPR, Part 11, device standards and federal accessibility obligations are not implied by a scientific or healthcare label. WCAG 2.2 AA is a design baseline here, not a universal legal determination. Catalogue abstracts do not support claims of full IEC clause review or conformity. Approved domain rules remain necessary for dose limits, thresholds, calibration decisions and clinical escalation.

**Decision-interface proposals remain proposals.** MONITOR / PREPARE / ACT NOW and a 60-second target are not official biological-threat standards. Model-run fractions need justified probability interpretations. The Decision Uncertainty Toolkit includes exceedance magnitude and duration as well as probability; it is not a rule to choose the smallest percentage. [Public-health evidence audit](research/decision-interface-audit.md).

**CDC/USWDS integration is conditional.** The proposed hierarchy of CDC branding and USWDS implementation is a proposed architecture, not an official joint certification scheme. Template generation, required assets, semantics, accessibility and component ownership need the actual project's evidence. A CDC-related typography page does not by itself establish an agency-wide web-platform requirement. [CDC/USWDS evidence audit](research/cdc-uswds-audit.md).

## What remains to validate

The skills contain research-informed instructions, not new empirical results. No representative-user study, clinical safety validation, scientific replication, complete accessibility audit, or regulatory determination was performed for these packages. Generalizing principles from biology to other sciences is an explicit design synthesis, supported where possible by cross-domain units/provenance standards and tested with synthetic nonbiological scenarios.

Use the [validation record](VALIDATION.md) for actual assistant checks and installation limits. To claim improved performance, evaluate the relevant workflow with representative users and data against a defined baseline, measuring correct completion and recovery alongside effort. Keep study findings distinct from the skill's own unmeasured effectiveness.
