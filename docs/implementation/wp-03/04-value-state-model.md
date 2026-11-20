# WP-03 – Wertzustände

`ValueState` definiert `missing`, `empty`, `value` und `deleted`.
`Value` speichert Zustand und Rohwert unabhängig voneinander. Ungültige
Kombinationen wie `missing` mit Rohwert oder `value` ohne Rohwert werden
beim Erzeugen abgelehnt. Leere Strings werden explizit als `empty`
repräsentiert; Unicode, HTML und Zeilenumbrüche bleiben unverändert.

Die Implementierung interpretiert `Y/N`, `0/1` und Expressions nicht
automatisch. Eine spätere Adapterprojektion kann typisieren und muss den
Rohwert behalten.
