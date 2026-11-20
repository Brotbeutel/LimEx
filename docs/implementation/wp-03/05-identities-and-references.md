# WP-03 – Identitäten und Referenzen

`stable_id` ist die interne Identität, `source_id` die optionale originale
LimeSurvey-ID und `code` der fachliche Schlüssel. Beziehungen referenzieren
stabile IDs, niemals Excel-Zeilennummern. `Condition.references`,
`group.question_refs`, `Question.group_ref` und Elternreferenzen sind
explizite Strings.

Die Ziel-ID-Vergabe und ExpressionScript-Umschreibung bleiben Aufgabe
späterer Adapter. Unbekannte Expressions werden nicht verändert.
