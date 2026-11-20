# WP-03 – Rohdatenmodell

`RawTable` bewahrt Tabellenname, Tabellenreihenfolge, Feldnamen, Zeilen,
Quellpfad und den Status `known`. `RawRow` bewahrt Datensatzreihenfolge und
`RawField` bewahrt Feldreihenfolge, Namen, Wertzustand und Originalwert.
Damit können unbekannte Tabellen/Felder ohne interpretierte Semantik gehalten
werden. Eine spätere Domänenprojektion ersetzt diese Struktur nicht.

Die Test-Fixture nutzt ausschließlich tatsächlich beobachtete LSS-Bereiche;
fehlende oder leere Bereiche werden nicht als Beleg ihrer vollständigen
Semantik ausgelegt.
