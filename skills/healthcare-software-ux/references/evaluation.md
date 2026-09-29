# Healthcare review and verification

Use this reference for a requested audit, a meaningful workflow change, or a study plan. Scale coverage to the agreed surface and consequences. Do not turn a narrow copy edit into an unsolicited whole-product audit.

## Build an evidence trail

Identify the intended user and task, inspect the end-to-end flow, and trace each plausible error to a consequence. A finding needs an observed trigger or a clearly labeled hypothesis.

Use a compact record when useful:

`Location → user/task → trigger → observed behavior → possible consequence → proposed change → verification → unresolved owner/dependency`

Prioritize serious possible harm even if exposure is rare. Also consider encounter frequency, how quickly the error can be detected/corrected, and whether defaults or shared components spread it across people. Describe the actual failure mechanism; do not assign medical severity without adequate context.

Distinguish:

- **Observed defect:** reproduced in the interface/code with a stated condition.
- **Design hypothesis:** plausible risk needing user/domain evaluation.
- **Requirement:** tied to an applicable standard, policy, contract or law, with its scope established.
- **Evidence gap:** relevant behavior could not be inspected, measured or verified.

The [FDA human-factors guidance](https://www.fda.gov/media/80481/download) links intended users, environments, critical tasks and use-related risk for medical devices. It is nonbinding guidance except where it cites applicable requirements; using this review format does not satisfy a device submission or quality-system process.

## Choose scenarios that expose the changed risk

| Flow dependency | Useful scenario | Observable outcome |
|---|---|---|
| Patient/context | Switch records with a draft or stale tab open | Data, heading and action target stay associated; no silent carryover |
| Data interpretation | Missing, stale, contradictory, changed-unit or delayed measurement | User can identify state, unit, source and relevant time |
| Selection | Similar names, long labels, keyboard selection, filtered catalog | Correct item remains distinguishable and legitimate choices reachable |
| Submission | Slow response, disconnect, repeat click, timeout after server commit | Unknown outcome is reconciled; no unreported duplication |
| Recovery | Session expiry, interruption, rejected save, concurrent edit | Work is preserved appropriately; conflict and next step are explicit |
| Alerts/results | Repeated alert, changed evidence, absent recipient, handoff | Priority, ownership, delivery and acknowledgement have truthful states |
| Patient/proxy | Explain instructions or switch whom the user represents | Meaning, next action and access scope remain understandable |
| Accessibility | Keyboard, screen reader, zoom/reflow, limited dexterity | Task completes with usable labels, focus, controls and feedback |
| AI suggestion | Plausible wrong output, missing source, stale input | User can detect uncertainty, inspect evidence and correct/reject it |

Only run scenarios relevant to the product, with synthetic or appropriately authorized data. Do not carry out real clinical actions to test a prototype.

## Match methods to claims

Start with artifact/code inspection, walkthroughs and focused technical checks. For implementation, use the existing project test setup and leave the smallest meaningful regression check for nontrivial changed logic. Test what could fail, not whether text matches this checklist.

Use formative sessions to explore understanding and failure mechanisms with intended users. Cover distinct clinical/patient/caregiver roles, expertise, languages and access needs where they affect the task. Context includes lighting, noise, interruptions, physical placement and network availability when relevant. A fixed “five users” formula is not evidence that critical tasks are safe.

Measure correct task completion, consequential use errors, near misses, recovery and comprehension before comparing speed or clicks. Workload and perceived usability measures can supplement performance; satisfaction alone is not safety evidence. Define success, assistance, failure and timing boundaries in advance. Think-aloud can help exploration but may alter timing; use an appropriate study protocol for performance comparisons.

When comparing alternatives, control learning and order effects if they could alter the result. Record participant/task limitations; do not extrapolate a small simulation to patient outcomes.

For regulated device functions, the responsible human-factors/regulatory team must establish the applicable validation protocol, representative-user coverage, critical tasks, final-interface conditions and evidence. Do not describe an agent test or mock-user trial as formal validation. [NISTIR 7804](https://www.nist.gov/publications/nistir-7804-technical-evaluation-testing-and-validation-usability-electronic-health) provides an EHR evaluation protocol combining expert review with realistic tasks and representative users.

## Report scope honestly

For an audit, lead with actionable findings and evidence, then the significant untested areas. Do not claim a whole application was audited if only screenshots, one route or frontend code were available. A frontend review cannot verify backend permissions, clinical-rule correctness or delivery guarantees without evidence.

For a design or implementation, state what was produced/changed, what was verified, and what requires a clinical, accessibility, security, backend or regulatory owner. Keep proposed behavior separate from implemented behavior. Never label an application “safe,” “compliant,” “FDA approved,” or “production ready” based on this skill alone.

For a requested handoff, include only relevant dependencies:

- Data semantics: identity/encounter keys, unit/precision, source, event and update time, quality/freshness, reference interval source.
- State contract: drafts, commits, delivery, acknowledgement, errors, cancellation, conflicts, retry/idempotency and offline behavior.
- Access contract: actor/proxy identity, permissions, session expiry, retention, sharing/export rules and audit needs.
- Domain ownership: approved thresholds, terminology, alerts, clinical copy, follow-up and escalation, including what remains unresolved.
- Acceptance evidence: scenario, expected result, owner and whether tested, blocked or proposed.

After release, relevant product owners should review near misses, support reports, overrides, delayed tasks and workarounds. Prefer aggregate or minimized telemetry; do not add patient content to analytics to make monitoring convenient.
