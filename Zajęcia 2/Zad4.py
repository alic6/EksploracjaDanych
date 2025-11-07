import pandas as pd
temperatura = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Styczeń': [-2, -1, 0, -1, -2, -3],
    'Kwiecień': [9, 10, 8, 11, 10, 9],
    'Lipiec': [19, 20, 17, 21, 19, 20],
    'Październik': [9, 9, 10, 10, 9, 8]
})

# === A ===
print("\n1. Miasta z temperaturą powyżej 19 stopni w lipcu:")
print(temperatura[temperatura["Lipiec"] > 19])

# === B ===
print("\n2. Miasta z temperaturą wyższą lub równą -1 stopni w styczniu:")
print(temperatura[temperatura["Styczeń"] >= -1])

# === C ===
print("\n3. Miasta z temperaturą równą 10 stopni w kwietniu:")
print(temperatura[temperatura["Kwiecień"] == 10])

# === D === 
print("\n4. Miasta z temperaturą równą 20 stopni w lipcu lub -1 w styczniu:")
print(temperatura[(temperatura["Styczeń"] == -1) | (temperatura["Lipiec"] == 20)])

# a) Znajdź miasta, gdzie temperatura w lipcu jest większa niż 19 stopni
# b) Znajdź miasta, gdzie temperatura w styczniu jest większa lub równa -1
# c) Znajdź miasta, gdzie temperatura w kwietniu wynosi dokładnie 10 stopni
# d) Znajdź miasta, gdzie temperatura w lipcu jest 20 LUB temperatura w styczniu jest -1