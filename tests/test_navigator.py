from core.navigator import review_program_criteria, screen_eligibility, prepare_application_checklist

def test_review_valid_criteria():
    result = review_program_criteria({"name": "Example", "criteria": [{"id": "residency", "description": "Lives locally"}]})
    assert len(result["criteria"]) == 1
    assert result["issues"] == []

def test_review_flags_invalid_criteria():
    result = review_program_criteria({"criteria": [{"description": "Missing id"}]})
    assert result["issues"]

def test_screen_unknown_when_fact_missing():
    result = screen_eligibility({"criteria": [{"id": "income", "description": "Income limit"}]}, {})
    assert result["results"][0]["status"] == "unknown"

def test_screen_required_value_match():
    program = {"name": "Example", "criteria": [{"id": "area", "description": "Service area", "required_value": "local"}]}
    result = screen_eligibility(program, {"area": "local"})
    assert result["results"][0]["status"] == "meets"

def test_screen_required_value_mismatch():
    program = {"criteria": [{"id": "area", "description": "Service area", "required_value": "local"}]}
    assert screen_eligibility(program, {"area": "remote"})["results"][0]["status"] == "does_not_meet"

def test_checklist_does_not_invent_document_requirements():
    result = prepare_application_checklist({"name": "Example"})
    assert result["documents_to_verify"] == []
    assert result["questions_to_ask"]

def test_invalid_documents():
    import pytest
    with pytest.raises(ValueError):
        prepare_application_checklist({}, "not-a-list")
