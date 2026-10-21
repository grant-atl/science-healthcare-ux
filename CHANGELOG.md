# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-10-21

### Added

- Claude Code plugin and marketplace manifests, so both skills install with `claude plugin install`.
- Codex display metadata (`agents/openai.yaml`) for each skill.
- Trigger and behavior evals for both skills, with synthetic fixtures and graded results in `evals/RESULTS.md`, and a runner that loads this plugin alongside others, such as the Accessibility Audit Kit, so overlapping skills compete for each prompt.
- Structure tests and CI: manifest and version agreement, frontmatter, self-contained skill links, license copies, and eval files.
- This changelog.

### Changed

- Skill descriptions now say when to use each skill and where its scope ends, for more reliable triggering.
- Skill frontmatter adds `metadata` with author and version.
- Healthcare Software UX forbids specific doses, rates, thresholds, and clinical interpretations in examples and verification steps, and asks for a final self-check, after an eval showed invented clinical values.
- README and PUBLISHING describe the plugin install path and verified eval results.

### Verified

- All 69 external source links resolve, and the PubMed and DOI citations match the studies they describe.

## [1.0.0] - 2026-09-28

### Added

- Initial release: `scientific-software-ux` and `healthcare-software-ux` skills with self-contained references.

[1.1.0]: https://github.com/grant-atl/science-healthcare-ux/compare/9ac6b0c...science-healthcare-ux--v1.1.0
[1.0.0]: https://github.com/grant-atl/science-healthcare-ux/commit/9ac6b0c
