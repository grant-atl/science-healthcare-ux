# Healthcare interaction patterns

Read only the sections relevant to the task. These are design starting points informed by the cited research, not universal clinical protocols. Confirm domain rules with the product's approved sources and intended users. For evidence classification and regulatory scope, see [sources.md](sources.md).

## Context, identity and interruption

- Keep enough patient identity and encounter context visible to distinguish the relevant record at ordering, signing, messaging and other consequential actions. Use the organization's approved identifiers; do not prescribe one universal banner or reveal unnecessary identifiers on every surface.
- Make a patient or proxy switch apparent and reconcile open forms, selected records, pending operations and cached data with the new context. Never leave an old patient's draft attached to a new patient's heading.
- On resuming interrupted work, expose what was completed, what remains, and whether the underlying data changed. Preserve secure drafts, position and comparison context where appropriate.
- Keep active filters, time range and encounter scope visible. A filtered absence of results must not look like no clinical history exists.
- A shared device needs clear active-user state and a workable handover/session-expiry path. Draft persistence must follow the approved security model; do not default to storing sensitive forms in browser local storage.

Patient identification and EHR continuity are recommended safety practices in the [ONC SAFER Guides](https://healthit.gov/clinical-quality-and-safety/safer-guides). Specific display and recovery mechanisms above are design inferences to test locally.

## Values, timelines and visual hierarchy

Display the information needed to interpret a value together: variable, value, unit, measurement time, source and quality/freshness. Separate measurement time from receipt/update time if delay matters; clarify timezone when workflows cross zones. Avoid ambiguous numeric dates.

- Preserve precision appropriate to the source and task; do not silently round consequential values or convert units without an approved, tested conversion.
- Treat reference intervals, decision thresholds and treatment targets as distinct concepts. Use source- and context-appropriate ranges supplied by the system; never synthesize universal normal values.
- Show missing, not yet measured, rejected, stale, disconnected, below-detection, estimated and zero distinctly when those states exist. Do not connect gaps in a trend as if measurements were observed.
- Use aligned times and comparable scales for comparison; reveal axis, aggregation, filtering and smoothing choices. Include exact values through keyboard-accessible inspection or an accessible table when appropriate.
- Put important exceptions where the task requires them. Equal-weight grids, many decorative cards, tiny metadata and saturation everywhere flatten priority.
- Keep related values, labels and actions visually together; separate clinically opposite actions. Use tabular numbers where comparison benefits, but never lose row/column or entity association.
- Preserve necessary information on small screens through deliberate prioritization, an accessible detail view or usable scrolling. Do not shrink consequential labels into unreadability.

## Ordering, reconciliation and committing work

Use structured selection when it preserves the domain meaning better than free text. Show enough distinguishing detail for similar names, formulations, strengths or procedures. Do not invent abbreviations or apply arbitrary capitalization to medication names.

For a medication-related interface, the approved order model may include medication, formulation/strength, dose, unit, route, frequency, duration and indication. Surface relevant context from validated sources; do not add unsupported interaction or dosing logic. Make complete consequential parameters reviewable before commitment.

For reconciliation, align the old and proposed records and make matched, added, changed, held and discontinued states explicit. Preserve source and effective time. Require a deliberate resolution of ambiguous matches rather than assuming similar strings represent the same item.

| Situation | Useful behavior | Misleading behavior |
|---|---|---|
| Routine reversible edit | Inline validation, clear save state, recovery | Confirmation on every keystroke |
| Consequential commitment | Summary of the actual object, parameters and consequence | Generic “Are you sure?” |
| Request timed out | Show unknown outcome; reconcile server status before retry | Assume failure and submit again |
| Queued offline | Distinct queued state and delivery/reconciliation behavior | “Order sent” before server acceptance |
| Concurrent update | Show conflict and relevant before/after information | Silently overwrite newer data |
| Signed/acted-on record | Approved amendment/correction workflow | UI “undo” implying care was reversed |

Ordering and clinical decision support need local implementation review, not just a component review. The [ONC CPOE guide](https://healthit.gov/wp-content/uploads/2025/06/SAFER-Guide-3.-CPOE-Final.pdf) is guidance for multidisciplinary design, implementation, use and monitoring.

## Alerts, results and handoffs

Do not equate every abnormal value with an interruptive alert. Determine the approved severity, urgency, responsible recipient and available action. Use inline information or queues for nonurgent work when appropriate; preserve escalation and acknowledgement for critical workflows.

- State the problem, why this patient/context matters, the source or rationale, and a useful action. Details can expand without hiding the essential warning.
- Distinguish seen, acknowledged, assigned, acted on and resolved. Dismissing a banner does not resolve its clinical cause.
- Represent conflicting alerts, stale evidence, repeated notifications and unreachable recipients explicitly. Propose deduplication/suppression rules for clinical review; do not silently alter a live alarm system.
- For test results and messages, show the status, responsible role, delivery state and follow-up path the system actually supports. Do not label a result reviewed because a page rendered.
- Review repeat-alert volume, appropriateness of overrides, missed events, delays and workarounds with clinical owners. A low override rate alone does not prove good decision support.

The [SAFER results and clinician communication guides](https://healthit.gov/clinical-quality-and-safety/safer-guides) support closed-loop communication practices; exact receipt, ownership and escalation states are product-specific design decisions.

## Patients, caregivers and copy

Patient-facing interfaces need their own language, comprehension checks and privacy model. Do not simply remove columns from a clinician dashboard.

- Lead with the person's task and concrete next step. Explain an unfamiliar clinical term on first use while preserving the underlying record's meaning.
- Separate what the result says, what is uncertain, and what approved follow-up is available. “Outside this laboratory's reference interval” must not become “You have [condition].”
- Avoid unsupported reassurance, alarming headlines, invented urgency, blame, and slogans. Use accurate state-specific copy such as “Your message is saved as a draft” only when true.
- For appointment, medication or preparation instructions, preserve dates, units, sequencing and clinically approved wording; verify translation and comprehension with the intended audience.
- Make proxy identity, scope and the person being acted for explicit. Do not assume a caregiver has full access, and do not merge a patient's preferences with a proxy's.
- Distinguish clinical consent, privacy authorization, research participation and optional product preferences. Use the mechanism approved for that purpose; do not force a universal consent checkbox.
- Show genuine optional choices fairly, with plain consequences and a change/withdrawal route where applicable. Preserve the supported version and decision state when required.

Plain-language and comprehension work is supported by [AHRQ's Health Literacy Toolkit](https://www.ahrq.gov/health-literacy/improve/precautions/quick.html). In patient testing, ask people to explain the next step in their own words; this adapts the [teach-back method](https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html) to evaluating the interface, not to grading the patient.

## Accessibility and real use environments

Use semantic controls, programmatic labels and errors, meaningful reading order, visible keyboard focus, accessible status messages and non-color state cues. Do not make hover, drag, hearing, precise movement or memory the only way to complete an essential action.

For web work, check the applicable [WCAG 2.2 criteria](https://www.w3.org/TR/WCAG22/), including their exceptions: normal-text contrast 4.5:1, large-text contrast 3:1, relevant non-text contrast 3:1, 200% text resizing, reflow, and minimum target size of 24×24 CSS pixels or a permitted alternative/exception. Keyboard focus must be visible and not entirely hidden by author-created content at AA. These checks are only part of conformance.

Support password managers and accessible authentication alternatives. Test zoom, screen readers, keyboard-only use, sticky headers, dialogs and interrupted sessions. Respect reduced motion; avoid decorative motion competing with real-time clinical changes. Enlarge controls beyond minimums when gloves, tremor, mobility, sight lines or stressful use conditions warrant it; test on the actual device and setting.

## AI-assisted interfaces

Label generated summaries, predictions and suggested actions according to their true status. Preserve the ability to inspect relevant source records and distinguish source evidence from model explanation. Show intended use, relevant input limitations, known failure conditions and review state; make uncertainty understandable without inventing confidence values.

Do not present a suggestion as a signed order, verified fact, diagnosis or completed task. Keep a usable correction/rejection path and evaluate whether the human can detect plausible errors. The [FDA/Health Canada/MHRA transparency principles](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/transparency-machine-learning-enabled-medical-devices-guiding-principles) are guidance for ML-enabled devices; applying similar visibility to other healthcare AI is a design inference, not a regulatory classification.
