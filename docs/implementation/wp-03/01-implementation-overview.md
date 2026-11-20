# WP-03 – Implementierungsübersicht

WP-03 implementiert das adapterunabhängige Fundament unter `src/limex/`.
Es verwendet Python-Standardbibliothek-Dataclasses mit `slots=True` und
keine externe Laufzeitabhängigkeit. Dataclasses sind hier ausreichend
explizit, testbar und verwerfen keine unbekannten Rohdaten; Validierung
erfolgt separat.

Enthalten sind Zustände, Domänenentitäten, Raw-Tabellen, stabile Referenzen,
Schema-Version und Integritätsvalidierung. Nicht enthalten sind LSS-/XLSX-
Adapter, CLI und produktive Konvertierung.
