# WP-02.5 – Fragen, Attribute und Antwortmodell

## Frageprojektion

Die sichtbare `Fragen`-Zeile enthält nur stabile, häufig benötigte
Eigenschaften. Der Typcode bleibt originalgetreu; unbekannte Codes werden
nicht in einen ähnlichen Typ umgewandelt. `parent_ref` und `scale_id`
modellieren Unterfragen und Mehrfachskalen, ohne für jeden Fragetyp ein
eigenes Blatt zu benötigen.

## Attribute

Attribute werden als Zeilen statt als Spalten modelliert:

`question_ref + attribute + language + value_state + raw_value`.

Die optionale Definition ergänzt Anzeigename, `inputtype`, Datentyp,
Optionen, Default, Min/Max, kompatible Typen, `i18n`, Readonly und
Herkunft. `support_status` lautet `verified`, `designed`, `raw-only` oder
`unknown`. Die Definition stammt bevorzugt aus LimeSurvey-Theme-/Plugin-
Metadaten; die WP-01-Fallbackliste wird nicht als vollständiger Installations-
katalog ausgegeben.

## Antworten/Unterfragen/Skalen

Antwortcodes sind fachliche Schlüssel, `aid` nur technische IDs.
`assessment_value` bleibt numerischer Rohwert. `scale_id` ist eine
unabhängige Achsenreferenz; Antwortreihenfolge kommt aus `sortorder` und
`answer_order`, nicht aus der Tabellenreihenfolge. Unterfragen sind
Fragezeilen mit `parent_ref` und können je Skala eigene Codes haben.

## Metadaten ohne Installation

Ein LSS-Import benötigt keine erreichbare LimeSurvey-Installation. Fehlen
Definitionen, werden Attribute mit Originalwert in `Rohdaten` und
`Attribute` übernommen, aber nicht als sicher validierbare Dropdowns
angeboten. Bei späterem Metadatenimport werden Definitionen anhand von
Attributname, Fragetyp und Theme gematcht; nicht passende Definitionen
bleiben roh.
