# WP-01.9 – Offene Fragen und Entscheidungen

## Bereits entschieden

* Ziel ist LimeSurvey 6, LSS/XLSX und Python/CLI.
* HTML, JavaScript, Unicode und unbekannte Attribute müssen erhalten bleiben.
* `hidden`, Relevance und `random_group` werden getrennt modelliert.
* WP-01 implementiert keine Konvertierung.

## Offene technische Fragen

1. Welche konkrete LimeSurvey-6-Version/Commit ist Ziel? `DBVersion=651`
   identifiziert nicht eindeutig den Serverbuild.
2. Soll Excel unbekannte XML-Tabellen als geschütztes Rohblatt oder nur in
   einem Sidecar aufnehmen?
3. Wie werden Theme- und Plugin-Attribute aus der Zielinstallation
   bezogen, wenn sie nicht im LSS definiert sind?
4. Sollen Quoten, Teilnehmerattribute, Berechtigungen, Ressourcen und Plugins
   in Version 1 typisiert oder zunächst nur verlustfrei bewahrt werden?
5. Wie werden neu erzeugte IDs beim LSS-Export vergeben und referenziert?
6. Ist eine LSS-Datei mit Conditions, Quoten und mehreren Sprachen als
   zusätzliche Referenztestmenge verfügbar?
7. Welche Excel-Eingabevalidierung ist für HTML, Expressions und
   mehrzeilige Inhalte akzeptabel?

## Architekturentscheidungen vor WP-02

Vor dem Excel-Schema müssen ein Raw-XML-Layer, ein explizites
missing/empty/value-Modell, ID-Mappings und eine Unknown-Data-Policy
festgelegt werden. Ohne diese Entscheidungen ist „vollständig“ nicht
messbar. Die Attributdefinition muss aus LimeSurvey-Theme-/Plugin-Metadaten
abgeleitet werden, nicht aus einer handgepflegten Liste allein.

## Noch nicht verifiziert

Die Referenz belegt keine Quoten, Conditions, Teilnehmerattribute,
Berechtigungen, Ressourcen, Unterfragen, Mehrfachskalen oder nicht-deutschen
Übersetzungen. Diese Features sind durch Dokumentation/Quellcode plausibel,
aber für den konkreten Roundtrip noch mit Exportdateien zu testen.
