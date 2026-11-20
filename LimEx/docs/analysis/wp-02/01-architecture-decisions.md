# WP-02.1 – Architekturentscheidungen

## Status

Dieses Dokument ist ein Entwurf, keine Implementierung. Begriffe wie
„muss“ beschreiben die spätere Architektur, nicht bereits vorhandenen Code.
Die Grundlage ist [WP-01](../wp-01/10-wp-01-summary.md).

## Entscheidung A1: hybrider Raw-XML-Layer

| Variante | Integrität | UX/Portabilität | Bewertung |
|---|---|---|---|
| Technische XLSX-Blätter | gut, aber Excel kann Werte ändern | geschlossen und portabel, für Einsteiger unübersichtlich | nicht allein ausreichend |
| Sidecar JSON/XML | sehr gut, große Inhalte möglich | zusätzliche Datei, Kopieren/Weitergeben fehleranfällig | als Debug-/Archivformat |
| Hybrid | beste Kombination | Workbook bleibt selbständig, Sidecar optional | **empfohlen** |

Das Workbook enthält verborgene technische Tabellen als vollständige
strukturierte Rohdarstellung. Ein optionaler Sidecar bewahrt zusätzlich
Original-XML oder sehr große Inhalte. Das Workbook ist die transportierbare
Arbeitsdatei; der Sidecar wird nie stillschweigend vorausgesetzt.

### Konkrete Raw-Struktur

`RAW_TABLES` enthält pro Zeile `raw_id`, `table_name`, `row_order`,
`field_order`, `field_name`, `state`, `raw_value`, `value_encoding`,
`source_path` und `export_policy`. `RAW_DOCUMENT` enthält Dokumenttyp,
DBVersion, XML-Kodierung, Top-Level-Reihenfolge und optional den Original-
Sidecar. Große Werte werden in `RAW_CHUNKS` mit `raw_id`, `chunk_order` und
Textfragmenten gespeichert; 32.767 Zeichen pro Excel-Zelle werden nicht
überschritten.

## Entscheidung A2: expliziter Zustandswert

Jeder Wert besteht logisch aus `{state, raw_value, typed_value}`:

* `missing`: Quelle enthält kein Feld;
* `empty`: Feld ist vorhanden, aber leer;
* `value`: Feld enthält Zeichen, auch `"0"`, `"N"` oder Whitespace;
* `deleted`: Benutzer markiert ein vorhandenes Feld bewusst zur Entfernung.

In typisierten Tabellen steht `state` in einer eigenen Spalte (beispielsweise
`text_state`). Ein leeres Excel-Feld bedeutet nicht automatisch `missing`;
Importe setzen den Zustand aus XML, neue Excel-Zeilen setzen standardmäßig
`value` oder verlangen eine explizite Auswahl. `deleted` ist nur in
technischen Tabellen erlaubt und wird vor dem Export validiert.

## Entscheidung A3: vier ID-Ebenen

1. `source_id`: originale LimeSurvey-ID, unverändert und optional.
2. `stable_id`: UUID/struktureller interner Schlüssel, unabhängig von Zeilen.
3. `business_key`: z. B. eindeutiger Fragecode oder Antwortcode.
4. `target_id`: beim Export neu vergebene Ziel-ID.

Beziehungen referenzieren ausschließlich `stable_id`; Excel-Zeilenpositionen
sind nie Schlüssel. `ID_MAP` speichert Entität, `stable_id`, `source_id`,
`target_id`, Quelle und Status. Referenzen in Expressions werden nicht per
String-Replacement geändert, sondern über eine noch zu definierende
Expression-Referenzauflösung; unbekannte Ausdrücke bleiben roh.

## Entscheidung A4: Unknown-Data-Policy

Unbekannte Tabellen, Felder, Attribute und Plugin-/Theme-Werte werden
verlustfrei in `RAW_*` erhalten, beim Import als `unknown` markiert und beim
Export unverändert übernommen, sofern keine abhängige ID geändert wurde.
Bekannte, verifizierte Kernfelder werden typisiert und bearbeitbar. Nur
`designed`-Funktionen dürfen als nutzerfreundliche Projektion erscheinen.
Nicht sicher rekonstruierbare Werte erzeugen einen Fehler oder eine
explizite Warnung, niemals einen stillen Default.

Attributmetadaten kommen optional aus einer Zielinstallation oder einem
exportierten Theme-/Plugin-Metadatenpaket: Name, Typ, Optionen, Default,
Min/Max, `i18n`, zulässige Typen und Readonly-Regeln. Ohne diese Quelle
bleibt der LSS-Import möglich; Attribute werden roh und als `unknown`
behandelt. Eine Metadatenquelle wird mit URL/Commit, Installationskennung
und Zeitstempel versioniert.

## Entscheidungsmatrix

Die Architektur priorisiert Roundtrip-Integrität vor komfortabler
Typisierung. Excel-Blattschutz ist nur UX, kein Sicherheitsmechanismus.
Alle technischen Tabellen sind einsehbar und für Experten bearbeitbar.
