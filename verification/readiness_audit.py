from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    "agent.yaml", "SOUL.md", "README.md", "RULES.md", "DUTIES.md", "AGENTS.md",
    "EXPLAINABILITY.md", "requirements.txt", ".env.example", ".gitignore",
    "adapter.py", "core/navigator.py", "tests/test_navigator.py",
    "tools/review-program-criteria.yaml", "tools/screen-eligibility.yaml",
    "tools/prepare-application-checklist.yaml", "skills/program-criteria-review/SKILL.md",
    "skills/eligibility-screening/SKILL.md", "skills/application-preparation/SKILL.md"
]
missing = [p for p in required if not (root / p).is_file()]
print(f"Required files: {len(required)-len(missing)}/{len(required)} present")
if missing:
    print("Missing:", ", ".join(missing))
    print("Readiness audit: FAIL")
    sys.exit(1)
print("Readiness audit: PASS")
