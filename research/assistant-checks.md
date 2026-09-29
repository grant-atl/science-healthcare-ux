# Assistant check inputs and outputs

Run September 28, 2026. All fixtures are synthetic. The evaluator received the requests and skill files, not expected answers. These records preserve actual responses; they are not executed application tests.

# Synthetic skill test requests

Use the appropriate skill and relevant references to answer each request. These scenarios contain all needed input facts. Do not browse, operate a live application, alter source artifacts, invent test results, or contact anyone. Produce actual answers to the user requests; afterward, report unclear or conflicting skill instructions.

## S1 — scientific comparison

Use Scientific Software UX. Review this physical-science simulation results screen; corrections only, no code. Run A records force in N, run B records force in kN. The chart plots both raw vectors [2, 3] on a shared axis labeled “Force”, with no conversion or unit labels. Run B's solver terminated early, but its tile says Complete because the CSV export succeeded. The run was configured with model v1; the UI's Rerun button now silently uses model v2 and current defaults. The table displays specimen ID 00127 as 127. Describe the necessary interface corrections and the backend information they need.

## S2 — scientific reproducibility claim

Use Scientific Software UX. Write one honest README sentence to replace “Every result is fully reproducible with one click.” This prototype stores only the final CSV, not input identities, parameter defaults, reference data, calibration, random seed, or software version. Do not redesign the product or choose scientific parameters.

## S3 — narrow scientific wording

Use Scientific Software UX. Only improve the label “Job completed successfully.” The server reports queued, no execution has started. Return the label only.

## H1 — patient results

Use Healthcare Software UX. Review this patient portal result card and give concise corrections. The approved backend record has value 6.2, unit unavailable, no reference interval, and interpretation pending. UI draft: “Dangerously high. You have diabetes. Start treatment now.” The caregiver is using proxy access but the card shows only the caregiver's name, no patient's identity. Clicking Mark read hides the result from the clinician's follow-up queue. No clinical escalation policy has been supplied. Do not diagnose or invent a clinical next step.

## H2 — ambiguous order submission

Use Healthcare Software UX. Review a proposed order workflow. Patient A's draft is open when the user switches to Patient B in another tab. The draft still uses A internally but the heading now shows B. After submission times out, the screen says Failed and offers Retry; Retry creates a new order without looking up whether the first one was accepted. The button called Undo cancels only the local view after dispatch. Give the key corrections and one relevant verification scenario; no code.

## H3 — narrow healthcare wording

Use Healthcare Software UX. Only shorten this scheduling button label: “Click here to view the available appointment times.” Do not audit or redesign the form.


# Independent forward-use results

These answers use only the six synthetic requests, the two portable skills, and their relevant references. No source research, build notes, other agents’ conclusions, browsing, live application actions, or human testing were used. Verification below means a proposed acceptance check, not a check that was run.

## S1 — scientific comparison

Four corrections are needed; all affect scientific meaning or record identity and are high priority.

| Location and consequence | Interface correction | Backend information needed | Verification |
| --- | --- | --- | --- |
| Shared force chart: identical plotted vectors imply equal forces despite a 1,000-fold unit difference. | Convert both series to one explicit axis unit. For an axis labeled **Force (N)**, show A as `[2, 3]` and B as `[2000, 3000]`; retain each series’ original unit in its details. | Authoritative quantity/unit metadata for each series, original values, and the tested conversion contract; retain run identity and conversion provenance. | Compare these two supplied vectors and inspect the chart, exact-value view, and export for consistent units and values. |
| Run B tile: **Complete** reports CSV export success as solver success. | Show **Solver terminated early** and the supplied termination reason/diagnostics; display **CSV exported** separately. Mark the displayed result partial where the authoritative run record supports that state. Do not imply convergence or scientific validity. | Solver execution/termination state, reason, available output extent and diagnostics, separate export state, and any supplied convergence/QC state. | An early-termination run with a successful export must still show early termination; the exported file must not change the run outcome. |
| **Rerun**: silently changing v1 to v2 and applying current defaults prevents a faithful repeat. | Show the original model/version and resolved settings. A rerun should create a linked new run using that recorded configuration; show changes explicitly when the user chooses an updated configuration. If v1 or original settings are unavailable, disclose that limitation before submission. | Original input identities, model/tool version, actual resolved settings including defaults, relevant references/environment/seed where applicable, version availability, and parent/new run IDs. | Change the current model/defaults, reopen the v1 run, and verify that rerun preserves the recorded configuration or explicitly reports what cannot be recovered. |
| Specimen table: **00127** becomes **127**, changing a string identifier. | Render **00127** exactly and preserve it through selection, links, import, and export. | The authoritative identifier as a string end to end; any separate internal key must remain associated with it. If zeros were discarded upstream, recover from the source rather than guessing padding. | Round-trip `00127` and `127` as distinct string IDs without merging or changing either. |

These are corrections inferred from the supplied screen behavior; backend availability and implementation have not been inspected.

## S2 — scientific reproducibility claim

This prototype stores only the final CSV and does not retain the inputs, resolved settings, reference data, calibration, random seed, or software version needed to support reproducible reruns.

## S3 — narrow scientific wording

Queued

## H1 — patient results

- Replace the unsupported diagnosis, danger claim, and treatment instruction with **“Result: 6.2 · Unit unavailable. Reference interval unavailable. Interpretation pending.”** Do not assign an abnormality level or infer a diagnosis from this record. Check that missing metadata and pending interpretation never generate diagnostic or treatment copy.
- Show the patient’s identity using approved identifiers, alongside **“[Caregiver] viewing for [Patient]”** and the applicable proxy context. Check that patient and actor remain distinct when proxy context changes; the backend must supply the correct patient, actor, and access scope.
- Make **Mark read** affect only the supported viewing/read state. It must not remove a result from the clinician’s follow-up queue or mark clinical follow-up resolved. Check that the same result remains in that queue after the caregiver marks it read; backend read, ownership, and resolution states must be separate.
- Leave clinical follow-up and escalation copy pending the responsible clinical owner’s approved policy. None was supplied, so there is no basis to invent urgency or a clinical next step.

## H2 — ambiguous order submission

- **Keep the draft and patient context aligned.** A’s draft must not appear beneath B’s heading. Preserve it under A, then explicitly reconcile the tab’s context on return and before submission. Show the actual patient and order in the commitment summary. The server must validate the draft’s patient binding and authorization; a changed heading cannot retarget an order.
- **Treat a timeout as an unknown outcome.** Show **“Submission status unknown”**, reconcile the original submission’s status, and use a stable submission identifier with a backend deduplication contract. Do not offer a retry that blindly creates another order; expose the confirmed accepted or rejected outcome when available.
- **Name the local action accurately.** If **Undo** only closes the local view, label it **Close** and preserve the submitted order’s status. Any actual cancellation needs a separate supported workflow and authoritative acknowledgement; closing a view must never imply that a dispatched order or downstream care was reversed.

**Verification scenario, proposed:** Open A’s draft, switch another tab to B, then return and attempt submission. Confirm the heading, draft and actual submission target agree and require explicit context reconciliation if they do not. Let the server accept the order but drop its response. Confirm the UI reports an unknown outcome, resolves the original submission to the existing order, and creates no duplicate on a repeated attempt. Close the view and reopen the order; its accepted state must remain unless the server has separately confirmed cancellation. This scenario requires backend identity, status lookup, deduplication and cancellation contracts; those guarantees have not been verified.

## H3 — narrow healthcare wording

View available times

## Unclear or conflicting instructions

No blocking conflicts were encountered. The references supplied enough standalone guidance for all six requests without requiring their source reports or another skill.

A minor interpretation point: both skills contain broad reporting/verification instructions, while S2, S3 and H3 explicitly restrict the answer. I applied each skill’s scope language and followed the narrower request: S2 is one sentence, S3 and H3 are labels only, with no unsolicited audit or check report inside those answers.

The scientific review instruction requests a severity but supplies no severity scale. I used the plain priority “high” for the four integrity defects and did not invent a scoring system or imply clinical severity.
