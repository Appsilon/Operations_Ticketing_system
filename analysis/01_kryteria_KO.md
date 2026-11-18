# Kryteria K.O. – propozycja

1. Status: **PROPOZYCJA, czeka na akceptację użytkownika.**
2. Źródło: Google Sheet „Helpdesk Tool requirements”, zakładki Requirements, Notes i Legend. Wersja pliku z modifiedTime 2026-11-13 13:07 UTC, sprawdzona 2026-11-18.
3. Kryterium K.O. = jeśli narzędzie go nie spełnia, odpada z dalszego porównania.

## Metoda (wyłącznie dane z arkusza)

1. Warunek wstępny: jedno narzędzie do zgłoszeń wewnętrznych i obsługi klientów zewnętrznych (brief; Notes #11 „One tool for internal needs (IT, operations) and external ones (client support)”).
2. Reguła A: wymaganie ma „Must have” od co najmniej 2 obszarów (kolumny Platform / Operations / IT / People / Finance).
3. Reguła B: wymaganie jest wskazane jako kluczowe lub eliminujące w Notes, w kolumnie „Impact on tool choice”, przez słowa „has to”, „key”, „are out”, „remain the must”.
4. K.O. to suma A i B. Pozostałe „Must have” są oceniane, ale nie eliminują.

## Wynik: 13 kryteriów K.O.

| # | Wymaganie | Reguła | Uzasadnienie z arkusza |
|---|---|---|---|
| 1 | Email-based ticket handling | A + B | Must: Platform, Operations. Notes #1: „Email handling has to be very good.” Notes #9: „The value has to come from our side, with no requirements placed on clients.” |
| 3 | Autoresponder | A | Must: Platform, People |
| 4 | Automatic notifications to the requester | A | Must: Platform, Operations, IT, People |
| 5 | Private notes (internal comments) | A | Must: Platform, Operations, People |
| 6 | Team collaboration on a ticket | A | Must: Platform, People |
| 9 | Configurable forms per ticket type or group | A + B | Must: Operations, People. Notes #20: „Configurable forms remain the must.” |
| 10 | Multi-step approval workflows | B | Notes #11: „The audit log and approval flows are key.” |
| 12 | Requesters see only their own tickets | A + B | Must: Operations, IT, People. Notes #16: „The tool has to support several permission models.” |
| 13 | Access separated by team desk, project or client | A + B | Must: Platform, IT, People. Notes #16 (jw.) |
| 15 | SLA/SLO policies with breach warnings | B | Notes #6: „The tool has to handle several levels of targets and warnings.” |
| 16 | Dashboards and reports | A | Must: Platform, Operations |
| 17 | Audit log of changes | B | Notes #11: „The audit log and approval flows are key.” |
| 26 | Mature vendor compliant with ISO 27001, NIS2 and GDPR | B | Notes #13: „Immature vendors without certifications are out.” |

## Obserwacje

1. Reguła A sama nie odróżnia narzędzi: 8 z 9 jej wymagań ma w arkuszu ocenę „Standard”, a #9 „Standard (higher plans)”. Ta ocena jest wstępna (Legend: „to be verified during trials”).
2. Narzędzia realnie różnicują: #10, #15, #17, #26 oraz to, w którym planie cenowym dana funkcja jest dostępna.
3. Do osobnej decyzji: poniższe wymagania mają „Must have” tylko od jednego obszaru i Notes nie nazywa ich kluczowymi, ale mogą być twarde:
   1. #27 Data stored in the EU (Operations),
   2. #29 Only agents are paid seats (Operations),
   3. #23 Two-way Slack integration (IT; Notes #25 pisze „must for IT”, ale tylko jako „Supports”).
4. Niespójność w arkuszu: Notes #16 mówi „Operations needs isolation per ticket (for example HR cases)”, a #40 „Per-ticket visibility for agents too” (przykład HR) ma u Operations „Nice to have”.

## Jak używamy K.O.

1. Krok 1: wszystkich kandydatów sprawdzamy tylko na 13 kryteriów K.O.
2. Krok 2: pełne 59 wymagań sprawdzamy tylko u kandydatów, którzy przeszli krok 1.
