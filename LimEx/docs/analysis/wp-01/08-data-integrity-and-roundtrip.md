# WP-01.8 – Datenintegrität und Roundtrip

## Verlust- und Veränderungsrisiken

1. **HTML/JavaScript:** Fragetext, Hilfe, Surveytexte und Attribute können
   Markup oder Script enthalten. Nicht sanitizen, rendern, minifizieren,
   normalisieren oder automatisch escapen.
2. **CDATA:** CDATA ist nur XML-Syntax. Inhalt exakt als Unicode-String
   speichern; `]]>` beim Export segmentieren.
3. **Whitespace:** Zeilenumbrüche, führende Leerzeichen und leere Strings
   nicht trimmen.
4. **Sprachen:** `language` und Basissprache als Codes führen; keine
   Übersetzung aus einer anderen Sprache ableiten.
5. **Werte:** XML liest zunächst Zeichenketten. Typisierte Projektionen (Y/N,
   Integer, Float) dürfen den Rohwert nicht ersetzen.
6. **IDs:** `qid`, `gid`, `aid` und L10n-IDs sind Referenzen; neu vergebene
   IDs brauchen ein explizites Mapping.
7. **Reihenfolge:** XML-Reihenfolge, `sortorder`, `question_order` und
   `group_order` getrennt bewahren.
8. **Unbekannte Daten:** unbekannte Tabellen, Felder und Attribute nicht
   verwerfen.

## Dreizustandsregel

Jeder Feldwert benötigt mindestens:

* `missing`: XML-Element fehlt;
* `empty`: Element ist vorhanden, aber leer;
* `value`: Element hat Inhalt, einschließlich `"0"`, `"N"` oder Whitespace.

Defaults dürfen nur bei expliziter LimeSurvey-Semantik angewendet werden und
müssen als abgeleitet markiert werden.

## Empfohlenes internes Rohmodell

Das spätere Modell braucht einen verlustfreien Dokumentlayer (Originaltabellen,
Feldreihenfolge, Rohwerte, XML-Status, IDs und unbekannte Daten) und eine
getrennte semantische Projektion (Survey, Gruppe, Frage, Antwort, L10n,
Attribute, Logik). Der Dokumentlayer ist die Roundtrip-Garantie; die
Excel-Projektion ist eine Benutzeroberfläche, nicht die alleinige Quelle.

## Testfälle für WP-02+

* HTML mit Anführungszeichen, Unicode, CDATA-Grenzen und JavaScript.
* fehlendes, leeres und `"0"`-Feld.
* mehrere Sprachen und lokalisierte Attribute.
* unbekannter Attribute-Key und unbekannter Top-Level-Bereich.
* Antwortreihenfolge versus `random_group`.
* IDs mit nicht sortierter XML-Reihenfolge.
