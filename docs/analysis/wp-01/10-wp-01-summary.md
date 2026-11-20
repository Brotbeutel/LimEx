# WP-01 – Abschlussbericht

## Ergebnis

Das LSS ist ein XML-Dokument mit `<document>` als Wurzel und tabellenartigen
`fields`/`rows`-Bereichen. Die Referenz ist `Survey`, `DBVersion=651`,
deutschsprachig, hat 20 `L`-Fragen, 80 Antworten und 840 Attribute.
Survey-, Gruppen-, Frage-, Antwort-, Übersetzungs- und Attributdaten sind über
technische IDs verbunden; lokalisierte Texte liegen in eigenen Bereichen.

## Was das interne Modell zwingend braucht

Survey- und Gruppenmetadaten, Fragen mit Elternbeziehungen, Fragecodes und
Relevance, lokalisierte Texte, Antworten mit Codes/Sortierung/Skala,
Attribute als typisierte Projektion plus Roh-Key/Rohwert, Sprachcodes,
technische ID-Mappings und optionale/unbekannte XML-Bereiche. Außerdem muss
der Dokumentlayer fehlende, leere und gesetzte Felder unterscheiden.

## Fragetypen und Logik

LimeSurvey 6 kennt 29 Kerncodes (Arrays, Auswahl, Text, Datum, Upload,
Equation und Matrizen). Die Referenz deckt nur `L` ab. `relevance` ist
ExpressionScript; Conditions sind eine alternative strukturierte
Editor-Darstellung und müssen bei Export/Import konsistent behandelt werden.
`hidden`, `answer_order` und `random_group` sind unabhängige Konzepte.

## Datenverlust

Das größte Risiko liegt nicht in XML, sondern in einer zu stark typisierten
Excel-Zwischendarstellung: HTML/JavaScript, CDATA, Whitespace,
Mehrsprachigkeit, Attribute, IDs und unbekannte Bereiche würden sonst
verändert. Rohdaten müssen deshalb neben nutzerfreundlichen Excel-Feldern
existieren.

## Empfehlung für WP-02

**Ja, als Entwurf kann WP-02 beginnen**, sofern die offenen Entscheidungen aus
[09-open-questions-and-decisions.md](09-open-questions-and-decisions.md)
als Annahmen dokumentiert werden. Für eine Behauptung vollständiger
Roundtrip-Unterstützung ist die Analyse noch nicht abschließend: Es fehlen
Referenzexports mit Conditions, Quoten, Unterfragen/Mehrfachskalen,
Teilnehmerdaten, Ressourcen und mehreren Sprachen sowie ein festgelegter
LimeSurvey-6-Zielcommit.

## Quellen

* [LimeSurvey question types](https://www.limesurvey.org/manual/Question_types)
* [ExpressionScript presentation](https://www.limesurvey.org/manual/ExpressionScript_-_Presentation)
* [Conditions](https://www.limesurvey.org/manual/Setting_conditions)
* [Question.php](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Question.php)
* [QuestionAttribute.php](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/QuestionAttribute.php)
* [questionHelper.php](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/helpers/questionHelper.php)
* [Survey.php](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Survey.php)
