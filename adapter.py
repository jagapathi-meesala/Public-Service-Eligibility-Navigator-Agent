"""Simple Python adapter for local integrations."""
from core.navigator import review_program_criteria, screen_eligibility, prepare_application_checklist

def handle(request: dict):
    action = request.get("action")
    if action == "review_program_criteria":
        return review_program_criteria(request.get("program", {}))
    if action == "screen_eligibility":
        return screen_eligibility(request.get("program", {}), request.get("applicant", {}))
    if action == "prepare_application_checklist":
        return prepare_application_checklist(request.get("program", {}), request.get("documents", []))
    raise ValueError(f"Unsupported action: {action!r}")
