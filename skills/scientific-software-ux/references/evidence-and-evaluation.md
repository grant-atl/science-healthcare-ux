# Evidence and evaluation

## How to use this evidence

This skill is an evidence-informed design synthesis. Sources support the specific statements below; they do not validate the skill or prove every proposed interface pattern improves outcomes. Distinguish a confirmed project/specification requirement, a research finding in its studied context, and a design inference that needs testing.

The workflow guidance combines scientific-software literature, public data standards, and interface practice. Biology-specific findings are bounded to their study context; applications to other disciplines are identified as design synthesis.

Sources below were checked on **2026-09-28**. Recheck changing standards, formats, implementations, and legal scope when they drive an actual decision. This is a targeted claim audit, not a systematic review of all scientific UX literature.

## Primary-source audit

| Source | What was supported | Limit and resulting treatment |
| --- | --- | --- |
| [Ramakrishnan & Gunter, 2017, *Ten Principles for Creating Usable Software for Science*](https://escholarship.org/uc/item/0w5547jv) | Experience from scientific data/workflow projects, including materials, environmental, climate, and biological sciences, supports continuous user involvement and attention to differing scientific roles | Experience-based principles, not a controlled proof of every interface pattern. Supports broad scientific scope and context discovery |
| [List, Ebert & Albrecht, 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005265) | Guidance on input checking, logging, defaults, data growth, and user feedback | An editorial focused on computational biology. Transfer to other disciplines is design synthesis, not evidence of universal effect size |
| [Loach, Smith & Bacon, 2026](https://academic.oup.com/bib/article/27/4/bbag396/8738527) | The review included 21 evaluation papers and descriptions of 55 WMSs, deriving 12 themes. Evaluations favored different interfaces for noncomputational users and developers; definitions/scoring were not comparable | Restricted to bioinformatics WMSs permitting sequencing analysis. Supports role-sensitive evaluation; neither a ranking of products nor proof all scientists need the same GUI |
| [Jäger et al., 2026, ELN implementation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0355558) | 55 completed responses, with subgroup analyses excluding 3 inexperienced respondents and using **n=52**. Tables 5/6 confirm 47/52 (90.38%) user-friendliness, 37/52 (71.15%) introductory courses, and 27/52 (51.92%) technical support. The 22-month rollout reached 237 registered users, 32 teams, and 4,263 active experiments | A chart title “n=55” would be misleading for those percentages; use question-specific denominators. Local observational case study, not a causal comparison or representative estimate for all scientific software. Core skill retains contextual onboarding guidance rather than percentages |
| [LIS heuristic case study, EMHJ 2020](https://applications.emro.who.int/emhj/v26/12/1020-3397-2020-2612-1456-1464-eng.pdf) | 162 identified problems; 73 (45.06%) rated major; flexibility/efficiency had the largest count | Counts describe one inspected system and method; they are not error rates, clinical harm rates, or prevalence across laboratories. No general numeric claim retained |
| [BIPM SI Brochure, 9th edition, 2026 update](https://www.bipm.org/en/publications/si-brochure) | Authoritative quantity/unit expression; temperature values and temperature differences have distinct conversion semantics | Does not define every discipline's admissible units or scientific validation bounds. Supports explicit units and format-aware conversion |
| [NIST TN 1297 §7](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty) | Measurement-uncertainty reporting distinguishes standard and expanded uncertainty, coverage factors, and the basis for probability interpretations | Older NIST guidance; page is flagged as no longer being updated. Used for that stable reporting distinction, not as a current universal policy or automatic “± means 95%” rule |
| [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) | Domain-independent entities, activities, responsible agents, and derivations | An interoperability model, not a reproduction guarantee; adopting its full serialization is optional |
| [Wilkinson et al., 2016, FAIR](https://www.nature.com/articles/sdata201618) | Identifiers, metadata, provenance, reuse conditions; authentication/authorization are permitted | Guiding principles rather than a mandated implementation or instruction to make sensitive data public |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Web accessibility criteria including keyboard access, focus, color, dragging alternatives, and target sizing | Apply the relevant criteria, levels, and exceptions. One widget checklist cannot establish whole-product conformance |
| [ASA statement, 2016](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf) | P-values do not measure hypothesis truth probability, effect size, or importance | Supports accurate labeling; does not select an analysis method or significance threshold |
| [FDA Part 11 scope guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application) | Applicability depends on particular electronic records/signatures and underlying predicate-rule obligations | U.S. guidance, not a universal lab-software requirement. A real deployment needs current rule and record-specific analysis; no compliance certification is offered |

## Evidence limits

- Vendor rankings and release-specific claims about Benchling, Galaxy, Geneious, SnapGene, and BaseSpace were not re-audited here. Interaction ideas are retained as design patterns without comparative-superiority claims.
- [BioChef's 2026 primary paper](https://link.springer.com/article/10.1186/s12859-026-06431-1) was located and its browser-based workflow/validation description checked. Detailed performance benchmarks and all browser/privacy claims were not independently reproduced. The skill prescribes measurement of the actual workload, not a universal browser/native speed claim.
- Specific clinical-genomics and blood-sample traceability effect claims, every historical cognitive/perception citation, and every product/format reference were not exhaustively traced. Those empirical effect claims and universal numeric design thresholds are not carried into the skill.
- Simulation, instrument, field, spatial, and AI patterns extend beyond the biology-specific studies. They are conditional design synthesis. Domain specialists must supply model assumptions, instrument constraints, safety procedures, coordinate contracts, and scientific acceptance criteria.
- No representative-user study, clinical validation, or controlled comparison of this skill has been performed. A source being real does not establish that its findings generalize to the user's product.

## Review and evaluation

Prioritize observed consequence, likelihood, and recoverability. Wrong-object actions, silent unit/reference changes, lost evidence, destructive retries, or false completion can affect scientific integrity even when the interface looks polished. Distinguish those from a blocked workflow or a lower-consequence discoverability issue. An unknown guarantee is “not verified,” not automatically a defect.

Choose a realistic scenario for the changed feature using synthetic or approved data:

| Scenario | Fault to include | Observable success |
| --- | --- | --- |
| Instrument acquisition | Delayed acknowledgment or stale reading | Requested and observed states remain distinct; consequential command is reconciled before retry |
| Measurement/import | Wrong unit, missing calibration, leading-zero ID, or unsupported format | Meaning preserved; unknown metadata exposed; unsafe interpretation avoided |
| Simulation/analysis | One changed default or mismatched reference; solver completes without required QC | Actual settings/versions recoverable; numerical completion distinct from scientific acceptance |
| Batch work | Partial failure plus an unknown outcome after disconnect | Acknowledged successes preserved, unknown outcomes reconciled, no duplicate effects |
| Reproduction | Find and reuse an old run with an unavailable dependency | Record recoverable without memory; limitations explicit; original result preserved |
| Sample/record | Similar ID or concurrent edit | Correct identity, conflict handling, and necessary prior history retained |
| Viewer | Filtering, downsampling, keyboard selection, and export | Units, context, focus, exclusions, and source evidence remain available |

Test real scale where it affects the interaction. For users, recruit by task, discipline, and domain/software expertise; don't assume one role represents all scientists. Record assistance rather than counting coached completion as independent success. Use appropriate baseline comparisons and measure correct completion, error detection, recovery, provenance completeness, understanding, and effort. Separate human active time from computation. A SUS score, click count, small convenience sample, or zero observed errors does not establish scientific safety or validity.

## AI and governance boundaries

Distinguish measured data, calculated results, retrieved evidence, generated suggestions, and human interpretations. Generated claims need inspectable sources and versions; do not invent citations or calibrated confidence. Preserve rejection/correction paths and the original observations. Consequential proposed changes must follow the product's actual authorization and review contract.

Use approved data/services and show meaningful input/data-destination context. A local-looking or browser-based interface does not prove that data stays private. Avoid sensitive details in telemetry, prompts, logs, URLs, and exports.

Do not infer Part 11, GxP, GDPR, HIPAA, or device obligations from “science,” “biology,” or a hospital affiliation alone. Determine intended use, data, jurisdiction, organization, record obligations, and accountable governance owner before making legal claims. Continue general integrity and accessibility work while scope is resolved. UI review cannot certify regulated infrastructure or establish that a scientific method is valid.
