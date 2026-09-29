# Government design systems: optional CDC and USWDS context

Checked 2026-09-28. Load this reference only when the project explicitly uses CDC WCMS, CDC agency identity, USWDS, or applicable U.S. federal delivery requirements. These are not universal healthcare design rules. This independent skill is not endorsed by CDC, HHS, GSA, or USWDS.

## Establish the applicable system

- Identify the product owner, CMS/template generation, existing design system, deployment context, and required accessibility standard before choosing components. A healthcare subject does not establish CDC affiliation or Section 508 applicability.
- CDC's public [TP4 gallery](https://www.cdc.gov/wcms/4.0/cdc-wp/index.html) describes WCMS modules and refers site-management questions to an internal guide. Confirm current project requirements with the owner; do not assume TP4 is the applicable template.
- Reuse the project's existing shell and components. When both systems are explicitly required, document which system owns each shell element and interactive component. A CDC/USWDS crosswalk is a project design decision, not an official certification scheme.

## Brand and visual constraints

- Use agency logos or marks only with the relevant authorization; a component's logo slot grants no rights. CDC [restricts use of its marks](https://www.cdc.gov/other/agencymaterials.html), and TP4 [site-identity images require approval](https://www.cdc.gov/wcms/4.0/cdc-wp/page-and-site-options/site-title-bar.html). Do not add government identity to an unaffiliated product.
- The USWDS [government banner](https://designsystem.digital.gov/components/banner/) is scoped to appropriate official `.gov`/`.mil` sites using HTTPS. Do not use it to make a public skill demo or private healthcare product appear governmental.
- If TP4 applies, use its [approved palette](https://www.cdc.gov/wcms/4.0/cdc-wp/page-and-site-options/preferred-color-pairings.html). TP4 blue `#005eaa` differs from USWDS `blue-60v` `#005ea2`. Test actual text, controls, charts, focus and interaction states; approved swatches alone do not prove interface accessibility.
- CDC's [March 2026 writing tip](https://www.cdc.gov/nceh/clearwriting/writing-tips/2026/accessible-fonts-3-25-26.html) describes Roboto headings and Nunito Sans body/subheadings in new internal templates. It is not sufficient evidence of a universal CDC website mandate or an “accessible font” certification. Confirm the governing typography rather than automatically replacing it.

## Interaction and implementation

- Follow the installed version's component documentation; avoid competing JavaScript controllers for the same element. Preserve labels, relationships, keyboard operation and focus behavior when styling.
- CDC Critical → USWDS emergency is a plausible project mapping, not an official crosswalk. Select announcement behavior by urgency and timing: `alert` for urgent updates, `status` for advisory updates, and a named `region` where a navigable static notice helps. Do not turn every notice into an interruptive live region. See [USWDS alerts](https://designsystem.digital.gov/components/alert/) and the [WAI alert pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alert/). Editorial expiry of outdated advisories is different from auto-dismissing a message before a person can read it.
- Do not invent a mapping between numbered [CDC viewports](https://www.cdc.gov/wcms/4.0/cdc-wp/page-and-site-options/Mobile-Columns.html) and [USWDS breakpoints](https://designsystem.digital.gov/utilities/layout-grid/).
- Add USWDS only when the product needs it. For existing installations, inspect the lockfile and [release notes](https://github.com/uswds/uswds/releases), then test required upgrades. Use the documented [Sass and asset setup](https://designsystem.digital.gov/documentation/developers/); token names alone do not load fonts or initialize components.

## Validation and claims

Use WCAG 2.2 AA as a design target where appropriate, while recording the actual jurisdictional and contractual requirements. [Revised Section 508](https://www.access-board.gov/ict/) incorporates WCAG 2.0 A/AA within its scope; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) removed Parsing 4.1.1, which older-policy reporting may still require. The [ICT Baseline](https://ictbaseline.access-board.gov/web-baselines/) defines minimum checks, not a complete testing process.

Test representative tasks, keyboard access, screen readers, reflow/zoom, error recovery, and customized states. [USWDS explicitly requires project-level testing](https://designsystem.digital.gov/documentation/accessibility/). Neither importing a library nor passing an automated scan proves conformance or clinical safety. Report what was checked, its result, and any remaining gap.
