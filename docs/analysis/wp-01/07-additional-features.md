# WP-01.7 – Weitere Funktionen

| Funktion | LSS-Indiz | Einstufung | Entscheidung |
|---|---|---|---|
| Survey-/Gruppeneinstellungen | `surveys`, `groups`, L10n | Version 1 und umfassender Converter | vollständig roh + typisiert |
| Mehrsprachigkeit | `languages`, `*_l10ns` | Version 1 | erforderlich |
| Quoten | optional `quotas*`-Bereiche | umfassender Converter | zunächst Rohdaten, später typisiert |
| Conditions | optional `conditions` | umfassender Converter | strukturierte Daten + Relevance |
| Bewertungen | `assessments`/Attribute | umfassender Converter | nicht mit normalem Antwortwert verwechseln |
| Teilnehmerattribute/Token | optional `participant_*`, Tokenbereiche | abhängig von Produktentscheidung | Datenschutzprüfung nötig |
| Plugins | `plugin_settings` | optional | nur bekannte Settings typisieren |
| Themes/Ressourcen | `themes`, `themes_inherited`, Ressourcen | optional | Referenzen und Originalwerte bewahren |
| Berechtigungen | optional Permissions | optional | nicht in Excel als lokale Benutzerrechte simulieren |
| Antworten | keine Response-Daten im Survey-LSS | nicht Bestandteil | nicht in Autorenmodell aufnehmen |

Die Referenz enthält fünf `plugin_settings`-Zeilen, aber keine Quoten,
Conditions, Teilnehmerattribute, Berechtigungs- oder Ressourcenbereiche.
`themes` und `themes_inherited` sind vorhanden, aber leer. Das zeigt, dass
leere optionale Bereiche normal sind.

## Grenzen

Ein LSS-Surveyexport beschreibt Survey-Struktur und Einstellungen, nicht
notwendigerweise installierte Plugins, externe Dateien, Benutzerkonten oder
Antwortdatensätze. Ein Converter darf solche Daten nicht erfinden. Für
nicht übertragbare Elemente ist eine Warnung mit Original-XML der sichere
Fallback.

Quellen: [LimeSurvey repository](https://github.com/LimeSurvey/LimeSurvey),
[Survey model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Survey.php).
