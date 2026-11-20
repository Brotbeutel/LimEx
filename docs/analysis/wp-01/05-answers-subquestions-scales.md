# WP-01.4 – Antworten, Unterfragen und Skalen

## Antwortoptionen

`answers` enthält `aid`, `qid`, `code`, `sortorder`, `assessment_value` und
`scale_id`. `answer_l10ns` enthält `id`, `aid`, `answer` und `language`.
Der Antwortcode ist der stabile fachliche Schlüssel innerhalb einer Frage;
`aid` ist die technische ID. `sortorder` ist nicht zwingend der Datei-
oder ID-Reihenfolge vorzuziehen.

Die Referenz enthält 80 Antworten und 80 Übersetzungen. `scale_id=0` wird
verwendet; `assessment_value` ist separat vom Antworttext und darf nicht als
Boolean interpretiert werden.

## Unterfragen

Unterfragen werden in `questions` gespeichert. `parent_qid` verweist auf die
Elternfrage, `title` ist der Unterfragen-Code, `question_order` ordnet sie
innerhalb der Elternfrage, `scale_id` wählt bei dualen/flexiblen Strukturen
die Achse. Text und Hilfe kommen aus `question_l10ns`. Deshalb müssen
Unterfragen dieselben ID-, Sprach- und Rohtextregeln wie normale Fragen
erfüllen.

## Skalen

`scale_id` am Antwortsatz und an der Frage/Unterfrage unterscheidet mehrere
Antwortachsen. Typische Fälle sind eine gemeinsame Array-Skala, duale Skala
oder flexible Matrix. Ein separater Scale-Top-Level-Bereich ist in der
Referenz nicht vorhanden; Skalen sind über die IDs und Frageattribute
implizit modelliert.

## Beziehungen und Exportreihenfolge

1. Survey/Gruppe anlegen.
2. Elternfragen anlegen.
3. Unterfragen anlegen.
4. Antworten mit `qid` und `scale_id` anlegen.
5. Lokalisierungen und Attribute anlegen.

Für einen Roundtrip müssen externe IDs entweder erhalten oder über eine
Mapping-Tabelle referenziert werden. Nie darf ein Antwortcode durch eine
neu berechnete ID ersetzt werden.

Quellen: [Question model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Question.php),
[Question types manual](https://www.limesurvey.org/manual/Question_types).
