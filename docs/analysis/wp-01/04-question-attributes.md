# WP-01.5 – Frageattribute

## Speicher- und Registrierungsmodell

`question_attributes` ist eine EAV-Struktur: `qid`, `attribute`, `value`,
`language`. Der Wert ist als String gespeichert; Datentyp, Default, Optionen,
Min/Max, Mehrsprachigkeit und Gültigkeit kommen aus der Definition des
Question Themes. Der LimeSurvey-6-Code lädt allgemeine Attribute aus
Theme-`config.xml`, erweiterte Attribute aus dem Theme und kann Plugin-
Attribute ergänzen. Ein statischer, für alle Installationen gültiger Katalog
ist daher nicht möglich.

Die Referenz enthält bei jeder der 20 `L`-Fragen dieselben 42 Attribute:

`answer_order`, `array_filter`, `array_filter_exclude`, `array_filter_style`,
`cssclass`, `display_columns`, `em_validation_q`, `em_validation_q_tip`,
`hidden`, `hide_tip`, `image`, `keep_codes_order`, `other_comment_mandatory`,
`other_numbers_only`, `other_position`, `other_position_code`,
`other_replace_text`, `page_break`, `printable_help`, `public_statistics`,
`random_group`, `save_as_default`, `scale_export`, `statistics_graphtype`,
`statistics_showgraph`, `time_limit`, `time_limit_action`,
`time_limit_countdown_message`, `time_limit_disable_next`,
`time_limit_disable_prev`, `time_limit_message`, `time_limit_message_delay`,
`time_limit_message_style`, `time_limit_timer_style`, `time_limit_warning`,
`time_limit_warning_2`, `time_limit_warning_2_display_time`,
`time_limit_warning_2_message`, `time_limit_warning_2_style`,
`time_limit_warning_display_time`, `time_limit_warning_message`,
`time_limit_warning_style`.

## Katalog nach Funktion

| Kategorie | Attribute/Datentyp (typisch) | Relevanz |
|---|---|---|
| Sichtbarkeit | `hidden` (Boolean), `page_break` (Boolean) | verstecken bzw. Seitenumbruch |
| Reihenfolge | `answer_order`, `keep_codes_order` (Auswahl/Boolean) | Antwortreihenfolge, nicht Frage-Randomisierung |
| Frage-Randomisierung | `random_group` (String) | gemeinsame Randomisierungsgruppe |
| Darstellung | `cssclass`, `image`, `hide_tip`, `display_columns`, `display_rows` | HTML/CSS/Anzeige |
| Filter | `array_filter`, `array_filter_exclude`, `array_filter_style` (Expression/String) | Antwort-/Unterfragenfilter |
| Eingabe | `numbers_only`, `text_input_width`, `text_input_size`, `prefix`, `suffix` | typabhängige Eingabe |
| Validierung | `em_validation_q`, `em_validation_sq`, jeweilige `_tip` (Expression/HTML) | Gesamt-/Unterfragenvalidierung |
| Zeit | `time_limit`, `time_limit_action`, Warn-/Countdown-/Timer-Felder | Sekunden und UI-Aktionen |
| Bewertung | `assessment_value`, `public_statistics`, `statistics_*` | Score/Statistik |
| Auswahl/Other | `other_*`, `exclude_all_others*`, `category_separator` | Sonderantworten |
| Datum/Zahl | `date_min`, `date_max`, `equals_num_value` | Grenzen und Summen |
| Equation | `equation` (Expression) | gespeicherte Berechnung |
| Mehrsprachigkeit | `i18n`-definierte Attribute | `language` ist dann relevant |

Die Tabelle nennt Funktionsfamilien und keine Behauptung, dass jedes Mitglied
für jeden Typ gilt. Die offizielle Definition ist die Quelle für `types`,
`default`, `options`, `inputtype`, `min`, `max`, `i18n`, `readonly` und
Abhängigkeiten.

## Kritische Unterscheidungen

`answer_order` steuert die Reihenfolge/Randomisierung von Antworten (für
bestimmte Antworttypen); `random_group` gruppiert Fragen zur
Frage-Randomisierung. `hidden=1` entfernt eine Frage aus der Darstellung und
ist nicht dasselbe wie eine false `relevance`.

## Anforderungen

Das interne Modell muss unbekannte Attribute mit Originalschlüssel, Originalwert
und optionaler Sprache bewahren. Es muss zugleich typisierte Projektionen
anbieten, ohne Rohwerte zu überschreiben. Attribute aus Themes/Plugins sind
bei Import und Export dynamisch zu erkennen.

Quelle: [QuestionAttribute.php](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/QuestionAttribute.php),
[questionHelper.php](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/helpers/questionHelper.php).
