# Scientific Software UX and Healthcare Software UX

[![CI](https://github.com/grant-atl/science-healthcare-ux/actions/workflows/ci.yml/badge.svg)](https://github.com/grant-atl/science-healthcare-ux/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Two independent, research-informed Agent Skills for designing, implementing, and reviewing software interfaces. Choose the skill for the work being done; neither requires the other.

| Skill | Use for |
| --- | --- |
| **Scientific Software UX** | Research workspaces, laboratory and instrument interfaces, scientific analysis, simulations, visualization, data and sample records, and reproducible workflows across scientific disciplines. |
| **Healthcare Software UX** | Clinician, patient, caregiver, and care-administration interfaces: EHRs, portals, scheduling, ordering, results, monitoring, and care coordination. |

Both preserve domain meaning and accessibility while adapting to the actual task. Scientific Software UX focuses on object identity, units, parameters, provenance, and reproducibility. Healthcare Software UX focuses on patient/encounter context, care-workflow state, understandable information, and recovery from consequential mistakes.

Clinical research and clinical genomics can need both perspectives. Select them deliberately where relevant; neither skill invents scientific findings, treatment advice, clinical rules, or a compliance determination.

## Install

### Claude Code plugin

```sh
claude plugin marketplace add grant-atl/science-healthcare-ux
claude plugin install science-healthcare-ux@science-healthcare-ux
```

Both skills install together and are namespaced, for example `/science-healthcare-ux:healthcare-software-ux`.

### Agent Skills CLI (Codex, Claude Code, and others)

Install either or both skills:

```sh
npx skills add grant-atl/science-healthcare-ux --skill scientific-software-ux -a codex -a claude-code
npx skills add grant-atl/science-healthcare-ux --skill healthcare-software-ux -a codex -a claude-code
```

These use the community [Skills CLI](https://github.com/vercel-labs/skills). Review the files before installing. See [installation and distribution](PUBLISHING.md).

Invoke `$scientific-software-ux` or `$healthcare-software-ux` in Codex; `/scientific-software-ux` or `/healthcare-software-ux` in Claude Code when installed with the CLI. Choose one install method per agent to avoid duplicate skills. If earlier skills cover the same work, explicitly invoke the intended one.

## Example requests

- “Use Scientific Software UX to review this simulation results screen. Check units, run comparison, parameter visibility, provenance, and failed-run recovery.”
- “Use Scientific Software UX to design a research instrument acquisition flow with clear calibration and run state.”
- “Use Healthcare Software UX to review this patient portal's results page for comprehension, access needs, and next-step clarity.”
- “Use Healthcare Software UX to improve this order workflow. Preserve patient context and distinguish saved drafts, submission, acceptance, and signing.”

## Works alongside accessibility skills

Healthcare Software UX covers care-workflow behavior: patient context, clinical values, status, alerts, and recovery. For WCAG audits of the same product, pair it with an accessibility skill such as the [Accessibility Audit Kit](https://github.com/grant-atl/accessibility-audit-kit). The trigger evals load both together to check that each prompt reaches the right skill; see [evals/RESULTS.md](evals/RESULTS.md).

## References

Each skill includes source citations and guidance on interpreting the evidence:

- [Scientific Software UX: evidence and evaluation](skills/scientific-software-ux/references/evidence-and-evaluation.md)
- [Healthcare Software UX: sources](skills/healthcare-software-ux/references/sources.md)

The skills use the [Agent Skills format](https://agentskills.io/specification), with self-contained references and no required service, API key, or executable helper. Installation and behavior can vary by host. All 69 cited sources were link-checked on 2026-10-21; see the [changelog](CHANGELOG.md).

## Development

```sh
python3 -m unittest discover -s tests -v
claude plugin validate .
python3 evals/run_triggers.py --runs 3 --also-plugin ../accessibility-audit-kit
```

## License

[MIT](LICENSE). Each skill includes the license so its notice travels with standalone installations. Source publications retain their own terms and are linked rather than bundled.
