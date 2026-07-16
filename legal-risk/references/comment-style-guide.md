# Comment Style Guide

How to write the Polish-language comments that appear in the annotated .docx.

## Tone

- **Professional but direct.** Like a senior in-house counsel reviewing for a fellow professional.
- **No padding.** No "I would suggest considering whether possibly..." Just say what's wrong and what to do.
- **No legal disclaimers** ("this is not legal advice," "consult an attorney"). The user knows the context.
- **No emojis in the body** of the comment. The severity tag in the header uses an emoji; that's enough.
- **Address the buyer as "Państwo"** (formal plural) or use impersonal forms ("warto," "należy," "rekomendujemy") — never "ty/wy".
- **Where the clause meaning is subtle or counter-intuitive, explain it before evaluating.** A senior lawyer doesn't just say "this is bad" — they say "this means X, which most readers would miss; the effect is Y; therefore action Z." If a clause uses a conditional structure ("subject to...", "provided that..."), a vague qualifier ("reasonable", "as deems necessary"), or a procedural mechanism (mandatory mediation, cure period) whose practical effect isn't obvious from a casual read, spend 2-3 sentences on what it actually does in practice — including a concrete worked example where helpful — before getting to the recommendation. The user should walk away understanding why the clause matters, not just trusting the label.

## Structure of every comment

```
[<emoji> <SEVERITY-PL> | KATEGORIA: <CATEGORY-PL>]

<Identyfikacja problemu — 1-2 zdania, co konkretnie jest nie tak>

<Uzasadnienie prawne lub biznesowe — 1-3 zdania, dlaczego to ważne, z podstawą prawną jeśli istotne (np. „GDPR Art. 28(3)", „KC Art. 473 §2")>

<Co zrobić — konkretne działanie>

Sugerowana zmiana (do wklejenia):
"<treść w języku umowy>"
```

Skip "Sugerowana zmiana" only if rewording doesn't apply (e.g., the issue is that something is missing entirely — then propose a new clause to insert, still in contract language).

## Severity labels in Polish

| EN | PL header | Emoji |
|---|---|---|
| DEAL_BREAKER | DEAL-BREAKER | 🔴 |
| NEGOTIATE | DO NEGOCJACJI | 🟠 |
| ACCEPTABLE | AKCEPTOWALNE | 🟢 |
| INFORMATIONAL | INFORMACYJNE | ⓘ |

## Category labels in Polish

| EN | PL |
|---|---|
| GDPR | RODO |
| IP | WŁASNOŚĆ INTELEKTUALNA |
| LIABILITY | ODPOWIEDZIALNOŚĆ |
| TERMINATION | ROZWIĄZANIE UMOWY |
| JURISDICTION | JURYSDYKCJA |
| PAYMENT | PŁATNOŚCI |
| CONFIDENTIALITY | POUFNOŚĆ |
| INDEMNIFICATION | ODSZKODOWANIA / INDEMNIZACJA |
| LICENSE | LICENCJA |
| OTHER | INNE |

## Examples

### Example 1: deal-breaker, GDPR
Anchor: "We may share data with third-party service providers as we deem necessary."

```
[🔴 DEAL-BREAKER | KATEGORIA: RODO]

Klauzula daje dostawcy nieograniczone prawo do udostępniania danych osobowych dowolnym podmiotom trzecim według własnego uznania. Narusza to art. 28 ust. 2 RODO, który wymaga uprzedniej pisemnej zgody administratora (Państwa) na każdego podprocesora oraz prawa do sprzeciwu.

Bez zmiany tej klauzuli nie można podpisać umowy w obecnym kształcie — naraża Państwa na bezpośrednie naruszenie RODO i ewentualne kary ze strony UODO.

Należy zażądać: (1) listy aktualnych podprocesorów w załączniku, (2) zobowiązania do powiadamiania o zmianach z minimum 30-dniowym wyprzedzeniem, (3) prawa do sprzeciwu z możliwością rozwiązania umowy.

Sugerowana zmiana (do wklejenia):
"Provider may engage sub-processors only with Customer's prior general written authorisation. Provider shall maintain a current list of sub-processors at [URL] and notify Customer of any intended changes at least thirty (30) days in advance. Customer may object to such changes; if the parties cannot agree, Customer may terminate the affected Services without penalty."
```

### Example 2: negotiate, liability
Anchor: "Provider's total liability shall not exceed fees paid in the preceding six (6) months."

```
[🟠 DO NEGOCJACJI | KATEGORIA: ODPOWIEDZIALNOŚĆ]

Limit odpowiedzialności dostawcy ograniczony do 6 miesięcy opłat jest poniżej standardu rynkowego (typowo 12 miesięcy). Przy umowach SaaS o znaczeniu produkcyjnym daje to bardzo niski pułap rekompensaty w przypadku poważnego naruszenia (np. wycieku danych).

Warto zażądać podwyższenia do 12 miesięcy oraz wprowadzenia tzw. super-cap (np. 2× standardowy limit) dla naruszeń bezpieczeństwa danych.

Sugerowana zmiana (do wklejenia):
"Provider's total liability shall not exceed fees paid by Customer in the twelve (12) months preceding the event giving rise to liability, except that for breaches of data protection or confidentiality obligations the cap shall be two times such amount."
```

### Example 3: acceptable, just for awareness
Anchor: "These Terms are governed by the laws of Ireland."

```
[🟢 AKCEPTOWALNE | KATEGORIA: JURYSDYKCJA]

Wybór prawa irlandzkiego dla klientów z EOG jest typowy dla amerykańskich dostawców SaaS działających przez podmiot europejski. Nie wiąże się z dodatkowym ryzykiem operacyjnym — prawo irlandzkie należy do systemu common law UE, decyzje sądów są wykonalne w Polsce zgodnie z Rozporządzeniem Bruksela I bis.

Sugerowana zmiana (do wklejenia): —
```

### Example 4: informational
Anchor: "Provider may use Customer's name and logo to identify Customer as a customer."

```
[ⓘ INFORMACYJNE | KATEGORIA: INNE]

Klauzula dotyczy publikacji marketingowej. Z punktu widzenia firmy działającej w sektorze retail, w którym kontrola marki jest istotna, warto zwrócić uwagę, że klauzula daje dostawcy prawo do wykorzystania logo bez Państwa uprzedniej zgody. Mechanizm opt-out (jeśli istnieje w innej części umowy) wystarcza, ale opt-in byłby korzystniejszy.

Działanie nie jest konieczne, ale można rozważyć negocjację, jeśli ekspozycja marki jest kwestią strategiczną.

Sugerowana zmiana (do wklejenia): —
```

### Example 5: deal-breaker, IP
Anchor: "Customer hereby grants Provider a perpetual, irrevocable, worldwide license to use Customer's Inputs for any purpose."

```
[🔴 DEAL-BREAKER | KATEGORIA: WŁASNOŚĆ INTELEKTUALNA]

Klauzula przekazuje dostawcy bezterminową, nieograniczoną licencję do dowolnego wykorzystania Państwa danych wejściowych (Inputs), w tym potencjalnie do trenowania modeli, sprzedaży osobom trzecim itp. Stanowi to nieakceptowalne ryzyko utraty kontroli nad danymi biznesowymi i potencjalnie tajemnicą przedsiębiorstwa.

Dodatkowo, jeśli Inputs zawierają dane osobowe, klauzula jest niezgodna z art. 28 ust. 3 lit. a) RODO (procesor działa wyłącznie na udokumentowane polecenie administratora).

Bez zasadniczej zmiany umowa nie nadaje się do podpisu. Należy zażądać: (1) zachowania pełni praw przez Klienta do Inputs, (2) ograniczenia licencji dla dostawcy wyłącznie do świadczenia usług na rzecz Klienta, (3) zakazu trenowania modeli na danych Klienta.

Sugerowana zmiana (do wklejenia):
"Customer retains all right, title and interest in and to its Inputs. Customer grants Provider a limited, non-exclusive, non-transferable license to use Inputs solely to the extent necessary to provide the Services to Customer. Provider shall not use Inputs to train or improve any machine-learning model or for any other purpose."
```

## Escaping reminder (docx mode)

Comment text is passed to `scripts/docx_tool.py` as plain text inside `findings.json` — the script handles all XML escaping automatically. Only standard JSON escaping applies:

| Character | JSON escape |
|---|---|
| `"` | `\"` |
| `\` | `\` |
| newline | `
` |

Polish characters (ą, ć, ę, ł, ń, ó, ś, ź, ż) and emoji are valid UTF-8 and need no escaping. In the markdown report, no escaping is needed at all.

## What NOT to write

Bad examples — don't do this:

❌ "It might be a good idea to perhaps consider whether you could ask the vendor to maybe think about adjusting this clause."
✅ "Klauzulę należy zmienić."

❌ "Please consult your attorney for specific advice on this matter."
✅ (nothing — user knows)

❌ "This is a very interesting and important clause that warrants careful attention from a legal perspective."
✅ "Klauzula podnosi ryzyko: [opis]. Zalecane działanie: [działanie]."

❌ Rambling about what the clause says — the user can read it.
✅ Identify the issue → why it matters → what to do.
