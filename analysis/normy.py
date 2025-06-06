import pandas as pd
import os

def analyze_normy(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'jazda_prosto.txt'))
    voltage_col = [col for col in df.columns if 'battery cell voltage' in col.lower()][0]
    current_col = [col for col in df.columns if 'momentary current consumption' in col.lower()][0]

    avg_voltage = df[voltage_col].mean()
    avg_current = df[current_col].mean()
    avg_power = (avg_voltage / 1000) * (avg_current / 1000)  # W

    # Pobór mocy w postojowym
    df_postoj = pd.read_csv(os.path.join(data_dir, 'postoj.txt'))
    voltage_col_p = [col for col in df_postoj.columns if 'battery cell voltage' in col.lower()][0]
    current_col_p = [col for col in df_postoj.columns if 'momentary current consumption' in col.lower()][0]
    standby_power = (df_postoj[voltage_col_p].mean() / 1000) * (df_postoj[current_col_p].mean() / 1000)

    # Przykładowy czas reakcji (do podania ręcznie lub wyliczenia)
    reaction_time = 0.3  # s

    params = {
        "avg_power": avg_power,
        "standby_power": standby_power,
        "reaction_time": reaction_time,
        "efficiency_ok": avg_power > 0.8,
        "standby_ok": standby_power < 25.0,
        "reaction_ok": reaction_time < 0.5
    }
    return params
