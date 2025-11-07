import pandas as pd
temperatura = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Styczeń': [-2, -1, 0, -1, -2, -3],
    'Kwiecień': [9, 10, 8, 11, 10, 9],
    'Lipiec': [19, 20, 17, 21, 19, 20],
    'Październik': [9, 9, 10, 10, 9, 8]
})

# === A ===
print("\n1. Miasta z temperaturą > 18 stopni w lipcu i >= -2 w styczniu:")
print(temperatura[(temperatura["Styczeń"] >= -2) & (temperatura["Lipiec"] > 18)])

# === B ===
print("\n2. Wybrane miasta:")
print(temperatura[temperatura["Miasto"].isin(["Warszawa", "Kraków", "Gdańsk"])])

# === C ===
print("\n3. Miasta, gdzie temperatura w lipcu jest między 18 a 20 stopni (włącznie):")
print(temperatura[(temperatura["Lipiec"] >= 18) & (temperatura["Lipiec"] <= 20)])

# a) Znajdź miasta, gdzie temperatura w lipcu > 18 ORAZ w styczniu >= -2
# b) Znajdź miasta: 'Warszawa', 'Kraków', 'Gdańsk'
# c) Znajdź miasta, gdzie temperatura w lipcu jest między 18 a 20 stopni (włącznie)