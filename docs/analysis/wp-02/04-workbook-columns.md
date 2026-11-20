# WP-02.4 – Spaltendefinitionen

## Allgemeine Konvention

Jede Zeile hat `stable_id` (Pflicht, technisch), `source_id` (optional),
`row_state` (`active`/`deleted`) und `notes` (optional). Technische IDs sind
für Einsteiger verborgen, aber nicht unzugänglich. Pflichtwerte werden durch
Tabellenvalidierung und Warnfarben geprüft; Excel-Validierung ersetzt keine
fachliche Prüfung.

## `Quiz`

| Technischer Name | Anzeige | Typ | Pflicht/Default | Validierung |
|---|---|---|---|---|
| `survey_key` | Survey-Schlüssel | Text | ja | eindeutig |
| `title` | Titel | Text/mehrzeilig | ja | nicht missing |
| `base_language` | Basissprache | Auswahl | ja | ISO-Code aus `Sprachen` |
| `description` | Beschreibung | Text/HTML | nein | roh bewahren |
| `anonymized` | Anonymisiert | Auswahl | nein | `Y/N` |
| `format` | Navigationsformat | Auswahl | nein | `A/G/Q/I` |
| `startdate`/`expires` | Start/Ende | Datum/Zeit/Text | nein | LimeSurvey-Format |

## `Gruppen`

`stable_id`, `group_code`, `name_ref`, `description_ref`, `group_order`,
`randomization_group`, `relevance`, `relevance_state`, `source_id`.
`group_order` ist Integer >= 0; `randomization_group` ist Text; Relevance
ist unveränderte Expression. `group_code` ist innerhalb des Surveys eindeutig.

## `Fragen`

`stable_id`, `question_code`, `group_ref`, `parent_ref`, `type`,
`question_order`, `text_ref`, `help_ref`, `mandatory`, `hidden`,
`relevance`, `random_group`, `answer_order`, `other`, `encrypted`,
`question_theme`, `source_id`, `raw_state`.

`type` ist der bekannte LimeSurvey-Code oder `unknown`; `mandatory` erlaubt
`Y/S/N`; `hidden` ist `Y/N`; `question_order` ist Integer. `hidden`,
`relevance`, `random_group` und `answer_order` werden bewusst separat
validiert.

## `Antworten` und `Unterfragen`

`Antworten`: `stable_id`, `question_ref`, `code`, `sortorder`,
`assessment_value`, `scale_id`, `text_ref`, `source_id`.

`Unterfragen`: dieselben Identitäts-/Textfelder wie Fragen plus
`parent_ref`, `scale_id`, `question_order`. Codes müssen je Elternfrage und
Skala eindeutig sein.

## `Sprachen` und `Übersetzungen`

`Sprachen`: `code`, `is_base`, `display_name`, `source_state`.
`Übersetzungen`: `stable_id`, `entity_type`, `entity_ref`, `language`,
`text_kind`, `text`, `text_state`, `source_id`. `text_kind` unterscheidet
Titel, Beschreibung, Hilfe, Script, Antwort und Mailtext.

## `Attribute`, `Bedingungen`, technische Blätter

`Attribute`: `question_ref`, `attribute`, `value`, `value_state`,
`language`, `data_type`, `definition_source`, `support_status`, `raw_value`.

`Bedingungen`: `stable_id`, `target_ref`, `group_ref`, `left_ref`,
`operator`, `right_value`, `join_operator`, `parent_condition_ref`,
`condition_state`, `raw_expression`.

`Technische Daten`: `entity_type`, `stable_id`, `source_id`, `target_id`,
`mapping_status`, `source_table`, `source_row_order`.

`Rohdaten`: `raw_id`, `table_name`, `row_order`, `field_order`, `field_name`,
`state`, `raw_value`, `chunk_ref`, `support_status`, `export_policy`.

## Eingabeformeln und große Inhalte

Textfelder werden beim XLSX-Schreiben als Text behandelt; Werte mit
`=`, `+`, `-` oder `@` bekommen eine sichere Excel-Textdarstellung.
Der ursprüngliche Rohwert bleibt separat erhalten. Inhalte über 32.767
Zeichen werden in `RAW_CHUNKS` ausgelagert; die sichtbare Projektion zeigt
eine Warnung und eine Referenz.
