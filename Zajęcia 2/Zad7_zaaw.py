import pandas as pd
import numpy as np

wyniki_egzaminy = pd.DataFrame({
    'Student': ['Anna', 'Bartek', 'Celina', 'Damian', 'Ewa', 'Filip', 'Gabriela', 'Hubert'],
    'Matematyka': [85, 92, 78, 88, 95, 72, 89, 81],
    'Fizyka': [78, 88, 82, 75, 91, 68, 85, 79],
    'Informatyka': [92, 85, 88, 90, 89, 95, 82, 87],
    'Kierunek': ['Informatyka', 'Fizyka', 'Matematyka', 'Informatyka',
                 'Matematyka', 'Informatyka', 'Fizyka', 'Matematyka']
})

# === A ===
print("\n1. Średnia wyników:")
wyniki_egzaminy["Średnia"] = wyniki_egzaminy[["Matematyka", "Fizyka", "Informatyka"]].mean(axis=1)
print(wyniki_egzaminy[["Student", "Średnia"]])

# === B ===
print("\n2. Status zaliczenia przedmiotu")
wyniki_egzaminy["Status"] = np.where(wyniki_egzaminy["Średnia"] >= 85, "Zaliczony", "Niezaliczony")
print(wyniki_egzaminy[["Student", "Średnia", "Status"]])

# === C ===
matematyka = wyniki_egzaminy[wyniki_egzaminy["Kierunek"] == "Matematyka"]
fizyka = wyniki_egzaminy[wyniki_egzaminy["Kierunek"] == "Fizyka"]
informatyka = wyniki_egzaminy[wyniki_egzaminy["Kierunek"] == "Informatyka"]

print("\nNajwyższa średnia - Matematyka")
print(matematyka.sort_values("Średnia", ascending=False)[["Student", "Średnia", "Kierunek"]].head(1))

print("\nNajwyższa średnia - Fizyka")
print(fizyka.sort_values("Średnia", ascending=False)[["Student", "Średnia", "Kierunek"]].head(1))

print("\nNajwyższa średnia - Informatyka")
print(informatyka.sort_values("Średnia", ascending=False)[["Student", "Średnia", "Kierunek"]].head(1))

# === D ===
print("\nWysoka średnia - informatyka")
sr_informatyka = wyniki_egzaminy[(wyniki_egzaminy["Kierunek"] == "Informatyka") & (wyniki_egzaminy["Średnia"] >= 85) 
                                 & (wyniki_egzaminy["Informatyka"] > 90)]
print(sr_informatyka.sort_values("Średnia", ascending=False)[["Student", "Średnia", "Informatyka"]])