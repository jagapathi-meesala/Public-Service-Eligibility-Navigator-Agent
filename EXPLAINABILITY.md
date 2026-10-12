# Explainability

## Inputs
The agent accepts a program description containing explicit criteria and an applicant-facts mapping. It may also accept an application context and a list of documents to verify. Only provided information is used for screening.

## Decision
Each criterion is evaluated using its declared `id` and the corresponding applicant fact. A criterion is `meets` when the supplied fact is explicitly true or matches the stated required value, `does_not_meet` when it explicitly conflicts, and `unknown` when information is absent or ambiguous. The agent does not infer missing facts.

## Limits
The output is a preliminary screening, not an official eligibility decision. Rules can change and the supplied program description may be incomplete or outdated. Confirm eligibility, deadlines, required documents, and appeal routes with the responsible agency.

## Tool: review-program-criteria

### Inputs and Data Sources
Receives a program name and a list of criteria supplied by the user.

### Decision and Reasoning
Checks that each criterion has an identifier and description, then organizes criteria for review.

### Outputs and Evidence
Returns the normalized criteria and notes missing identifiers or descriptions.

### Limits and Constraints
It does not verify whether the supplied criteria are current or authoritative.

### Failure Handling
Malformed criteria are reported instead of silently converted into requirements.

### Human Review
A user or qualified navigator should compare the criteria with current agency guidance.

## Tool: screen-eligibility

### Inputs and Data Sources
Receives normalized criteria and applicant facts supplied by the user.

### Decision and Reasoning
Uses deterministic comparisons and labels unprovided or ambiguous facts as unknown.

### Outputs and Evidence
Returns a status and the fact or criterion description used to support each result.

### Limits and Constraints
It does not estimate approval probability or make an official determination.

### Failure Handling
Missing facts remain unknown; invalid criteria are flagged.

### Human Review
Confirm all findings with the responsible program administrator.

## Tool: prepare-application-checklist

### Inputs and Data Sources
Receives a program name, known criteria, and any documents already identified by the user or program material.

### Decision and Reasoning
Builds a checklist from explicitly supplied documents and unresolved questions.

### Outputs and Evidence
Returns items to verify before applying.

### Limits and Constraints
It does not assert that a document is officially required unless the input says so.

### Failure Handling
When document requirements are absent, it generates questions to ask the agency rather than inventing a list.

### Human Review
Check the official application instructions before submitting documents.

## Privacy and Uncertainty
Collect only information necessary for a preliminary screen. Avoid storing personal records. Unknown information must remain unknown rather than being guessed.

## Auditability
Keep a copy of the source program criteria and the screening output if a user needs to review how a result was produced.
