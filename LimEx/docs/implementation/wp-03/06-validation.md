# WP-03 – Validierung

`validate_survey` liefert `ValidationResult` mit Fehlern und Warnungen.
Geprüft werden doppelte IDs/Codes, Survey-/Gruppen-/Fragebeziehungen,
Elternreferenzen, Antwortbeziehungen, Skalenbezüge und Condition-
Referenzen. Ein Konflikt zwischen Conditions und vorhandener Relevance ist
eine Warnung, weil beide Daten bewusst erhalten bleiben.

Unbekannte Attribute und Rohfelder sind keine Fehler. Adapter können später
zusätzliche typabhängige Regeln ergänzen.
