# WP-01.6 – Relevanz und Bedingungen

## Zwei Darstellungen derselben Logik

`questions.relevance` und `groups.grelevance` enthalten ExpressionScript-
Ausdrücke. Eine leere Expression bedeutet üblicherweise „keine zusätzliche
Bedingung“; die explizite Expression `1` ist dagegen ein vorhandener Wert.
Relevanz wird zur Anzeigeentscheidung ausgewertet, nicht als Sprungziel.

Der Conditions-Editor speichert strukturierte Bedingungen in einem
`conditions`-Bereich, sofern der Export sie enthält. LimeSurvey kann diese
Bedingungen in eine Relevanz-Expression überführen. Laut offizieller
Dokumentation sollen Conditions und manuell gepflegte Relevance nicht
gleichzeitig als unabhängige Wahrheiten behandelt werden: der Editor ersetzt
die Relevance-Expression.

## Unterstützte Ausdrücke

Vergleiche können Antworten, Konstanten und – abhängig von Datenschutz und
Survey-Einstellungen – Teilnehmerdaten verwenden. Operatoren umfassen
Gleichheit, Ungleichheit, numerische Vergleiche und reguläre Ausdrücke;
`AND`/`OR` kombinieren Bedingungen. Array-Fragen können auf Frage-, Zeilen-
oder Zellniveau referenziert werden.

`array_filter` und `array_filter_exclude` sind Frageattribute und erzeugen
Unterfragen-/Antwortfilter. Sie sind nicht identisch mit der Sichtbarkeit
der gesamten Frage.

## Import-/Exportanforderungen

* Originale Relevance-Strings byte-/zeichengetreu erhalten.
* Strukturierte Conditions mit Operator, linker/rechter Referenz,
  Gruppierung und Reihenfolge erhalten, wenn vorhanden.
* Fragecodes statt nur numerischer SGQA-IDs als semantische Referenz nutzen,
  aber alte IDs für verlustfreien Export aufbewahren.
* Keine Expression auswerten oder umformatieren.
* Konflikte zwischen `conditions` und `relevance` melden.

## Status der Referenz

In der bereitgestellten Datei existiert kein `conditions`-Bereich; die
20 Fragen tragen Relevance-Felder und die Gruppe `grelevance`. Das ist
eine Beobachtung dieses Exports und kein Beweis, dass Conditions generell
nicht exportiert werden.

Quellen: [ExpressionScript – Presentation](https://www.limesurvey.org/manual/ExpressionScript_-_Presentation),
[Setting conditions](https://www.limesurvey.org/manual/Setting_conditions).
