# WP-02.2 – Neutrales internes Datenmodell

## Schichten

Das Modell besteht aus drei getrennten Schichten:

1. **Dokumentschicht:** XML-Metadaten, Tabellenreihenfolge, Rohfelder,
   Zustände und unbekannte Daten.
2. **Domänenschicht:** Survey, Sprache, Gruppe, Frage, Antwort,
   Unterfrage, Attribute und Logik mit stabilen Referenzen.
3. **Projektionen:** Excel-Spalten und spätere LSS-Adapter.

Die Projektion darf Rohwerte nie ersetzen. Ein Adapter kann eine Domäne
erzeugen, ohne unbekannte Dokumentdaten zu verlieren.

## Entitäten

| Entität | Identität | Beziehungen |
|---|---|---|
| Survey | `stable_id`, optional `source_id` | Sprachen, Gruppen, Einstellungen |
| Language | Survey + `code` | lokalisierte Texte |
| Group | `stable_id` | Survey, L10n, Fragen |
| Question | `stable_id`, `code` | Gruppe, Elternfrage, Antworten, Attribute |
| Answer | `stable_id`, Frage + Code | L10n, Skala |
| Subquestion | Frage-Entität mit `parent_id` | Elternfrage, Skala |
| Attribute | Frage + Name + Sprache | Definition, Rohwert |
| Condition | `stable_id` | Ziel, Referenzen, Operatoren |
| RawTable/RawField | `raw_id` + Reihenfolge | Originaldokument |

## Typisierte Felder

Texte und Expressions bleiben Unicode-Strings. Boolesche Werte werden nur
als Projektion aus den LimeSurvey-Werten `Y/N`, `0/1` oder dokumentierten
Optionen gebildet. Jede Projektion behält Originalwert und Zustandswert.
IDs sind Strings oder Integer entsprechend ihrer Quelle, aber nie implizite
Excel-Zeilennummern.

## Beispiel einer Domänenreferenz

```json
{
  "stable_id": "question:7d...",
  "source_id": "2965",
  "code": "Q00",
  "group_ref": "group:...",
  "type": "L",
  "text_ref": {"de": "…"},
  "hidden": {"state": "value", "raw": "1"},
  "relevance": {"state": "value", "raw": "1"},
  "attributes": [{"name": "random_group", "raw": ""}]
}
```

Dies ist nur ein Datenformatbeispiel, keine produktive Python-Struktur.

## Zustandsmodell und Validierung

Import validiert Dokumentstruktur, Referenzen und bekannte Datentypen;
unbekannte Werte werden nicht verworfen. Domänenvalidierung meldet
Duplikate bei Survey-/Frage-/Antwortcodes, fehlende Eltern und ungültige
Skalen. Export validiert zusätzlich Ziel-ID-Mappings und Konflikte zwischen
`conditions` und `relevance`.

## Wahl der späteren Python-Technik

Für die spätere Implementierung ist eine Kombination aus typisierten
Dataclasses/Pydantic-Modellen für die Domänenschicht und einfachen
Rohdataclasses für XML-Felder geeignet. Pydantic bietet gute Eingabe- und
Fehlermeldungen, darf aber unbekannte Felder nicht durch Standardkonfiguration
verlieren. Die endgültige Bibliothekswahl bleibt WP-03 vorbehalten.
