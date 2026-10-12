"""Deterministic preliminary eligibility navigation helpers."""
from typing import Any

VALID_STATUSES = {"meets", "does_not_meet", "unknown"}

def review_program_criteria(program: dict[str, Any]) -> dict[str, Any]:
    name = program.get("name", "Unnamed program")
    criteria = program.get("criteria", [])
    if not isinstance(criteria, list):
        raise ValueError("program.criteria must be a list")
    normalized = []
    issues = []
    for index, item in enumerate(criteria):
        if not isinstance(item, dict):
            issues.append(f"Criterion at index {index} must be an object.")
            continue
        cid = item.get("id")
        desc = item.get("description")
        if not isinstance(cid, str) or not cid.strip():
            issues.append(f"Criterion at index {index} is missing an id.")
        if not isinstance(desc, str) or not desc.strip():
            issues.append(f"Criterion at index {index} is missing a description.")
        if isinstance(cid, str) and cid.strip() and isinstance(desc, str) and desc.strip():
            normalized.append({"id": cid.strip(), "description": desc.strip(), **({"required_value": item["required_value"]} if "required_value" in item else {})})
    return {"program": name, "criteria": normalized, "issues": issues}

def screen_eligibility(program: dict[str, Any], applicant: dict[str, Any]) -> dict[str, Any]:
    reviewed = review_program_criteria(program)
    results = []
    for criterion in reviewed["criteria"]:
        cid = criterion["id"]
        fact = applicant.get(cid, None)
        if fact is None or (isinstance(fact, str) and fact.strip().lower() in {"", "unknown", "not sure", "n/a"}):
            status = "unknown"
            reason = "No usable applicant fact was supplied for this criterion."
        elif "required_value" in criterion:
            status = "meets" if fact == criterion["required_value"] else "does_not_meet"
            reason = f"Supplied value {fact!r} compared with required value {criterion['required_value']!r}."
        elif isinstance(fact, bool):
            status = "meets" if fact else "does_not_meet"
            reason = "Evaluated the supplied boolean fact."
        else:
            status = "unknown"
            reason = "Criterion has no comparison rule; human review is needed."
        results.append({"criterion_id": cid, "description": criterion["description"], "status": status, "evidence": fact, "reason": reason})
    return {"program": reviewed["program"], "results": results, "issues": reviewed["issues"], "official_decision": False}

def prepare_application_checklist(program: dict[str, Any], documents: list[str] | None = None) -> dict[str, Any]:
    if documents is None:
        documents = []
    if not isinstance(documents, list) or any(not isinstance(d, str) for d in documents):
        raise ValueError("documents must be a list of strings")
    return {
        "program": program.get("name", "Unnamed program"),
        "documents_to_verify": [{"item": d, "status": "verify_with_agency"} for d in documents],
        "questions_to_ask": [
            "Which documents are currently required for this program?",
            "What is the current application deadline and submission method?",
            "How can an applicant confirm eligibility or request a review?"
        ],
        "note": "Only supplied document names are listed; this checklist does not establish official requirements."
    }
