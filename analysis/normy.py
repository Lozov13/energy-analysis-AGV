import pandas as pd
import os

def get_data_dir():
    # Pobierz absolutną ścieżkę do katalogu głównego projektu (tam gdzie app.py)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def analyze_normy():
    # Przykład: sprawdzenie wybranych parametrów względem normy IEC 62864-1
    # (dane przykładowe, dostosuj do swoich plików)
    data_dir = get_data_dir()
    df = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    # Sprawność układu (przykład uproszczony)
    avg_power = (df['Battery cell voltage mV'].mean() / 1000) * (df['Current consumption mA'].mean() / 1000)
    # Norma: sprawność powinna być >80%, pobór standby <25W, czas reakcji <0.5s
    # Tu tylko przykładowe wartości do porównania
    params = {
        "avg_power": avg_power,
        "standby_power": 24.0,    # Załóżmy, że masz taki pomiar z pliku "postoj.txt"
        "reaction_time": 0.3,     # Załóżmy, że masz taki pomiar
        "efficiency_ok": avg_power > 0.8,
        "standby_ok": 24.0 < 25.0,
        "reaction_ok": 0.3 < 0.5
    }
    return params
