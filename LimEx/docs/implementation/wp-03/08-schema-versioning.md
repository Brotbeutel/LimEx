# WP-03 – Schema-Versionierung

`src/limex/version.py` definiert `WORKBOOK_SCHEMA_VERSION = "1.0.0"`.
Spätere Workbook-Adapter sollen denselben Wert in `START` und technischen
Workbook-Metadaten lesen. Unbekannte Major-Versionen sind inkompatibel;
Minor-/Patch-Versionen können nur nach expliziter Kompatibilitätsprüfung
akzeptiert werden.

WP-03 erzeugt noch kein Workbook und implementiert keine Migration.
