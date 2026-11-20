# WP-03 – Fixtures und Testabdeckung

`tests/fixtures/limesurvey_survey_154993.lss` ist eine Kopie der bereit-
gestellten Referenzdatei. Die Tests prüfen XML-Format, `DBVersion=651`,
Sprache `de`, 20 Fragen vom Typ `L`, 80 Antworten, 20 Lokalisierungen,
840 Attribute, fünf Plugin-Settings und die beiden leeren Theme-Bereiche.

Unit-Tests prüfen zusätzlich Zustände, Unicode/HTML/Zeilenumbrüche, stabile
Referenzen, Umordnung, unbekannte Rohdaten, getrennte Logikfelder und
Validierungsfehler. Nicht verifiziert werden dadurch Quoten, Conditions als
LSS-Bereich, Unterfragen, Mehrfachskalen, Ressourcen, Berechtigungen und
andere Fragetypen.
