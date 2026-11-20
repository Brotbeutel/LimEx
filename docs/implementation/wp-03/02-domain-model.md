# WP-03 – Domänenmodell

`Survey` enthält Sprachen, Gruppen, Fragen, Einstellungen und Conditions.
`Group` referenziert Survey und Fragen. `Question` besitzt Code, Typ,
Gruppe, optionale Elternreferenz, Antworten, Unterfragen, Attribute und
Conditions. `Answer` referenziert eine Frage und behält Code, Quell-ID,
Sortierung und Skala. `Subquestion` ist eine eigenständige Entität mit
Eltern- und Skalenreferenz.

`Language`, `Attribute` und `Condition` sind unabhängig referenzierbar.
Alle Entitäten besitzen `stable_id`; `source_id` und Fachcodes sind getrennt.
Die Listenreihenfolge ist keine Identität.
