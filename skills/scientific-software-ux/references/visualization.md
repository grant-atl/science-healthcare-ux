# Visualization and interaction

Choose the representation from the task: compare values, inspect anomalies, locate evidence, trace relationships, or edit scientific objects. The patterns below are design synthesis; preserve the conventions of the actual discipline and format.

## Shared display rules

Show units, axis meaning, scale, normalization/transformation, filters, aggregation, and missingness. Keep comparable views on common scales or disclose their differences. Do not silently rescale, smooth across missing observations, hide exclusions, or imply no data means no effect.

Connect a selected mark to its originating object, record, or region. Distinguish hover, selection, and filtering; preserve identity through reloads. Show stale evidence and the relevant data timestamp. Export figures with labels, legends, processing/filter context, and a traceable originating dataset/run.

Use readable, aligned values for precise comparisons. Choose categorical, sequential, or diverging color according to meaning, with a defined midpoint where relevant. Keep safety/status information understandable without color. Dense expert views may use grouped controls, pinned context, and an inspector; don't replace useful evidence with oversized summary cards.

## Uncertainty and interpretation

- Label what intervals/error bars mean: spread, standard uncertainty, confidence interval, credible interval, prediction interval, or another supplied quantity. Include level/coverage factor and method where relevant; do not invent missing definitions.
- State relevant sample size and independence/replicate context. Distinguish raw observations, summaries, simulations, and model estimates.
- Separate measurement uncertainty, statistical uncertainty, model assumptions, QC, and scientific interpretation. Do not combine them into one unexplained confidence percentage.
- Keep thresholds and their source/version visible. Choosing a significance cutoff, normalization, solver tolerance, or exclusion rule is a scientific decision, not a visual styling decision.
- An ensemble fraction is not automatically a calibrated probability. Explain the ensemble population and weighting if known; show model limitations rather than relabeling them as certainty.

[NIST TN 1297 §7](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty) illustrates why an uncertainty value needs its definition and reporting context; it is measurement guidance, not a universal interval recipe. A p-value is neither the probability that a hypothesis is true nor an effect-size measure. [ASA statement](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf)

## Choose domain-specific context

| Interface | Context and interaction to preserve |
| --- | --- |
| Time series and sensors | Sampling/time basis, irregular intervals, outages, interventions, calibration, and raw versus interpolated/aggregated values; inspect events alongside values |
| Spectra and distributions | Axis quantity/unit, baseline/normalization, resolution/binning, selected peaks/ranges, raw/processed comparison, and supplied fit residuals |
| Simulation/engineering views | Model/run identity, geometry/mesh version, units, frame/orientation, time step, boundary conditions, scalar/vector definitions, clipping, and convergence diagnostics where relevant |
| Maps/geospatial fields | Coordinate reference system/datum, projection, spatial resolution, time, missing coverage, and transformation context; avoid treating projected distance as universally equivalent to physical distance |
| Images/microscopy | Source image/version, dimensions/channels/timepoint, valid calibration and scale, display contrast versus data processing, and overlay/ROI coordinate space |
| Genomics/sequences | Organism, assembly/reference version, coordinate convention, strand/transcript where relevant; linked map/sequence/evidence and explicit gaps or ambiguity |
| Networks/pipelines | Node/edge meaning, direction, filters, and evidence; keep graph structure, parameter configuration, and actual execution separate |
| High-dimensional analyses | Analysis population, preprocessing, exclusions, dimension-reduction/clustering method, and linked observations; plotted proximity alone does not establish a scientific relationship |

Use only the fields that affect the task. Check the actual format and reader before implementing coordinate conversion; one domain's indexing conventions cannot be generalized to all its formats. A scale bar requires valid calibration; absent metadata must not be replaced with invented physical units. Graph layout, interpolation, segmentation, or a model fit must not appear to be an unprocessed observation.

## Accessibility and scale

Apply the project's web accessibility target using [WCAG 2.2](https://www.w3.org/TR/WCAG22/) where relevant. Provide keyboard operation, meaningful focus, labels and status announcements, non-color cues, data access without hover, and alternatives to dragging. Test the specialized viewer itself, including focus restoration after virtualized rows or panels change.

Provide structured access to essential data, selected values, relationships, and controls. A table can complement a chart or image but does not communicate every spatial or visual property; determine what information the actual task requires. Avoid exposing thousands of unstructured canvas objects as an accessibility substitute.

Use existing rendering/storage features first. Windowed tables, image pyramids, indexed ranges, query-centered networks, and level-of-detail views can help at real data scale. Disclose downsampling, truncation, missing tiles, and approximate views, and preserve exact data access where required. Do not mandate a new storage format without inspecting the existing system.

Measure interaction latency and memory on representative data and hardware. Preserve context during loading. Fit workstation comparison, bench/scanner input, or a focused field workflow to its environment instead of compressing a complete desktop editor onto a phone.
