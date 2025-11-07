import pandas as pd
temperatura = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Styczeń': [-2, -1, 0, -1, -2, -3],
    'Kwiecień': [9, 10, 8, 11, 10, 9],
    'Lipiec': [19, 20, 17, 21, 19, 20],
    'Październik': [9, 9, 10, 10, 9, 8]
})

# === A ===
print("\n1. Miasta posortowane wg temperatury w lipcu (rosnąco):")
print(temperatura.sort_values("Lipiec").head())

# === B ===
print("\n2. Miasta posortowane wg temperatury w styczniu (malejąco):")
print(temperatura.sort_values("Styczeń", ascending=False).head())

#=== C ===
print("\n3. Miasta posortowane wg temperatury w lipcu (malejąco), a następnie według kwietnia (rosnąco):")
print(temperatura.sort_values(["Lipiec", "Kwiecień"],
                         ascending=[False, True]))

# a) Posortuj miasta według temperatury w lipcu (rosnąco)
# b) Posortuj miasta według temperatury w styczniu (malejąco)
# c) Posortuj miasta według temperatury w lipcu (malejąco), a następnie według kwietnia (rosnąco)