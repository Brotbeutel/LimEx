from limex import (
    Answer,
    Attribute,
    Condition,
    Group,
    Question,
    RawField,
    RawRow,
    RawTable,
    Survey,
    Value,
    ValueState,
    validate_survey,
)


def test_value_states_are_distinct():
    assert Value.missing().state == ValueState.MISSING
    assert Value.empty().state == ValueState.EMPTY
    assert Value.value("").state == ValueState.EMPTY
    assert Value.value("0").raw == "0"
    assert Value.deleted().state == ValueState.DELETED
    assert Value.missing() != Value.empty()
    assert Value.empty() != Value.value("0")
    try:
        Value(ValueState.VALUE)
    except ValueError:
        pass
    else:
        raise AssertionError("value without raw content must be rejected")


def test_stable_and_source_ids_are_separate():
    answer = Answer("answer-stable", "question-stable", "A", source_id="6181")
    assert answer.stable_id == "answer-stable"
    assert answer.source_id == "6181"


def test_unicode_html_and_multiline_values_are_unchanged():
    text = "Grüße <strong>世界</strong>\n<script>const x = 1;</script>"
    assert Value.value(text).raw == text


def test_references_survive_reordering():
    group = Group("group-1", "survey-1", "g1")
    first = Question("question-1", "q1", group.stable_id, "L")
    second = Question("question-2", "q2", group.stable_id, "L")
    group.question_refs = [first.stable_id, second.stable_id]
    survey = Survey("survey-1", "quiz", groups=[group], questions=[second, first])
    assert validate_survey(survey).valid
    assert group.question_refs == ["question-1", "question-2"]


def test_unknown_attribute_and_raw_fields_are_preserved():
    attribute = Attribute("attribute-1", "question-1", "plugin_setting", Value.value("未知"))
    field = RawField("new_field", Value.value("HTML <b>x</b>"), 0)
    raw = RawTable("unknown_table", 3, ["new_field"], [RawRow(0, [field])])
    assert attribute.raw_value.raw == "未知"
    assert raw.known is False
    assert raw.rows[0].fields[0].value.raw == "HTML <b>x</b>"


def test_logic_properties_are_separate():
    question = Question(
        "question-1", "q1", "group-1", "L",
        hidden=Value.value("Y"),
        relevance=Value.value("q0 == 'Y'"),
        random_group=Value.value("rg"),
        answer_order=Value.value("random"),
    )
    assert {question.hidden.raw, question.relevance.raw, question.random_group.raw, question.answer_order.raw} == {
        "Y", "q0 == 'Y'", "rg", "random"
    }


def test_conditions_and_relevance_are_separate():
    question = Question(
        "question-1", "q1", "group-1", "L",
        relevance=Value.value("q0 == 'Y'"),
        conditions=[Condition("condition-1", "question-1", references=["question-0"])],
    )
    survey = Survey("survey-1", "quiz", questions=[question])
    result = validate_survey(survey)
    assert any(issue.code == "logic-conflict" for issue in result.warnings)


def test_validation_detects_relationship_errors():
    question = Question("question-1", "q1", "missing-group", "L")
    question.answers.append(Answer("answer-1", "other-question", "A"))
    survey = Survey("survey-1", "quiz", questions=[question])
    result = validate_survey(survey)
    assert not result.valid
    assert {issue.code for issue in result.errors} >= {"unresolved-reference", "wrong-parent"}
