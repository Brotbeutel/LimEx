# WP-02.9 – Feature- und Roundtrip-Matrix

Legende: `verified` = in der Referenz beobachtet; `designed` = Schema
entworfen; `raw-preservation-only` = nur Rohbewahrung vorgesehen;
`requires-reference-test` = weitere LSS-Datei nötig; `unknown` = Semantik
noch offen.

| Bereich | LSS | Modell | Excel | Rohdaten | Export | Status |
|---|---|---|---|---|---|---|
| Survey-Einstellungen | ja | ja | ja | ja | entworfen | verified |
| Gruppen | ja | ja | ja | ja | entworfen | verified |
| Fragen | ja | ja | ja | ja | entworfen | verified |
| 29 Kern-Fragetypen | teilweise | ja | ja | ja | typabhängig | requires-reference-test |
| Frageattribute | ja | Projektion + roh | ja | ja | entworfen | verified/unknown |
| Antworten | ja | ja | ja | ja | entworfen | verified |
| Unterfragen | möglich | ja | ja | ja | entworfen | requires-reference-test |
| Mehrfachskalen | möglich | ja | ja | ja | entworfen | requires-reference-test |
| Übersetzungen | ja | ja | ja | ja | entworfen | verified |
| Relevance | ja | ja | ja | ja | entworfen | verified |
| Conditions | optional | ja | Experten | ja | konfliktabhängig | requires-reference-test |
| Quoten | optional | raw | nein/Experte | ja | raw | requires-reference-test |
| Teilnehmerattribute | optional | raw | nein/Experte | ja | raw | requires-reference-test |
| Berechtigungen | optional | raw | nein | ja | raw | requires-reference-test |
| Ressourcen | optional | raw | nein | ja | raw | requires-reference-test |
| Plugins | `plugin_settings` | raw + Metadaten | Experten | ja | bedingt | verified/raw-only |
| Theme-Daten | optional | raw + Metadaten | Experten | ja | bedingt | requires-reference-test |
| Unbekannte XML-Bereiche | möglich | raw | Experten | ja | Policy | designed |

Die Referenz verifiziert nur das tatsächliche Vorkommen: `de`, 20 `L`-Fragen,
Antworten, L10n, Attribute, Survey-/Gruppenbereiche, Plugin-Settings und
leere Theme-Bereiche. Sie verifiziert nicht die Fähigkeiten leerer oder
fehlender Bereiche.

Benötigte Zusatzreferenzen: Unterfrage/Array, duale Skala, Conditions,
mehrsprachiger Survey, Quote, Token/Teilnehmerattribute, Plugin/Theme,
Ressourcen und unbekannte Tabellen/Felder.
