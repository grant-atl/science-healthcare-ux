# Installation and distribution

Instructions checked September 28, 2026. The [GitHub repository](https://github.com/grant-atl/science-healthcare-ux) contains two independently installable skills under the [MIT license](LICENSE).

## Install either skill

```sh
npx skills add grant-atl/science-healthcare-ux --list
npx skills add grant-atl/science-healthcare-ux --skill scientific-software-ux -a codex -a claude-code
npx skills add grant-atl/science-healthcare-ux --skill healthcare-software-ux -a codex -a claude-code
```

Select only the agents you use. Add `-g` to an installation command for personal use across projects. These commands use the community [Skills CLI](https://github.com/vercel-labs/skills), separate from either product's official directory. Review the source before installation.

For manual installation, copy the entire selected skill folder to a supported location:

| Host | Project location | Personal location |
| --- | --- | --- |
| Codex | `.agents/skills/SKILL-NAME/` | `~/.agents/skills/SKILL-NAME/` |
| Claude Code | `.claude/skills/SKILL-NAME/` | `~/.claude/skills/SKILL-NAME/` |

Replace `SKILL-NAME` with `scientific-software-ux` or `healthcare-software-ux`. Invoke it with `$SKILL-NAME` in Codex or `/SKILL-NAME` in Claude Code. Restart Codex if new files are not detected. [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

For Claude web/desktop upload, ZIP the selected skill folder with one top-level named folder containing `SKILL.md`, `LICENSE`, and `references/`. Use **Customize → Skills → + → Create skill → Upload a skill**, then enable and test the uploaded skill. Do not upload the entire repository ZIP. [Claude packaging](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Optional discovery

- **skills.sh:** files remain hosted in GitHub. The [FAQ](https://www.skills.sh/docs/faq) describes listing through installation telemetry; do not assume immediate indexing or a specific rank.
- **OpenAI Plugins Directory:** a separate skills-only plugin route with verified publisher identity, listing material, five positive and three negative cases, review, and a later publication step. No server is required for a skills-only plugin, but this bundle does not include a plugin wrapper or submission. [Packaging](https://developers.openai.com/plugins/build/plugins), [submission](https://developers.openai.com/plugins/deploy/submission).
- **Claude plugin distribution:** optional plugin/catalog packaging. Hosting a catalog and submitting to Anthropic's directory are different actions. [Marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

The first release needs no website or running service. Describe it as research-informed interface guidance. Preserve third-party source terms; the MIT license covers this repository’s original material, not the linked source publications.
