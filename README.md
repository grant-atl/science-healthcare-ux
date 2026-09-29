# Scientific Software UX and Healthcare Software UX

Two independent, research-informed Agent Skills for designing, implementing, and reviewing software interfaces. Choose the skill for the work being done; neither requires the other.

| Skill | Use for |
| --- | --- |
| **Scientific Software UX** | Research workspaces, laboratory and instrument interfaces, scientific analysis, simulations, visualization, data and sample records, and reproducible workflows across scientific disciplines. |
| **Healthcare Software UX** | Clinician, patient, caregiver, and care-administration interfaces: EHRs, portals, scheduling, ordering, results, monitoring, and care coordination. |

Both preserve domain meaning and accessibility while adapting to the actual task. Scientific Software UX focuses on object identity, units, parameters, provenance, and reproducibility. Healthcare Software UX focuses on patient/encounter context, care-workflow state, understandable information, and recovery from consequential mistakes.

Clinical research and clinical genomics can need both perspectives. Select them deliberately where relevant; neither skill invents scientific findings, treatment advice, clinical rules, or a compliance determination.

## Install

Install either or both skills:

```sh
npx skills add grant-atl/science-healthcare-ux --skill scientific-software-ux -a codex -a claude-code
npx skills add grant-atl/science-healthcare-ux --skill healthcare-software-ux -a codex -a claude-code
```

These use the community [Skills CLI](https://github.com/vercel-labs/skills). Review the files before installing. See [installation and distribution](PUBLISHING.md).

Invoke `$scientific-software-ux` or `$healthcare-software-ux` in Codex; `/scientific-software-ux` or `/healthcare-software-ux` in Claude Code. If earlier skills cover the same work, explicitly invoke the intended one.

## Example requests

- “Use Scientific Software UX to review this simulation results screen. Check units, run comparison, parameter visibility, provenance, and failed-run recovery.”
- “Use Scientific Software UX to design a research instrument acquisition flow with clear calibration and run state.”
- “Use Healthcare Software UX to review this patient portal's results page for comprehension, access needs, and next-step clarity.”
- “Use Healthcare Software UX to improve this order workflow. Preserve patient context and distinguish saved drafts, submission, acceptance, and signing.”

## References

Each skill includes source citations and guidance on interpreting the evidence:

- [Scientific Software UX: evidence and evaluation](skills/scientific-software-ux/references/evidence-and-evaluation.md)
- [Healthcare Software UX: sources](skills/healthcare-software-ux/references/sources.md)

The skills use the [Agent Skills format](https://agentskills.io/specification), with self-contained references and no required service, API key, or executable helper. Installation and behavior can vary by host.

## License

[MIT](LICENSE). Each skill includes the license so its notice travels with standalone installations. Source publications retain their own terms and are linked rather than bundled.
