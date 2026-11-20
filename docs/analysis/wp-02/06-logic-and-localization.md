# WP-02.6 – Logik und Lokalisierung

## Relevance

`Fragen.relevance` und `Gruppen.relevance` sind unveränderte
ExpressionScript-Strings. Der Wert `1`, ein leerer Wert und `missing` bleiben
unterscheidbar. Die Excel-Projektion darf Expressions nicht formatieren,
auswerten oder automatisch in Conditions zerlegen.

## Strukturierte Conditions

`Bedingungen` repräsentiert einzelne Vergleichsknoten und ihre Verknüpfung:
Ziel, linke Referenz, Operator, rechter Wert, `AND`/`OR` und
Elternknoten. Nicht abbildbare Syntax wird als `raw_expression` erhalten.
Conditions und Relevance sind alternative bzw. abhängige Darstellungen,
nicht zwei automatisch zu verknüpfende Regeln.

Bei Import werden vorhandene Conditions und Relevance gemeinsam geprüft.
Bei einem Konflikt wird ein Fehler/Warnstatus erzeugt und keine Seite
stillschweigend überschrieben. Export nutzt die strukturierte Form nur,
wenn ihre Rekonstruktion verifiziert ist; sonst wird die Originalstruktur
aus `Rohdaten` verwendet.

## Lokalisierung

Alle Texte referenzieren einen Sprachcode aus `Sprachen`. Titel, Hilfe,
Beschreibung, Antworttext, Gruppentext, Script, Attribute und Mailtexte
haben getrennte `text_kind`-Werte. Ein fehlender Text wird nicht aus der
Basissprache kopiert. Excel-Zellen enthalten Unicode und Zeilenumbrüche
unverändert.

`same_script`/sprachabhängige Attribute werden als eigene Sprachwerte
modelliert; die Semantik bleibt vom LSS-Adapter zu prüfen.

Quellen: [ExpressionScript](https://www.limesurvey.org/manual/ExpressionScript_-_Presentation),
[Conditions](https://www.limesurvey.org/manual/Setting_conditions).
