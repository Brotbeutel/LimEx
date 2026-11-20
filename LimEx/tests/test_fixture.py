from pathlib import Path
import xml.etree.ElementTree as ET


FIXTURE = Path(__file__).parent / "fixtures" / "limesurvey_survey_154993.lss"


def _rows(root, name):
    section = root.find(name)
    fields = [node.text for node in section.findall("./fields/fieldname")]
    return [
        {field: row.findtext(field) if row.find(field) is not None else None for field in fields}
        for row in section.findall("./rows/row")
    ]


def test_reference_fixture_observed_counts():
    root = ET.parse(FIXTURE).getroot()
    assert root.tag == "document"
    assert root.findtext("LimeSurveyDocType") == "Survey"
    assert root.findtext("DBVersion") == "651"
    assert [node.text for node in root.findall("./languages/language")] == ["de"]
    assert len(_rows(root, "questions")) == 20
    assert {row["type"] for row in _rows(root, "questions")} == {"L"}
    assert len(_rows(root, "answers")) == 80
    assert len(_rows(root, "question_l10ns")) == 20
    assert len(_rows(root, "question_attributes")) == 840
    assert len(_rows(root, "plugin_settings")) == 5
    assert len(_rows(root, "themes")) == 0
    assert len(_rows(root, "themes_inherited")) == 0
