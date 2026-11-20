# WP-01.3 – Fragetypen

## Codes aus LimeSurvey 6

Die Codes sind aus `Question.php` und der offiziellen Übersicht belegt. Die
Referenzdatei enthält ausschließlich 20 Fragen des Typs `L` (List/Radio).

| Code | Bezeichnung | Struktur |
|---|---|---|
| `1` | Array dual scale | Unterfragen, zwei Antwortskalen |
| `5` | 5-point choice | feste 1–5-Antworten |
| `A` | Array 5 point | Unterfragen, feste 1–5-Skala |
| `B` | Array 10 choice | Unterfragen, feste 1–10-Skala |
| `C` | Array Yes/No/Uncertain | Unterfragen, feste Ja/Nein/Unsicher-Skala |
| `D` | Date | Datumseingabe |
| `E` | Array Increase/Same/Decrease | Unterfragen, feste Dreierskala |
| `F` | Array | Unterfragen und Antwortskala |
| `G` | Gender | vordefinierte Einzelauswahl |
| `H` | Array by column | Array mit vertauschten Achsen |
| `I` | Language | Sprachauswahl |
| `K` | Multiple numerical input | mehrere numerische Unterfragen |
| `L` | List (Radio) | einzelne Antwort, Referenz beobachtet |
| `M` | Multiple choice | mehrere Antworten/Unterfragen |
| `N` | Numerical input | Zahl |
| `O` | List with comment | Auswahl plus Kommentar |
| `P` | Multiple choice with comments | Mehrfachauswahl plus Kommentare |
| `Q` | Multiple short text | mehrere kurze Texte |
| `R` | Ranking | Rangfolge von Antworten |
| `S` | Short free text | kurzer Text |
| `T` | Long free text | mehrzeiliger Text |
| `U` | Huge free text | großer Text |
| `X` | Text display | Anzeige ohne Antwort |
| `Y` | Yes/No | Ja/Nein |
| `!` | List (Dropdown) | einzelne Antwort als Dropdown |
| `|` | File upload | Datei-Upload |
| `*` | Equation | berechneter, speicherbarer Wert |
| `:` | Array by numbers | numerische Matrix |
| `;` | Array by text | Textmatrix |

## Modellregeln

Fragen haben `qid`, `sid`, `gid`, `parent_qid`, `type`, `title` (Fragecode),
`preg` (Legacy-Validierung), `other`, `mandatory`, `encrypted`,
`question_order`, `scale_id`, `relevance`, Theme und Script-Felder.
Unterfragen sind ebenfalls `questions`-Zeilen mit `parent_qid` und eigener
Sprache; sie sind nicht durch einen separaten `subquestions`-Bereich
repräsentiert.

Antworten sind bei Auswahl-/Array-Typen erforderlich; Text-, Anzeige- und
Equation-Typen können ohne `answers` auskommen. Arrays benötigen zusätzlich
Unterfragen und mindestens eine Skala. Dual- und flexible Arrays können zwei
Skalen bzw. zwei Unterfragenachsen benötigen.

## Besonderheiten

Der Typcode allein beschreibt nicht die gesamte Darstellung. Theme,
`question_attributes`, Antworten, Unterfragen und Sprachzeilen bestimmen das
Verhalten gemeinsam. Neue/erweiterte Themes können zusätzliche Typen oder
Attribute registrieren. Die Produktlogik darf daher keine unbekannten Codes
verwerfen.

Quellen: [Question types manual](https://www.limesurvey.org/manual/Question_types),
[Question model](https://github.com/LimeSurvey/LimeSurvey/blob/master/application/models/Question.php).
