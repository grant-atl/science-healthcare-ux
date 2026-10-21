---
name: scientific-software-ux
description: "Design, build, or review user interfaces for scientific software: research workspaces, lab and instrument control, sample and data records, simulation setup and results, computational jobs and pipelines, analysis tools, and scientific visualization. Use when a screen must keep object identity, units, parameters, provenance, uncertainty, and run state clear, including reviewing simulation or analysis results screens for reproducibility, run comparison, and failed-run recovery. Not for clinical care workflows, and does not produce scientific conclusions."
license: MIT
metadata:
  author: grant-atl
  version: "1.1.0"
---

# Scientific Software UX

Make scientific work easier while preserving the information needed to understand, check, and reproduce it. Apply to the requested interface change; a small fix does not require a platform redesign.

This skill covers software for physical, environmental, computational, and life sciences. Choose guidance by the actual task, not by assuming every scientist runs experiments or every research product is regulated. Clinical care, patient-facing services, and healthcare operations require their own healthcare UX requirements. Research involving human data still needs appropriate privacy controls.

## Understand the task

Inspect the relevant UI, data model, shared components, imports/exports, and actual state transitions. Trace selection → configuration/action → result → recovery. A screenshot cannot establish backend guarantees.

Identify from the available context:

- Role and task: experimentalist, analyst, instrument operator, computational researcher, facility manager, or collaborator. Separate domain expertise from software expertise.
- Objects: datasets, specimens, instruments, observations, models, simulations, analyses, or records; their identity and version; the intended scientific output.
- Environment: workstation, bench, field or shared instrument; interruption, input devices, data scale, connectivity, and collaboration.
- Consequences: wrong object/unit/reference, hidden processing, lost data, costly compute, physical operation, or unsupported interpretation.
- Existing vocabulary, design system, backend contracts, and confirmed domain requirements.

State assumptions. Ask only when an unknown changes scientific meaning, access, record integrity, or a consequential action; continue independent work. Do not invent experimental settings, calibration intervals, QC limits, valid ranges, model assumptions, or retention policies.

## Read only the relevant detail

- Inputs, instruments, samples, records, jobs, simulations, or handoff: [Workflows and scientific state](references/workflows.md).
- Charts, maps, images, sequences, graphs, statistics, or specialized accessibility: [Visualization and interaction](references/visualization.md).
- Research claims, review priorities, user tests, AI, or regulatory scope: [Evidence and evaluation](references/evidence-and-evaluation.md).

These references are self-contained. Other skills and external research documents are not needed at runtime.

## Preserve scientific meaning

1. **Identity:** distinguish names from stable IDs and versions. Keep the active object and action scope clear across navigation, filters, and batch operations.
2. **Context:** retain the relevant unit, coordinate frame, reference, time basis, calibration, or model context with the values it qualifies.
3. **Provenance:** make actual inputs, resolved settings, transformations, versions, and output lineage inspectable. Reruns are linked new runs.
4. **Evidence:** distinguish observations, derived data, simulated/predicted values, QC, uncertainty, interpretation, and AI suggestions. Missing, zero, below detection, excluded, pending, and failed are different states.
5. **Control:** validate before costly or irreversible actions; expose consequences and selection scope. Use confirmations and hard stops proportionally to actual consequence.
6. **Recovery:** distinguish requested, acknowledged, executing, partial, failed, cancelled, and uncertain outcomes. A successful click or completed computation does not prove a valid scientific result.

The UI must reflect authoritative behavior. It cannot provide durable storage, authorization, atomicity, instrument interlocks, or an audit trail simply by displaying controls.

## Shape the interface

- Organize around durable domain objects and their relationships. Provide direct search by identifier and contextual links to source, derived result, and history when useful.
- Keep the current task and object prominent. Give the primary work area sufficient space; group parameters by scientific meaning and move secondary detail into an inspector without hiding consequential settings.
- Support guided and expert paths to the same recorded operation. Explain presets, show actual values, and preserve keyboard and batch efficiency where needed.
- Keep density when it helps comparison. Use legible numeric columns, meaningful headings, restrained semantic color, and consistent value/unit and status components. Do not remove evidence merely to achieve fewer clicks or a sparse layout.
- Build views around the scientific question. Link overview, selected detail, and source evidence; keep scales, filters, transformations, and uncertainty intelligible.
- Use literal actions and useful errors: affected object, failed stage, known outcome, and safe recovery. Distinguish computational completion from QC acceptance or scientific validity.
- Reuse the existing product's components and native controls. Add templates, shortcuts, saved views, APIs, or offline support only for a demonstrated workflow need.
- Label synthetic examples and mock states. Protect unpublished, participant, location-sensitive, or otherwise restricted data in screenshots, logs, exports, and AI inputs.

## Apply and verify

**Design/build:** implement the smallest complete requested flow and its consequential exception. Separate proposed backend behavior from implemented behavior. Preserve user choices about platform and visual identity.

**Review:** remain read-only unless fixes are requested. For each material finding give location/evidence, affected task, consequence, severity, correction, and a verification step. Separate observed defects, unverified guarantees, and suggestions. Do not manufacture a fixed number of findings.

**Handoff:** document the contracts affected by the change: object IDs/versions, units/references, validation owner, state transitions, retries, concurrency, permissions, provenance, and acceptance checks. Identify domain questions and their owners without inventing endpoints.

Use existing checks plus a meaningful regression check for changed nontrivial logic. Exercise the main task and a consequential failure with synthetic or approved data. For a viewer, test selection/context and keyboard access; for a mutation, test acknowledgment and recovery; for scientific imports, test semantic round-tripping.

For user evaluation, use representative roles, tasks, and data scale. Measure correct completion, understanding, and recovery alongside effort. Report the result, checks performed, and consequential gaps. Do not claim scientific validation, compliance, universal usability improvement, or successful integration from interface inspection alone.
