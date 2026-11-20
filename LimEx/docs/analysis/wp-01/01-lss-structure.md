# WP-01.1 – Struktur des LSS-Formats

## Status und Quellen

**Beobachtet** wurde die vollständige Referenzdatei `limesurvey_survey_154993 (1).lss`
(7.238 Zeilen, UTF-8). **Belegt** sind die allgemeinen Modell- und
Attributbeziehungen durch den LimeSurvey-6-Quellcode. Das LSS-Format ist ein
XML-Export, kein XML-Schema mit garantiert stabiler, versionsunabhängiger
Feldmenge.

## Wurzel und Metadaten

```xml
<document>
  <LimeSurveyDocType>Survey</LimeSurveyDocType>
  <DBVersion>651</DBVersion>
  <languages><language>de</language></languages>
  <... table ...>
</document>
```

Die Wurzel heißt `document`; es gibt keine Namespaces. `LimeSurveyDocType`
identifiziert den Export als Umfrage, `DBVersion` ist die Datenbank-/Exportversion
und darf nicht als LimeSurvey-Produktversion interpretiert werden. Die
Sprachliste enthält Codes, nicht Übersetzungstexte.

## Top-Level-Bereiche der Referenzdatei

| Bereich | Zeilen/Datensätze | Zweck |
|---|---:|---|
| `languages` | 1 | Surveysprachen (`de`) |
| `answers` | 80 | Antwortoptionen, über `aid`/`qid` |
| `answer_l10ns` | 80 | Antworttexte je Sprache |
| `groups` | 1 | Gruppenkerndaten |
| `group_l10ns` | 1 | Gruppentexte und lokalisierte Gruppensicht |
| `questions` | 20 | Fragen, Typen, Reihenfolge und Logik |
| `question_l10ns` | 20 | Fragetext, Hilfe und Skript je Sprache |
| `question_attributes` | 840 | Schlüssel-Wert-Attribute je Frage |
| `surveys` | 1 | globale Umfrageeinstellungen |
| `surveys_languagesettings` | 1 | Titel, Beschreibung, Mail- und Endtexte |
| `plugin_settings` | 5 | Plugin-spezifische Survey-Einstellungen |
| `surveys_groups` | 1 | Zuordnung zur Survey-Gruppe |
| `themes` | 0 | optionale Theme-Daten, hier leer |
| `themes_inherited` | 0 | geerbte Theme-Daten, hier leer |

Andere Exporte können zusätzlich unter anderem `conditions`, Quoten,
Teilnehmerattribute, Berechtigungen, Ressourcen oder Bewertungsdaten enthalten.
Ein Parser muss unbekannte Bereiche erhalten oder ausdrücklich melden.

## Tabellenkonvention

Jeder tabellarische Bereich besitzt:

```xml
<section>
  <fields><fieldname>...</fieldname></fields>
  <rows><row><field><![CDATA[value]]></field></row></rows>
</section>
```

Die Reihenfolge der `fieldname`-Elemente bestimmt die Spaltenzuordnung. Ein
`row` kann ein Feld auslassen; ein vorhandenes, leeres Element ist semantisch
nicht automatisch dasselbe wie ein fehlendes Element. Werte sind in der
Referenzdatei durchgehend CDATA-kodiert. CDATA ist eine XML-Darstellung:
die Zeichen `]]>` müssen beim Schreiben sicher behandelt werden; der Inhalt
darf nicht HTML-escaped, normalisiert oder getrimmt werden.

## Beziehungen

* `surveys.sid` ist der Fremdschlüssel für `groups.sid`, `questions.sid` und
  viele Einstellungen.
* `groups.gid` verbindet `questions.gid`, `group_l10ns.gid` und
  `surveys_groups.gid`.
* `questions.qid` verbindet `question_l10ns.qid`, `question_attributes.qid`
  und `answers.qid`.
* `questions.parent_qid` bildet Unterfragen als Fragenzeilen ab; `0` bedeutet
  keine Elternfrage.
* `answers.aid` verbindet `answer_l10ns.aid`; `answers.scale_id` unterscheidet
  Antwortskalen.
* Sprachabhängige Tabellen tragen einen `language`-Wert. IDs sind technische
  Referenzen und dürfen beim Roundtrip nicht als fachliche Codes verwendet
  werden.

## Parseranforderungen

Der spätere Parser soll XML-Ereignisse oder einen DOM sicher lesen, die
Feldreihenfolge prüfen, unbekannte Tabellen/Felder roh speichern und
`missing`, `empty` und `value` unterscheiden. Die semantische Konvertierung
gehört nicht in WP-01.

## Quellen

* [LimeSurvey Question model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Question.php)
* [LimeSurvey QuestionAttribute model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/QuestionAttribute.php)
* [LimeSurvey Survey model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Survey.php)
