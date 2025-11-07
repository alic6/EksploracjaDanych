import pandas as pd
temperatura = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Styczeń': [-2, -1, 0, -1, -2, -3],
    'Kwiecień': [9, 10, 8, 11, 10, 9],
    'Lipiec': [19, 20, 17, 21, 19, 20],
    'Październik': [9, 9, 10, 10, 9, 8]
})

# === A ===
print("1. Jedna kolumna: Miasto")
print(temperatura["Miasto"])
print(f"\nTyp: {type(temperatura['Miasto'])}")

# === B ===
print("\n2. Dwie kolumny: Miasto i Lipiec")
print(temperatura[["Miasto", "Lipiec"]])

# === C ===
print("\n3. Kolumny Miasto, Styczeń i Lipiec:")
kolumny = ["Miasto", "Styczeń", "Lipiec"]
print(temperatura[kolumny])

# a) Wybierz tylko kolumnę 'Miasto' (wynik: Series)
# b) Wybierz kolumny 'Miasto' i 'Lipiec' (wynik: DataFrame)
# c) Wybierz kolumny 'Miasto', 'Styczeń' i 'Lipiec', używając zmiennej z listą nazw kolumn
