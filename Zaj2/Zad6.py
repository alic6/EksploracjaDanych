import pandas as pd

temperatura = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Styczeń': [-2, -1, 0, -1, -2, -3],
    'Kwiecień': [9, 10, 8, 11, 10, 9],
    'Lipiec': [19, 20, 17, 21, 19, 20],
    'Październik': [9, 9, 10, 10, 9, 8]
})

# === A ===
print("\n1. Średnia z wszystkich miesięcy:")
temperatura["Średnia_roczna"] = temperatura[["Styczeń", "Kwiecień", "Lipiec", "Październik"]].mean(axis=1)
print(temperatura[["Miasto", "Średnia_roczna"]])

# === B ===
print("\n2. Różnica między lipcem a styczniem")
temperatura["Amplituda"] = temperatura["Lipiec"] - temperatura["Styczeń"]
print(temperatura[["Miasto", "Amplituda"]])

# === C ===
print("\n3. Miasta, w których średnia roczna > 11")
temperatura["Ciepłe_miasto"] = temperatura["Średnia_roczna"] > 11
print(temperatura[["Miasto", "Średnia_roczna", "Ciepłe_miasto"]])

# a) Dodaj kolumnę 'Średnia_roczna' - średnia z wszystkich miesięcy
# b) Dodaj kolumnę 'Amplituda' - różnica między lipcem a styczniem
# c) Dodaj kolumnę 'Ciepłe_miasto' (True jeśli średnia roczna > 11, False w przeciwnym razie)
