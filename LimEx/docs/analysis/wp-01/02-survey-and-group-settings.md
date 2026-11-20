# WP-01.2 – Umfrage- und Gruppeneinstellungen

## Beobachteter Survey

`surveys` enthält einen Datensatz für `sid=154993`; die Basissprache ist `de`,
`anonymized=Y`, `format=S`, `savetimings=Y`, `datestamp=Y`, `ipaddr=N`,
`ipanonymize=Y`, `allowprev=Y`, `showprogress=Y` und das Template ist
`hs-fulda`. Nicht gesetzte Werte sind in der Datei tatsächlich leer/fehlend
und dürfen nicht durch Defaults ersetzt werden.

## Survey-Kernfelder

| Feldgruppe | Felder und Bedeutung |
|---|---|
| Identität | `sid`, `gsid`, `admin`, `lastmodified` |
| Zeit | `startdate`, `expires`, `datestamp`, `savetimings` |
| Sprache | `language`, `additional_languages` |
| Datenschutz | `anonymized`, `ipaddr`, `ipanonymize`, `refurl`, `usecookie` |
| Navigation | `format` (`A/G/Q` bzw. geerbt), `allowprev`, `questionindex`, `navigationdelay` |
| Darstellung | `template`, `showwelcome`, `showprogress`, `showxquestions`, `showgroupinfo`, `showqnumcode`, `shownoanswer` |
| Teilnahme | `allowregister`, `allowsave`, `autoredirect`, `alloweditaftercompletion`, `access_mode` |
| Token/Mail | `usetokens`, `tokenlength`, `htmlemail`, `sendconfirmation`, `bounce_*`, `email*` |
| Statistik/Bewertung | `publicstatistics`, `publicgraphs`, `listpublic`, `assessments` |
| Captcha/Policy | `usecaptcha`, `showsurveypolicynotice`, `showregisterpolicy`, `showtokenpolicy` |
| Integration | `googleanalyticsstyle`, `googleanalyticsapikey` |

Die vollständige Feldmenge ist installations- und LimeSurvey-versionsabhängig;
die 62 Felder der Referenzdatei sind in `01-lss-structure.md` als beobachtete
Tabelle enthalten. Das interne Modell benötigt deshalb einen bekannten
Kern plus verlustfreien Erweiterungsspeicher.

## Sprachabhängige Survey-Daten

`surveys_languagesettings` enthält pro Sprache unter anderem
`surveyls_language`, `surveyls_title`, `surveyls_description`,
`surveyls_welcometext`, `surveyls_endtext`, Policy-Texte, URL und
E-Mail-Vorlagen. Texte sind HTML-/Markup-fähige Inhalte. Sprache wird über
`surveyls_survey_id` und `surveyls_language` zugeordnet; nicht über die
Reihenfolge der Zeilen.

## Gruppen

`groups` besitzt `gid`, `sid`, `group_order`, `randomization_group` und
`grelevance`. `group_l10ns` ergänzt `group_name`, `description`, `language`
und wiederholt technische Gruppeneigenschaften. Eine Gruppe ist damit
fachlich zweigeteilt: Reihenfolge/Logik im Kern und Text je Sprache.

`group_order` ist die feste Reihenfolge. `randomization_group` gruppiert
Gruppen für Randomisierung; `grelevance` ist eine ExpressionScript-Relevanz
für die Gruppe. Eine leere Relevanz muss von der expliziten Expression `1`
unterschieden werden.

## Belegt, beobachtet, offen

* **Belegt:** `Survey` dokumentiert Y/N-Felder und `format`, Navigation,
  Datenschutz und Beziehungen.
* **Beobachtet:** nur eine Gruppe, eine Sprache, keine Bedingungen,
  Quoten oder Teilnehmerattribute in dieser Datei.
* **Offen:** Vererbung aus Survey-Gruppen (`inherit`) und exakte Defaults
  müssen gegen die Zielinstallation getestet werden.

Quelle: [Survey model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Survey.php),
[Survey settings manual](https://www.limesurvey.org/manual/Survey_settings).
