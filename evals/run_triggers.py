#!/usr/bin/env python3
"""Measure which skill each trigger-eval query activates, with this plugin's skills (and optionally others) competing.

Loads this repository as a plugin in headless Claude Code with user-level settings, skills, and
MCP servers excluded, so globally installed copies and connectors cannot interfere. Each query runs
in an empty temporary directory with only the Skill and Read tools, and stops at the first Skill
call. Reading a file before choosing a skill is allowed.

    python3 evals/run_triggers.py --runs 3 --workers 6 --also-plugin ../accessibility-audit-kit
"""

import argparse
import collections
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent


def first_skill(query, timeout, extra_plugins=()):
    """Return the first skill invoked, "" if the session ended without one, or None if the run failed."""
    with tempfile.TemporaryDirectory() as cwd:
        command = [
            "claude", "-p", query, "--plugin-dir", str(ROOT), *[a for p in extra_plugins for a in ("--plugin-dir", str(p))], "--setting-sources", "project,local", "--strict-mcp-config",
            "--output-format", "stream-json", "--verbose", "--max-turns", "3", "--tools", "Skill,Read",
            "--no-session-persistence",
        ]
        process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        try:
            for line in process.stdout:
                try:
                    event = json.loads(line)
                except ValueError:
                    continue
                if event.get("type") == "assistant":
                    for block in event["message"].get("content", []):
                        if block.get("type") == "tool_use" and block.get("name") == "Skill":
                            return str(block.get("input", {}).get("skill", "")).split(":")[-1]
                if event.get("type") == "result":
                    return ""
            return None
        finally:
            process.kill()
            process.wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--runs", type=int, default=2, help="Runs per unique query")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--skill", action="append", help="Limit to these skills' trigger sets")
    parser.add_argument("--json", type=Path, help="Write full results to this file")
    parser.add_argument("--also-plugin", type=Path, action="append", default=[], help="Load another plugin so its skills compete too, e.g. accessibility-audit-kit")
    args = parser.parse_args()

    sets = {}
    for path in sorted(ROOT.glob("evals/*/triggers.json")):
        if not args.skill or path.parent.name in args.skill:
            sets[path.parent.name] = json.loads(path.read_text())
    queries = sorted({item["query"] for items in sets.values() for item in items})
    jobs = [query for query in queries for _ in range(args.runs)]
    print(f"Running {len(jobs)} sessions for {len(queries)} unique queries...", file=sys.stderr)
    choices = collections.defaultdict(list)
    with ThreadPoolExecutor(args.workers) as pool:
        for query, skill in zip(jobs, pool.map(lambda q: first_skill(q, args.timeout, args.also_plugin), jobs)):
            choices[query].append(skill)

    report = {}
    failures = 0
    for skill, items in sets.items():
        rows = []
        for item in items:
            picks = [c for c in choices[item["query"]] if c is not None]
            rate = sum(c == skill for c in picks) / len(picks) if picks else 0.0
            ok = bool(picks) and ((rate >= 0.5) if item["should_trigger"] else (rate < 0.5))
            failures += not ok
            rows.append({**item, "rate": rate, "picks": picks, "pass": ok})
        report[skill] = rows
        passed = sum(r["pass"] for r in rows)
        print(f"\n{skill}: {passed}/{len(rows)} passed")
        for r in rows:
            mark = "pass" if r["pass"] else "FAIL"
            want = "should" if r["should_trigger"] else "should not"
            picked = ", ".join(p or "(none)" for p in r["picks"]) or "(run failed)"
            print(f"  {mark}  {want} trigger | picked: {picked} | {r['query'][:70]}")
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
