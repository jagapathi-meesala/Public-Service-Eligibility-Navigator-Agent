# Public Service Eligibility Navigator Agent

A transparent planning assistant for reviewing public-service program criteria, performing a preliminary eligibility screen, and preparing application checklists.

## Capabilities
- Extract and organize criteria from supplied program descriptions.
- Compare user-provided circumstances with explicit criteria.
- Identify unknowns and missing evidence rather than guessing.
- Draft a checklist of documents and questions to verify with the agency.

## Quick start
Python 3.10+ is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python3 verification/readiness_audit.py
opengap validate
```

## Example
```python
from core.navigator import screen_eligibility
program = {
    "criteria": [
        {"id": "residency", "description": "Applicant must reside in the service area"}
    ]
}
applicant = {"residency": "unknown"}
print(screen_eligibility(program, applicant))
```

## Important limitations
This project provides preliminary information organization only. It does not make official eligibility decisions, guarantee benefits, or replace current agency guidance. Do not submit sensitive personal information to an untrusted system.
