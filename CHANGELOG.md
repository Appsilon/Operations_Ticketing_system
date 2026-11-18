# Historia zmian

Każda zmiana w repo = osobny commit + wpis tutaj (najnowsze na górze).

## 2026-11-18

1. Dodano `analysis/ko_screen/topdesk.md`: sprawdzenie K.O. TOPdesk (Meets 9 / Partial 6 / Does not meet 0 / Unknown 1). Korekta recenzenta: #12 z „Meets” na „Unknown”, bo ocena opierała się na wniosku agenta, nie na dowodzie. Ceny i źródło ISO 27001 sprawdzone ponownie.
2. `analysis/01_kryteria_KO.md` → `analysis/01_ko_criteria.md`: przetłumaczono na angielski, status „accepted”, dodano regułę C (#23, #27, #29 – decyzja użytkownika) i regułę flagi dla narzędzi, które odpadają tylko na nich. Razem 16 kryteriów.
3. `CLAUDE.md`: zapisano decyzje użytkownika – 16 kryteriów K.O. (13 + #23, #27, #29 z flagą „odpada tylko na nich”), większa waga wymagań Platform i IT, karta per narzędzie, ServiceNow w przeglądzie (treść stron od użytkownika), wyniki po angielsku. Usunięto z sekcji sieci curl z User-Agent i dodano zakaz obchodzenia blokad stron (próba wobec ServiceNow została zablokowana przez zabezpieczenia sesji).
4. Dodano `analysis/01_kryteria_KO.md`: propozycja 13 kryteriów K.O. wyliczona z arkusza (reguła A: Must od ≥2 obszarów; reguła B: Notes „Impact on tool choice” nazywa wymaganie kluczowym/eliminującym), wymagania do osobnej decyzji (#27, #29, #23) i niespójność #40 vs Notes #16. Status: czeka na akceptację.
5. Zapisano w `CLAUDE.md` decyzje z etapu 1 (źródło wymagań, jedno narzędzie najpierw, ceny bez budżetu, założenie ~11 agentów, lista narzędzi, format wyniku, termin) oraz sposób dostępu do stron vendorów. Dodano `tools/pw_text.js` (pobieranie stron przez Chromium), bo WebFetch nie działa w tej sesji.
6. Dodano `CHANGELOG.md` i zasady repo w `CLAUDE.md`: każda zmiana to osobny commit z wpisem w historii zmian.
7. Dodano `CLAUDE.md`: zasady komunikacji, brief zadania, link do arkusza wymagań, etapy pracy.
