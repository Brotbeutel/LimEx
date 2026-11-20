# WP-02.8 – Versionierung und Kompatibilität

## Vier Versionen

`workbook_schema_version` beschreibt Spalten, Zustände und Tabellen.
`converter_version` beschreibt das Programm. `target_limesurvey_range`
beschreibt den beabsichtigten LS6-Kompatibilitätsbereich. `metadata_source`
enthält Herkunft und Version von Theme-/Plugin-Definitionen.
`DBVersion=651` ist nur Export-/Datenbankmetadatum und kein exakter
Serverbuild.

## Speicherort und Erkennung

Alle vier Werte stehen in `START` sowie in einer technischen Workbook-
Eigenschaft. Der Import liest sie vor den fachlichen Tabellen. Fehlt die
Schema-Version, wird nur ein ausdrücklich unterstützter Legacy-Modus
angeboten; unbekannte Major-Versionen werden abgelehnt, unbekannte Minor-
Versionen als Warnung behandelt.

## Migration

Migrationen sind explizite, versionierte Schritte außerhalb des Workbooks.
Sie erstellen zunächst eine Kopie, protokollieren Änderungen und bewahren
Rohwerte. Automatische Migration ist in WP-02 nur entworfen, nicht
implementiert. Inkompatible Änderungen an Identitäten, Zuständen oder
Referenzen erfordern eine neue Major-Version.

## LimeSurvey-Zielversion

Die konkrete LS6-Version bleibt offen. Ein späterer Adapter muss Zielversion,
Quellcommit und Metadatenquelle beim Lauf dokumentieren. Ohne Zielinstallation
ist ein LSS-Import zulässig; Exportfunktionen, die installierte Themes oder
Plugins voraussetzen, werden als Warnung bzw. raw-only markiert.
