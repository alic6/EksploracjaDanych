import pandas as pd
temperatura = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Styczeń': [-2, -1, 0, -1, -2, -3],
    'Kwiecień': [9, 10, 8, 11, 10, 9],
    'Lipiec': [19, 20, 17, 21, 19, 20],
    'Październik': [9, 9, 10, 10, 9, 8]
})

# === A ===
print("3 pierwsze wiersze:")
print(temperatura.head(3))

# === B ===
temperatura.info()

# === C ===
print(f"Dataframe ma: {temperatura.shape[0]} wierszy i {temperatura.shape[1]} kolumn.")

# === D ===
print(f"Nazwy kolumn: {temperatura.columns.tolist()}")


# a) Wyświetl pierwsze 3 wiersze
# b) Wyświetl informacje o typach danych (.info())
# c) Wyświetl kształt DataFrame (.shape)
# d) Wyświetl tylko nazwy kolumn (.columns)