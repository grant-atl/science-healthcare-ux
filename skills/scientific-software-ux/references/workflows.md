# Workflows and scientific state

Read the sections that match the feature. These patterns are design synthesis, not a prescribed architecture or experimental protocol.

## Identity, records, and physical work

Use stable IDs and versions, not row positions or editable names, for selection and actions. Disambiguate similar results using object type, project/source, date, and relevant scientific metadata. Preserve context across sorting, filtering, pagination, refresh, and deep links.

Show relationships needed for the work: specimen → measurement → dataset → analysis, or model → configuration → simulation → result. A table or history is often enough; do not require a graph.

For sample custody, distinguish planned transfer, physical movement, and accepted digital record. A scanner can help select identity but cannot establish eligibility or prove movement. Show decoded identity, validate destination, commit once, and expose acknowledgment. A lost response is not grounds to repeat a physical movement. A correction must not fabricate a physical return or erase required custody history.

For research records, separate the plan/template, execution, observations, deviations, and interpretation. Use draft/review/approval states only where the product actually needs them. Comments, edits, reviews, and signatures are different events. Preserve prior state where traceability requires it; ordinary draft editing need not become a regulated workflow.

## Instruments and acquisition

Keep instrument identity, connection, observation timestamp, and freshness clear. Distinguish a requested setpoint from an acknowledged setting and a measured reading. Show calibration reference/version or validity status when supplied; retain the product's calibration controls and do not invent schedules or correction factors.

Use the instrument's real command/feedback contract. After a timeout, reconcile the original command and actual device state before retrying a consequential action. Software cancel/stop acknowledgment and verified safe physical state may differ. Preserve required hardware interlocks and domain operating procedures; do not replace them with a UI confirmation.

Separate acquisition state from file transfer and analysis. Expose dropped samples, clipping/saturation, disconnection, invalid readings, and source-clock uncertainty when relevant to interpretation. Missing acquisition data should not silently become zeros or interpolated observations.

## Values, parameters, and imports

Treat a quantity as value + unit + relevant qualifiers, source precision, and uncertainty. Label the unit adjacent to entry/display, including table headers where unambiguous. Preserve full stored precision; display rounding must not change analysis inputs.

Keep missing, zero, censored/below detection, invalid, and not applicable distinct. Preserve string identifiers and leading zeros. Localized numeric entry must have an explicit parsing policy; exports need unambiguous numbers, units, missing-value semantics, and timestamps.

A unit change must convert the value correctly or be explicitly identified as correcting erroneous metadata. Dimensional compatibility alone does not establish scientific equivalence: temperature values versus temperature differences, absolute versus gauge pressure, counts versus rates, and linear versus logarithmic measures need their actual definitions. Use the project's tested unit library or format contract; do not invent conversions from labels. SI expression guidance is available in [BIPM's SI Brochure](https://www.bipm.org/en/publications/si-brochure).

Validate actual format/version, metadata, input pairing, reference/coordinate compatibility, and scientific ranges supplied by the domain owner. Distinguish a scientific validity bound from a technical implementation limit. Do not infer units, assemblies, coordinate frames, or time bases from filenames.

For parameters show preset name/version and applicability, resolved values including defaults, explicit overrides, and validation reasons. Editing a completed run's configuration proposes a new run. Never silently rewrite what executed.

## Analysis, simulation, and reproducibility

Make the relevant record inspectable and exportable:

- Input identities/versions or hashes and upstream transformations.
- Workflow/model/tool versions and resolved settings, including defaults.
- Reference data, environment/dependency versions, random seeds and known nondeterminism when relevant.
- For simulations: supplied geometry/mesh, initial and boundary conditions, solver settings/tolerances, and convergence/termination information as relevant to the model.
- For measurements: instrument/acquisition and calibration metadata as relevant to the interpretation.
- Actor, timestamps, outputs, diagnostics, status, and QC.

This is a contextual list, not a universal database schema. Automatically capture known system state; ask people for rationale rather than making them reconstruct settings manually. [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) distinguishes entities, activities, agents, and derivations; adopt its serialization only if interoperability needs it.

Preserving a seed or container alone does not guarantee exact reproduction. Hardware, parallelism, mutable references, missing inputs, and unavailable environments can matter. Show known limitations; define whether the task needs bitwise reproduction, numerical agreement within an agreed tolerance, or another domain criterion.

Successful solver termination, convergence, and physical/model validity are distinct. Expose supplied diagnostics; do not choose tolerances, mesh adequacy, or validation criteria as interface styling decisions.

[FAIR principles](https://www.nature.com/articles/sdata201618) support identifiers, metadata, provenance, and reuse conditions. They allow authentication/authorization and do not require public release of restricted data or mandate a technology stack.

## Jobs, batches, and recovery

Before costly work, summarize inputs, actual settings, output destination, overwrite behavior, and available resource estimates. Label estimates. Separate invalid conditions from unusual but legitimate choices.

For batches, distinguish selected rows, this page, all filtered items, and all records. Show counts, ineligible items, and partial-versus-atomic behavior. Revalidate a stale selection before mutation.

Use authoritative job states. Preserve a durable run identity across navigation/reconnect. Distinguish queued, running, partial, complete, failed, cancellation requested, and cancelled when the backend does. Do not invent percent progress from stages.

Report each failed item's stage, known outcome, and recovery. Preserve completed results. A request that timed out may already have committed: show unknown/pending confirmation, reconcile its original submission ID, and only replay under the backend's deduplication contract. Retrying a request and starting a new scientific run are different operations.

Separate upload, parsing, validation, and accepted import. Report rejected rows and conversions; do not silently drop metadata. Offline work is conditional: show local, queued, syncing, accepted, and conflicted states and specify replay, clocks, permissions, and conflict behavior with the backend owner.

## Collaboration and handoff

Keep authorship, ownership, review, and access distinct. Sharing a live result and sharing a fixed snapshot have different meanings. State which one the product provides. Use explicit handoff/acceptance when another role owns the next step.

Specify backend guarantees only where the changed flow relies on them: authoritative validation, permission checks, version conflicts, atomicity, idempotency, retention of history, and meaningful error codes. Mark missing guarantees as unimplemented. Hidden controls, a success toast, or an audit-style timeline cannot establish those guarantees.
