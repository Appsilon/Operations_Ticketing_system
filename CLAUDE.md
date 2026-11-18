# Wybór narzędzia helpdesk / service desk

Czytaj ten plik na starcie każdej sesji i stosuj poniższe zasady.

## Zasady pracy i komunikacji (obowiązkowe)

1. Nigdy niczego nie zgaduj.
2. Nie zakładaj.
3. Nie wymyślaj.
4. Jeśli nie wiesz – powiedz, że nie wiesz, albo zapytaj.
5. Jeśli coś zakładasz – powiedz o tym wprost.
6. Jeśli korzystasz ze źródeł – zawsze podaj, z czego korzystasz (link, nazwa dokumentu, data sprawdzenia).
7. Wyniki podawaj zwięźle: punkty numerowane, bez bloków tekstu. Mniej tekstu = lepiej napisane zdanie.
8. Prosto do celu, bez owijania w bawełnę.
9. Nie bądź miły – bądź obiektywny.
10. Nie zgadzaj się z użytkownikiem, jeśli wiesz, że nie ma racji.
11. Bądź szczery i bezpośredni.
12. Używaj emotek.

## Zasady repo

1. Każda zmiana = osobny commit z opisem, co i dlaczego się zmieniło.
2. Każdy commit dopisuje wpis do `CHANGELOG.md` (data, co, dlaczego).
3. Po każdym commicie push na branch roboczy.

## Zadanie (brief od zlecającego)

Szukamy narzędzia helpdesk / service desk, które w jednym miejscu obsłuży:
- wewnętrzne zgłoszenia,
- pracę z klientami zewnętrznymi.

Kroki:
1. Przejrzeć listę wymagań z arkusza (poniżej).
2. Krótki przegląd rynku: jakie narzędzia sensownie łączą helpdesk wewnętrzny i kliencki.
3. Zestawić je z wymaganiami: prosta tabelka spełnia / częściowo / nie spełnia + orientacyjna cena (jeśli dostępna) + czy jest darmowy trial.
4. Wskazać 3 narzędzia do przetestowania na focus grupach, z uzasadnieniem w 1–2 zdaniach dla każdego.

Forma: nic rozbudowanego – zlecający ma szybko przejrzeć wyniki i zdecydować, od czego zacząć testy.

Narzędzia wymienione w rozmowach (lista otwarta, można dodawać inne):
- Jira Service Management (zlecający: „chyba inaczej się teraz nazywa, zrobił się z tego bundle, ma też asset management”),
- Freshdesk.

## Źródło wymagań

- Google Sheet „Helpdesk Tool requirements”: https://docs.google.com/spreadsheets/d/1ye7vTaVol6DFoRnUrXtx_ibS4FN5z_aJzppNDzCQIEM/edit
- Zakładki: Requirements, Notes, Legend.
- Lista wymagań jest otwarta i może się zmieniać – na starcie sesji czytaj aktualną wersję arkusza, nie polegaj na kopiach.
- Odczyt: connector Google Drive. `read_file_content` zwraca tylko próbkę tabeli – pobieraj eksport .xlsx (`download_file_content`) i parsuj wszystkie wiersze.
- Brak uprawnień do edycji arkusza (stan na 2026-11-18).

## Decyzje (stan na 2026-11-18)

1. Arkusz jest jedynym źródłem wymagań i jedynym miejscem z aktualnymi informacjami.
2. Szukamy najpierw jednego narzędzia (wewnętrzne + klienci). Dwa narzędzia rozważamy dopiero, gdy żadne pojedyncze nie spełnia kryteriów K.O.
3. Budżet nieznany i nie ustalamy go (to decyzja poza naszym zadaniem). Zapisujemy ceny: plan, cena za agenta, okres rozliczenia, waluta, data sprawdzenia, link.
4. Liczba agentów to założenie użytkownika, nie dane: Platform ok. 6 (arkusz, Notes #10), Finance 1, People 2, IT 1, Operations 1, razem ok. 11. Używać tylko do orientacyjnej sumy i zawsze oznaczać jako założenie.
5. HubSpot jest używany do sprzedaży i marketingu.
6. Lista narzędzi do przeglądu (zaakceptowana): Atlassian (JSM / Service Collection), Freshworks, Zendesk, HubSpot Service Hub, Zoho Desk, HaloITSM/HaloPSA, TOPdesk, ServiceNow. ServiceNow blokuje automatyczną przeglądarkę – użytkownik kopiuje treść stron z URL-i, które mu podamy.
7. Ile narzędzi trafi później do testów – nie nasza decyzja. Cel: racjonalny przegląd, z którego team wybierze. Idealny wynik, jeśli się da: 3 do focus grup + 2 do pilotu u klientów.
8. Wynik budujemy tutaj i zapisujemy w repo. Google Sheets tworzymy dopiero na prośbę użytkownika.
9. Termin: praca trwa do końca bieżącego tygodnia (16–22.11.2026), nawet jeśli nie skończymy.
10. Kryteria K.O. (zaakceptowane 2026-11-18): 16 kryteriów w `analysis/01_ko_criteria.md` = 13 z reguł A+B + #23, #27, #29. Narzędzie, które odpada tylko na #23/#27/#29, a spełnia resztę, oznaczamy flagą i nie usuwamy po cichu.
11. Waga obszarów (decyzja użytkownika): wymagania Platform i IT są ważniejsze, bo People i Finance pracują dziś na swoich narzędziach (arkusz: Aboard – Notes #18, #30), IT nie ma narzędzia (arkusz: pingi na Slacku – Notes #25), Platform – wg użytkownika nie ma narzędzia (arkusz tego nie opisuje). Waga Operations: nieustalona.
12. Każde narzędzie dostaje kartę: wynik K.O., ile wymagań spełnia i dla kogo (Must/Nice per obszar), cena, trial, źródła.
13. Język wyników (pliki w `analysis/`): angielski. `CLAUDE.md` i `CHANGELOG.md` po polsku.

## Dostęp do sieci (stan na 2026-11-18)

1. Strony vendorów: używać `tools/pw_text.js` (Chromium/Playwright przez proxy).
2. Narzędzie WebFetch nie działa (ENOTFOUND) – nie używać.
3. WebSearch działa – tylko do znajdowania stron; źródła wtórne (blogi, Capterra itp.) zawsze oznaczać jako wtórne.
4. servicenow.com blokuje przeglądarkę headless („Access Denied”).
5. Nie obchodzić blokad stron (zabezpieczenia antybotowe, podmiana User-Agent itp.). Strona zablokowana → zapisać URL i poprosić użytkownika o treść.

## Proces

1. Etap 1: sprawdzić, czy przygotowanie jest kompletne (wymagania, dostępy, pytania do użytkownika) – dopiero potem przegląd rynku.
2. Etap 2: przegląd rynku.
3. Etap 3: tabela porównawcza.
4. Etap 4: rekomendacja 3 narzędzi.
