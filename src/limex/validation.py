"""Adapter-independent integrity checks for the neutral model."""

from dataclasses import dataclass, field

from .model import Survey
from .state import ValueState


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    message: str
    path: str
    severity: str = "error"


@dataclass(slots=True)
class ValidationResult:
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "warning"]

    @property
    def valid(self) -> bool:
        return not self.errors


def _duplicate(values: list[str]) -> set[str]:
    return {value for value in values if values.count(value) > 1}


def validate_survey(survey: Survey) -> ValidationResult:
    result = ValidationResult()
    groups = {group.stable_id: group for group in survey.groups}
    questions = {question.stable_id: question for question in survey.questions}

    if len(groups) != len(survey.groups):
        result.issues.append(ValidationIssue("duplicate-id", "duplicate group stable_id", "groups"))
    if len(questions) != len(survey.questions):
        result.issues.append(ValidationIssue("duplicate-id", "duplicate question stable_id", "questions"))
    for code in _duplicate([group.code for group in survey.groups]):
        result.issues.append(ValidationIssue("duplicate-code", f"duplicate group code {code}", "groups"))
    for code in _duplicate([question.code for question in survey.questions]):
        result.issues.append(ValidationIssue("duplicate-code", f"duplicate question code {code}", "questions"))

    for group in survey.groups:
        if group.survey_ref != survey.stable_id:
            result.issues.append(ValidationIssue("wrong-parent", "group does not reference survey", group.stable_id))
        for ref in group.question_refs:
            if ref not in questions:
                result.issues.append(ValidationIssue("unresolved-reference", "unknown question reference", ref))

    for question in survey.questions:
        if question.group_ref not in groups:
            result.issues.append(ValidationIssue("unresolved-reference", "question group is missing", question.stable_id))
        if question.parent_ref is not None and question.parent_ref not in questions:
            result.issues.append(ValidationIssue("missing-parent", "question parent is missing", question.stable_id))
        answer_codes = [answer.code for answer in question.answers]
        for code in _duplicate(answer_codes):
            result.issues.append(ValidationIssue("duplicate-code", f"duplicate answer code {code}", question.stable_id))
        answer_ids = [answer.stable_id for answer in question.answers]
        if len(set(answer_ids)) != len(answer_ids):
            result.issues.append(ValidationIssue("duplicate-id", "duplicate answer stable_id", question.stable_id))
        for answer in question.answers:
            if answer.question_ref != question.stable_id:
                result.issues.append(ValidationIssue("wrong-parent", "answer does not reference question", answer.stable_id))
            if answer.scale_id is not None and not any(
                sub.scale_id == answer.scale_id for sub in question.subquestions
            ) and question.subquestions:
                result.issues.append(ValidationIssue("invalid-scale", "answer scale is not used by subquestions", answer.stable_id))
        for condition in [*question.conditions, *survey.conditions]:
            if condition.target_ref not in questions and condition.target_ref != survey.stable_id:
                result.issues.append(ValidationIssue("unresolved-condition", "condition target is unknown", condition.stable_id))
            for ref in condition.references:
                if ref not in questions:
                    result.issues.append(ValidationIssue("unresolved-condition", "condition reference is unknown", ref))
        for field_name in ("hidden", "relevance", "random_group", "answer_order"):
            value = getattr(question, field_name)
            if not isinstance(value.state, ValueState):
                result.issues.append(ValidationIssue("invalid-state", f"{field_name} has invalid state", question.stable_id))
        if question.conditions and question.relevance.state == ValueState.VALUE:
            result.issues.append(ValidationIssue(
                "logic-conflict",
                "structured conditions and relevance are both present",
                question.stable_id,
                "warning",
            ))
    return result
