# WP-02.3 – Workbook-Struktur

## Blätter

| Blatt | Zweck | Einsteiger | Bearbeitung |
|---|---|---:|---|
| `START` | Anleitung, Version, Warnungen, Beispiele | sichtbar | begrenzt |
| `Quiz` | Survey-Kern und Basissprache | sichtbar | ja |
| `Sprachen` | Sprachcodes und Basissprache | sichtbar | ja |
| `Gruppen` | Gruppen, Reihenfolge, Relevanz | sichtbar | ja |
| `Fragen` | zentrale Frageprojektion | sichtbar | ja |
| `Antworten` | Antwortoptionen/Skalen | sichtbar | ja |
| `Unterfragen` | Matrix-/Unterfragen | sichtbar | ja |
| `Übersetzungen` | lokalisierte Texte | sichtbar | ja |
| `Attribute` | erweiterte Attribute mit Metadaten | Experten | ja |
| `Bedingungen` | strukturierte Conditions | Experten | ja |
| `Weitere Einstellungen` | typisierte Zusatzbereiche | Experten | ja |
| `Technische Daten` | IDs, Versionen, Mapping | Experten | vorsichtig |
| `Rohdaten` | unbekannte Tabellen/Felder | Experten | ja |

Jedes Blatt hat eine Excel-Tabelle mit stabilen Spaltennamen. Beziehungen
verwenden `stable_id` oder einen sichtbaren fachlichen Schlüssel, niemals
Zeilennummern. `Technische Daten` und `Rohdaten` werden standardmäßig
ausgeblendet, aber nicht als Sicherheitsmaßnahme geschützt.

## Bedienkonzept

Einsteiger bearbeiten `Quiz`, `Gruppen`, `Fragen`, `Antworten`,
`Unterfragen`, `Sprachen` und häufige `Übersetzungen`. Experten blenden
Attribute, Bedingungen und Rohdaten ein. Anzeigenamen sind deutsch,
technische Namen stehen in Kopfkommentaren/Hilfetexten. Fixierte
Kopfzeilen, Filter, Tabellenformat und bedingte Warnfarben sind verbindlich.

## Redundanzregeln

Fragetext steht zentral in `Übersetzungen`, `Fragen` enthält nur den
Default-/Übersetzungszeiger. Häufige Frageeigenschaften werden in `Fragen`
projektiert; die vollständige Menge bleibt in `Attribute`. Antworttexte
stehen zentral in `Übersetzungen` mit `entity_type` und `entity_ref`.

## Workbook-Metadaten

`START` enthält `workbook_schema_version`, `converter_version`,
`target_limesurvey_range`, `source_format`, `metadata_source` und
`created_at`. Ein Import muss diese Werte lesen, bevor fachliche Tabellen
interpretiert werden.
