# WP-02.7 – Excel-UX und Validierung

## Modi

Der Einsteigermodus zeigt Kernblätter, deutsche Anzeigenamen,
Beispielzeilen, Dropdowns und kurze Hilfetexte. Der Expertenmodus blendet
Attribute, Conditions, Mapping und Rohdaten ein. Beide Modi arbeiten auf
denselben `stable_id`-Referenzen.

## UX-Regeln

Kopfzeilen werden fixiert, Tabellenfilter aktiviert und Pflichtfehler rot
markiert. Warnungen (unbekannter Typ, Roh-only-Attribut, Konflikt) sind
sichtbar, aber nicht durch kosmetische Defaults zu beheben. Technische
Spalten sind gruppiert und standardmäßig verborgen. Blattschutz darf nur
versehentliche Änderungen verhindern; Experten können ihn aufheben und die
Rohdaten bearbeiten.

## Validierung

Dropdowns nutzen Referenztabellen für Sprache, Fragetyp, Boolean/YN,
Operatoren und Skalen. Fachliche Prüfungen kontrollieren:

* eindeutige Survey-, Gruppen-, Frage- und Antwortcodes;
* existierende `group_ref`, `parent_ref`, `question_ref` und Sprachen;
* passende Antworten/Unterfragen zum Fragetyp;
* Integer-/Datums-/Optionenwerte gemäß Metadaten;
* `hidden`, `relevance`, `random_group` und `answer_order` getrennt;
* keine unaufgelösten ID-Mappings beim Export.

## HTML, Script und Formelinjektion

HTML, JavaScript, CSS und ExpressionScript werden als Textzellen behandelt.
Beim Schreiben wird eine Excel-formelsichere Anzeige verwendet, während
`raw_value` den Originalinhalt behält. Beim Lesen wird nur die Schutzmarkierung
entfernt, nicht der Inhalt interpretiert. Zeilenumbrüche bleiben erhalten;
Werte über 32.767 Zeichen gehen in `RAW_CHUNKS`.

Excel-Dateien sind keine Sicherheitsgrenze. HTML/JavaScript wird weder
ausgeführt noch sanitisiert; eine spätere Anwendung muss Warnungen und
Sicherheitsregeln getrennt behandeln.
