---
name: healthcare-software-ux
license: MIT
description: "Design, implement, or review healthcare UI/UX for clinicians, patients, caregivers, and care teams: EHRs, portals, monitoring, ordering, and coordination. Not medical advice or certification."
---

# Healthcare Software UX

Help the intended person complete the correct care-related task, understand its outcome, and recover from mistakes. Prioritize clinical meaning and use safety over visual minimalism or fewer clicks. Scale the process to the requested change; a scheduling form does not automatically need the controls of an infusion device.

## Read what applies

- For screens, flows, components, visualizations, copy, or implementation: read the relevant sections of [patterns.md](references/patterns.md).
- For an audit, significant workflow change, or validation plan: read [evaluation.md](references/evaluation.md).
- For legal, regulatory, standard, research-evidence, or medical-device claims: read [sources.md](references/sources.md) and verify the current primary source and product scope before making the claim. That file records evidence and its limits.

- For explicitly requested executive or public-health briefings: read [public-health-briefs.md](references/public-health-briefs.md). This is optional, not the default clinical workflow.

- For explicitly required CDC/USWDS or federal design-system integration: read [government-design-systems.md](references/government-design-systems.md). Do not apply its branding to ordinary healthcare apps.

The references are self-contained; other skills and external research documents are not runtime dependencies.

For clinical genomics or another research-to-care interface, preserve scientific provenance and analysis semantics as well as patient-facing and clinical safety. Scientific integrity does not replace these care-workflow checks, and a research label alone does not settle regulatory scope.

## Establish the context

Inspect the actual brief, relevant screens or code, shared components, states, data contracts, and existing clinical policies before choosing a design. For code work, trace the affected flow through its data source and action outcome, including sibling callers.

Identify what materially changes the decision:

- Intended user: clinician, patient, caregiver/proxy, administrator, or several distinct roles; expertise, language and access needs.
- Task and consequence: what is being viewed, entered, ordered, communicated, signed, or acted on; what an error could cause.
- Environment: bedside, clinic, home, shared workstation, mobile, gloves, noise, interruptions, poor connectivity or time pressure where relevant.
- Data: identity/encounter, source, units, measurement time, update time, missingness, confidence/quality, and who can change it.
- Product scope: jurisdiction and intended use if known; prototype versus production; wellness, care administration, clinical support or regulated device function.

Use existing answers. State reasonable assumptions and proceed on independent work. Ask only when an unknown materially affects the solution; leave unverified clinical rules or access policies as explicit dependencies rather than inventing them.

## Work in the requested mode

**Design:** map the main task and its consequential failure states. Choose a layout that preserves necessary context; explain the important tradeoff and what needs representative-user testing. Produce the requested flow, prototype, or specification.

**Implement:** reuse established components, native controls, data semantics and project styling. Make the smallest complete change across the real flow. Keep validation at the relevant trust boundary; a disabled button is not authorization. Verify affected states and interactions using existing checks and focused manual testing.

**Review:** inspect the agreed surface without modifying it. Lead with consequential findings, each tied to an observed element or file, a failure scenario, a specific fix, and a way to verify it. Separate observed defects from hypotheses and unavailable evidence. Do not manufacture findings to fill a quota.

## Protect the important invariants

1. Keep the patient, encounter, clinical object, and active actor/proxy unambiguous at consequential actions. Re-check context after patient switches, interrupted work, and stale-tab returns.
2. Associate each value with its label, unit, time and source where needed for interpretation. Missing, zero, unavailable, stale, estimated and final are different states.
3. Preserve clinically relevant density and comparison context. Do not hide units, timestamps, exceptions, or important options just to simplify the screen.
4. Distinguish draft, saving, saved, queued, sent, accepted, signed, acknowledged and failed as the real system supports them. A local change or successful request is not proof that downstream care occurred.
5. Prevent unsafe ambiguity before adding warnings. Apply constraints and defaults from approved domain rules; make significant defaults visible and editable where appropriate. Never invent dose limits, diagnostic thresholds, treatments, alarm priorities or clinical escalation instructions.
6. Add friction in proportion to the potential harm and reversibility. A consequential confirmation identifies the object and consequence; routine actions should not train users to dismiss generic warnings.
7. Tier alerts by validated urgency, severity and actionability. Preserve their rationale and response options. Do not silence, suppress, or change clinical rules merely to reduce visual noise.
8. Preserve work through interruption and recovery using approved secure storage. Resolve conflicts and ambiguous submissions explicitly; do not silently duplicate an order or imply software undo reverses real-world treatment.
9. Support keyboard, focus, assistive technology, non-color cues, readable content and responsive use. Prefer WCAG 2.2 AA as a web design baseline while checking the actual contractual/legal target; this is not a conformance certificate.
10. Show appropriate account, role, sharing, access and session states. Use clearly synthetic patient data in examples and demos. Access or expose real patient information only for an authorized purpose with suitable safeguards; never assume design review authorizes disclosure into screenshots, logs, analytics, prompts or exports.
11. Adapt language and detail for patients and caregivers. Preserve uncertainty, explain unfamiliar terms, make the next action concrete, and verify comprehension; do not turn an abnormal result into an invented diagnosis.
12. Separate AI-generated suggestions from verified records and approved actions. Show relevant source, limitations and review state; never invent evidence or confidence percentages. Do not add autonomous clinical action to a task that only requests a UI.

## Verify and deliver

Choose checks from the changed task's plausible failure modes, not an indiscriminate checklist. Test the primary action, critical context, failure/recovery, and affected keyboard/mobile behavior. Include interruptions, network ambiguity, and stale data when the flow depends on them.

Use representative users for claims about real-world usability or comprehension. An agent walkthrough, automated accessibility scan, code test, or attractive prototype cannot establish clinical safety, WCAG conformance, or regulatory approval.

Deliver the requested artifact plus only the useful supporting detail:

- Key assumptions and consequential design choices.
- Concrete findings or changes with evidence and relevant locations.
- Checks actually run, outcomes, and meaningful coverage limits.
- Unresolved clinical, backend, privacy, accessibility, or regulatory dependencies, with an acceptance check or owner when known.

For a handoff, specify identity, units/time, status transitions, permissions, retries and conflict behavior that the frontend depends on. Label proposed contracts as proposals. Do not claim that a simulated backend implements them.

## Scope and judgment

Follow current user intent and explicit project decisions. Preserve approved branding while retaining clinical context and accessibility. This skill governs healthcare interaction behavior; it does not impose a visual style, technology stack, or redesign outside the requested scope.

Do not make a blanket HIPAA, FDA, IEC, GDPR, or accessibility compliance claim. Not every healthcare application has the same obligations. Use this skill to improve interfaces and identify evidence gaps, with the appropriate clinical and regulatory owners resolving product-specific requirements.
