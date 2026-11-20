# WP-02 – Abschlussbericht

## Wesentliche Entscheidungen

Das Workbook erhält einen hybriden Raw-XML-Layer: technische Tabellen und
Mappingdaten liegen im Workbook, ein Sidecar ist optional. Das Modell
unterscheidet `missing`, `empty`, `value` und bewusstes `deleted`.
Beziehungen verwenden stabile interne IDs; LimeSurvey-IDs und fachliche
Codes bleiben getrennt. Unbekannte Daten werden roh erhalten und nicht
stillschweigend verworfen.

Das sichtbare Workbook hat Kernblätter für Survey, Sprachen, Gruppen,
Fragen, Antworten, Unterfragen und Übersetzungen sowie Expertenblätter für
Attribute, Conditions, technische Daten und Rohdaten. Die zentrale
Fragentabelle trennt `hidden`, `relevance`, `random_group` und
`answer_order`.

## Konsistenz

Das interne Modell und das Workbook teilen dieselben Entitäten, Referenzen,
Zustände, Sprachcodes und Rohwertregeln. Excel-Zeilensortierung ist nur
Darstellung. Attribute werden zeilenförmig und installationsabhängig
modelliert; Definitionen können später dynamisch importiert werden.

## Bewusst offen

Offen bleiben Zielcommit/Version von LimeSurvey 6, endgültige Python-
Validierungsbibliothek, die genaue ExpressionScript-Referenzauflösung und
Zusatzexports für Quoten, Conditions, Unterfragen, Ressourcen, Plugins und
Mehrfachsprachen. Dafür sind zusätzliche Referenzdateien erforderlich.

## Risiken

Excel-Zellgrenzen, Formelinjektion, versehentliche Änderungen technischer
Blätter, unvollständige Theme-Metadaten und Konflikte zwischen Conditions
und Relevance können Roundtrips gefährden. Deshalb sind Warnungen,
Rohbewahrung und explizite Exportvalidierung vorgesehen.

## Empfehlung für WP-03

WP-03 kann mit einem kleinen neutralen Dokument-/Domänenmodell und
Roundtrip-Testfixtures beginnen, aber noch nicht mit einer Behauptung
vollständiger LimeSurvey-Funktionalität. Zuerst sollten die in der
[Feature-Matrix](09-feature-and-roundtrip-matrix.md) genannten
Referenzexports ergänzt und die Schema-Version initial festgelegt werden.
Produktive Adapter und XLSX-Erzeugung bleiben nachgelagert.
