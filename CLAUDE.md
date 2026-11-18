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

## Proces

1. Etap 1: sprawdzić, czy przygotowanie jest kompletne (wymagania, dostępy, pytania do użytkownika) – dopiero potem przegląd rynku.
2. Etap 2: przegląd rynku.
3. Etap 3: tabela porównawcza.
4. Etap 4: rekomendacja 3 narzędzi.
