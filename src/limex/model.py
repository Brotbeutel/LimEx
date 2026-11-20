"""Neutral domain entities; no XML or spreadsheet concerns belong here."""

from dataclasses import dataclass, field
from typing import Optional

from .state import Value


@dataclass(slots=True)
class Language:
    stable_id: str
    code: str
    source_id: Optional[str] = None
    display_name: Value[str] = field(default_factory=Value.missing)
    is_base: bool = False


@dataclass(slots=True)
class Attribute:
    stable_id: str
    question_ref: str
    name: str
    raw_value: Value[str]
    language: Optional[str] = None
    definition_ref: Optional[str] = None
    definition_source: Optional[str] = None
    support_status: str = "unknown"


@dataclass(slots=True)
class Answer:
    stable_id: str
    question_ref: str
    code: str
    sortorder: Optional[int] = None
    assessment_value: Optional[str] = None
    scale_id: Optional[str] = None
    source_id: Optional[str] = None
    localized_text: dict[str, Value[str]] = field(default_factory=dict)


@dataclass(slots=True)
class Subquestion:
    stable_id: str
    parent_ref: str
    code: str
    question_order: Optional[int] = None
    scale_id: Optional[str] = None
    source_id: Optional[str] = None
    localized_text: dict[str, Value[str]] = field(default_factory=dict)


@dataclass(slots=True)
class Condition:
    stable_id: str
    target_ref: str
    left_ref: Optional[str] = None
    operator: Optional[str] = None
    right_value: Optional[str] = None
    join_operator: Optional[str] = None
    parent_ref: Optional[str] = None
    raw_expression: Value[str] = field(default_factory=Value.missing)
    references: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Question:
    stable_id: str
    code: str
    group_ref: str
    type: str
    source_id: Optional[str] = None
    parent_ref: Optional[str] = None
    question_order: Optional[int] = None
    hidden: Value[str] = field(default_factory=Value.missing)
    relevance: Value[str] = field(default_factory=Value.missing)
    random_group: Value[str] = field(default_factory=Value.missing)
    answer_order: Value[str] = field(default_factory=Value.missing)
    localized_text: dict[str, Value[str]] = field(default_factory=dict)
    answers: list[Answer] = field(default_factory=list)
    subquestions: list[Subquestion] = field(default_factory=list)
    attributes: list[Attribute] = field(default_factory=list)
    conditions: list[Condition] = field(default_factory=list)


@dataclass(slots=True)
class Group:
    stable_id: str
    survey_ref: str
    code: str
    group_order: Optional[int] = None
    source_id: Optional[str] = None
    relevance: Value[str] = field(default_factory=Value.missing)
    localized_text: dict[str, Value[str]] = field(default_factory=dict)
    question_refs: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Survey:
    stable_id: str
    key: str
    source_id: Optional[str] = None
    languages: list[Language] = field(default_factory=list)
    groups: list[Group] = field(default_factory=list)
    questions: list[Question] = field(default_factory=list)
    settings: dict[str, Value[str]] = field(default_factory=dict)
    conditions: list[Condition] = field(default_factory=list)
