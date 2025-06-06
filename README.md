# Analiza energii dla pojazdu AGV

Aplikacja webowa do analizy zużycia energii przez pojazd AGV (Automated Guided Vehicle) w różnych trybach pracy. Projekt powstał na potrzeby zajęć "Energooszczędne układy napędowe".

---


## 🚀 Jak uruchomić aplikację?

1. **Klonuj repozytorium:**
    ```
    git clone https://github.com/Lozov13/energy-analysis-AGV.git
    cd energy-analysis-AGV
    ```
2. **Zainstaluj zależności:**
    ```
    pip install -r requirements.txt
    ```

3. **Uruchom aplikację:**
    ```
    python app.py
    ```

4. **Otwórz w przeglądarce:**
    ```
    http://localhost:5000
    ```

---

## 🛠️ Technologie i biblioteki

- **Flask** – backend i routing aplikacji webowej
- **Pandas, NumPy** – analiza i przetwarzanie danych
- **Plotly** – interaktywne wykresy
- **Bootstrap 5** – stylowanie i responsywność
- **HTML/CSS** – szablony i własny styl

---

## 📊 Co znajdziesz w aplikacji?

Aplikacja prezentuje dane i wykresy w 5 zakładkach tematycznych:
- **Analiza efektywności energetycznej** – zużycie energii, sprawność, wykresy czasowe
- **Porównanie trybów pracy** – wykresy słupkowe, porównania manewrów (jazda prosto, zakręt, postój itd.)
- **Optymalizacja profilu jazdy** – analiza przyspieszania, jazdy ze stałą prędkością, propozycje optymalizacji
- **Analiza baterii i zarządzanie energią** – napięcie, stan naładowania, trendy
- **Weryfikacja zgodności z normami** – porównanie z IEC 62864-1 i typowymi wymaganiami branżowymi

Każda zakładka korzysta z własnego pliku analitycznego w folderze `analysis/`, co ułatwia rozwój i modyfikacje.

---

## 📄 Format danych

Pliki w folderze `data/` to CSV/TXT z nagłówkami, np.:
- `Time stamp`
- `Momentary energy consumption mWh`
- `Total energy consumption uWh`
- `Battery cell voltage`
- `Momentary current consumption mA`
- `State Of Charge`
- `ActualSpeed_L`, `ActualSpeed_R`
- ...i inne parametry statusu pojazdu

---

## ✍️ Jak to działa?

- Logika analityczna jest rozbita na osobne moduły (każda zakładka = osobny plik w `analysis/`)
- Flask ładuje dane, przekazuje wyniki i wykresy do szablonów HTML
- Wykresy generowane są w Plotly i wyświetlane na stronie przez JavaScript
- Aplikacja jest responsywna i czytelna dzięki Bootstrapowi

---

## 📈 Przykładowe analizy

- Średnie i całkowite zużycie energii w różnych manewrach
- Porównanie efektywności jazdy prosto vs. zakręt vs. postój
- Analiza napięcia i SoC baterii w czasie
- Sprawdzenie zgodności z normami branżowymi

---

## 👤 Autor

- Łoziński Wojciech
- Górka Oskar
- Kępa Radosław

---
