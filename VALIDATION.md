# Validation record

Checked September 28, 2026. This record describes checks actually run on the skill package. It does not establish usability with representative users, scientific validity, clinical safety, or compliance.

## Format and packaging

Both skills passed the skill-creator format validator. Package checks verify names match folders, descriptions are under 200 characters, bundled links resolve, each skill's references stay inside its own folder, old personal branding and local machine paths are absent, and ZIP contents/integrity match the final files.

No executable code, external service, API key, plugin wrapper, or runtime dependency is required by either skill. Research citations are links, not embedded copies of source publications.

## Independent assistant checks

An independent assistant received the final skill instructions and six synthetic requests, with no expected answers or prior audit conclusions. It loaded the relevant references and produced actual responses. The author reviewed those responses against the supplied facts and requested scope.

| Case | What was checked | Observed outcome |
| --- | --- | --- |
| Scientific comparison | Newton/kilonewton mismatch, failed solver with successful export, changed rerun defaults, leading-zero specimen ID | Corrected the comparison, separated solver/export states, preserved or disclosed original-run dependencies, and retained string IDs. |
| Reproducibility claim | Only a final CSV is stored; user requests one honest replacement sentence | Removed the unsupported guarantee and identified missing recorded state without redesigning the product. |
| Scientific copy edit | Server says queued; label incorrectly says complete | Returned only “Queued.” |
| Patient results | Missing units/range, interpretation pending, unsupported diagnosis, ambiguous caregiver identity, read status hiding clinical follow-up | Removed invented clinical interpretation, separated patient/proxy identity, preserved follow-up state and left escalation to approved policy. |
| Order submission | Cross-tab patient mismatch, timeout after possible acceptance, duplicate retry, misleading Undo | Required consistent context, reconciliation of unknown outcome, deduplication and truthful cancellation semantics; proposed a relevant scenario without claiming to run it. |
| Healthcare copy edit | User requests only a shorter appointment button label | Returned only “View available times.” |

All six met the checked expectations. The evaluator reported no blocking instruction conflicts. It noted that broad reporting instructions require interpretation for label-only requests; the skills' existing scope language and explicit user requests kept those answers narrow. No instruction changes were required after this pass.

The [requests and actual responses](research/assistant-checks.md) are included for inspection and repetition. These are qualitative samples from one assistant evaluation, not six independent human studies, an automatic-discovery benchmark, or a statistically established success rate.

## Coverage limits

- No installation or behavioral test was run inside Claude Code, Claude web, or every compatible host. The portable format and self-contained references were checked; native host behavior remains to test.
- The initial assistant evaluation used local skill files. It did not test public-repository installation.
- The government references were source-audited, not tested by compiling illustrative Sass/HTML or running a CDC WCMS instance. Those snippets are not shipped as an implementation.
- Original research findings were checked to the source-access depth documented in the evidence files. No raw-data replication, full licensed IEC review, product-specific legal assessment, complete accessibility evaluation, or representative-user trial was performed.

Test fresh installation and invocation in each advertised host before claiming native host validation. For performance claims, evaluate representative tasks, users and data against the actual baseline, measuring correctness and recovery alongside time and effort. The public directory routes may require additional cases and listing material beyond this portable GitHub package.
