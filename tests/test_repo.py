"""Structural checks for manifests, skills, references, links, and evals."""

import filecmp
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))


def frontmatter(path):
    match = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not match:
        raise AssertionError(f"{path} has no frontmatter")
    fields = {}
    for line in match.group(1).splitlines():
        if line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if value and not value.startswith('"') and ": " in value:
            raise AssertionError(f"{path}: unquoted ': ' in {key} breaks YAML")
        fields[key] = value.strip('"')
    return fields


class ManifestTests(unittest.TestCase):
    def test_versions_agree(self):
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        version = plugin["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(market["metadata"]["version"], version)
        self.assertEqual(next(p for p in market["plugins"] if p["name"] == plugin["name"])["version"], version)
        for skill in SKILLS:
            self.assertIn(f'version: "{version}"', (skill / "SKILL.md").read_text(), skill.name)
        self.assertIn(f"## [{version}]", (ROOT / "CHANGELOG.md").read_text())


class SkillTests(unittest.TestCase):
    def test_expected_skills(self):
        self.assertEqual([s.name for s in SKILLS], ["healthcare-software-ux", "scientific-software-ux"])

    def test_frontmatter(self):
        for skill in SKILLS:
            fields = frontmatter(skill / "SKILL.md")
            self.assertEqual(fields["name"], skill.name)
            self.assertTrue(100 <= len(fields["description"]) <= 1024, skill.name)
            self.assertIn("Use when", fields["description"], skill.name)
            self.assertEqual(fields["license"], "MIT")

    def test_each_skill_ships_license_and_codex_metadata(self):
        for skill in SKILLS:
            self.assertTrue(filecmp.cmp(ROOT / "LICENSE", skill / "LICENSE", shallow=False), skill.name)
            self.assertIn("display_name:", (skill / "agents/openai.yaml").read_text(), skill.name)

    def test_skills_are_self_contained(self):
        for skill in SKILLS:
            for doc in skill.rglob("*.md"):
                for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", doc.read_text()):
                    if re.match(r"^[a-z]+:", target):
                        continue
                    resolved = (doc.parent / target).resolve()
                    self.assertTrue(resolved.is_relative_to(skill.resolve()), f"{doc.relative_to(ROOT)} links outside its skill: {target}")


class LinkTests(unittest.TestCase):
    def test_relative_markdown_links_resolve(self):
        for doc in ROOT.rglob("*.md"):
            if ".git" in doc.parts:
                continue
            for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", doc.read_text()):
                if not re.match(r"^[a-z]+:", target):
                    self.assertTrue((doc.parent / target).exists(), f"{doc.relative_to(ROOT)} -> {target}")


class EvalTests(unittest.TestCase):
    def test_every_skill_has_balanced_trigger_evals(self):
        for skill in SKILLS:
            items = json.loads((ROOT / "evals" / skill.name / "triggers.json").read_text())
            self.assertTrue(all(set(i) == {"query", "should_trigger"} for i in items), skill.name)
            self.assertGreaterEqual(sum(i["should_trigger"] for i in items), 5, skill.name)
            self.assertGreaterEqual(sum(not i["should_trigger"] for i in items), 4, skill.name)


if __name__ == "__main__":
    unittest.main()
