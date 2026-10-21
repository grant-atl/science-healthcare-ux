# Eval results

All runs used Claude Code 2.1.128 headless, with user-level settings, skills, and MCP connectors excluded (`--setting-sources project,local --strict-mcp-config`), so only the loaded plugins could respond.

## Trigger evals (2026-10-21)

`run_triggers.py` loaded this plugin **and the [Accessibility Audit Kit](https://github.com/grant-atl/accessibility-audit-kit)**, so seven skills competed for every prompt, including the overlapping `healthcare-accessibility`. Each query ran 3 times.

| Run | Change | Passed | Notes |
|---|---|---|---|
| 1 | New descriptions | 19/20 | "Review this simulation results screen…" triggered `scientific-software-ux` only 1 of 3 times. |
| 2 | Description names simulation results review explicitly | **20/20** | All 20 unanimous across 3 runs. |

The accessibility boundary held in both directions on every run: "Audit our patient portal for WCAG 2.2 AA" went to `healthcare-accessibility`, and every healthcare UX prompt went to `healthcare-software-ux`.

## Behavior evals (2026-10-21)

Each skill reviewed a synthetic fixture in [`files/`](files) with planted problems, in a copy of the repository with `evals.json` removed. Graded by hand against the expectations.

| Skill | Fixture | Result | Notes |
|---|---|---|---|
| scientific-software-ux | [`simulation-results.html`](files/simulation-results.html) | **8/8** | Found all seven planted problems: missing units, duplicate run names, hidden settings and version, in-place rerun, ambiguous zero, "Done" versus validity, unscoped delete. Separated observed defects from unverified backend guarantees and left the fixture unchanged. |
| healthcare-software-ux | [`order-entry.html`](files/order-entry.html) | 7/8, then **8/8 twice** | The first run found every planted problem but invented clinical content: an example dose and rate, a platelet threshold, a clinical interpretation of a unit-less value, and a judgment that a frequency was wrong. The skill now forbids specific clinical values in examples and verification steps, forbids interpreting values without supplied units and ranges, and asks for a final self-check. Two reruns covered every planted problem with no invented values, routing dosing limits and clinical rules to owners as dependencies. |

## Sources

All 69 external links in the references resolved on 2026-10-21, checked in a real browser where sites block scripts. PubMed IDs were confirmed through NCBI E-utilities and the Briefings in Bioinformatics DOI through Crossref; each matches the study the reference describes.

Results vary between runs; rerun after changing a description or a safety rule.
