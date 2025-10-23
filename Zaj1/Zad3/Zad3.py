import matplotlib.pyplot as plt

temp_2022 = [2, 4, 8, 13, 18, 21, 24, 23, 19, 14, 8, 3]
temp_2023 = [3, 5, 9, 14, 19, 22, 25, 24, 20, 15, 9, 4]
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze',
            'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']

def wykres(tab22, tab23, mce):

    # 2022
    max_22_val = max(tab22)
    min_22_val = min(tab22)
    max_22_idx = tab22.index(max_22_val)
    min_22_idx = tab22.index(min_22_val)
    
    # 2023
    max_23_val = max(tab23)
    min_23_val = min(tab23)
    max_23_idx = tab23.index(max_23_val)
    min_23_idx = tab23.index(min_23_val)

    plt.figure(figsize=(12, 6))
    plt.plot(mce, tab22, color = 'red', label = '2022')
    plt.plot(mce, tab23, color = 'blue', label = '2023')
    plt.title("Średnia temperatura")
    plt.xlabel("Miesiąc")
    plt.ylabel("Temperatura")

    # MAX
    plt.scatter(mce[max_22_idx], max_22_val, 
                color='red', marker='^', s=150, zorder=5, 
                label=f"Max 2022 ({max_22_val}°C w {mce[max_22_idx]})")
    
    plt.scatter(mce[max_23_idx], max_23_val, 
                color='red', marker='^', s=150, zorder=5, 
                label=f"Max 2023 ({max_23_val}°C w {mce[max_23_idx]})")
    
    # MIN
    plt.scatter(mce[min_22_idx], min_22_val, 
                color='blue', marker='v', s=150, zorder=5, 
                label=f"Min 2022 ({min_22_val}°C w {mce[min_22_idx]})")
    
    plt.scatter(mce[min_23_idx], min_23_val, 
                color='blue', marker='v', s=150, zorder=5, 
                label=f"Min 2023 ({min_23_val}°C w {mce[min_23_idx]})")
    
    plt.legend()
    plt.savefig('wykres3.png')

def srednia_roznica(tab22, tab23):
    roznice = []
    for i in range(12):
        roznica = tab22[i] - tab23[i]
        roznice.append(roznica)

    srednia_roz = abs(sum(roznice) / 12)
    print(f"Średnia różnica temperatur między latami wynosi: {srednia_roz:.2f}.")

    
wykres(temp_2022, temp_2023, miesiace)
srednia_roznica(temp_2022, temp_2023)


# a) Stwórz wykres liniowy porównujący temperatury w obu latach

# b) Zaznacz najcieplejszy i najzimniejszy miesiąc każdego roku

# c) Oblicz średnią różnicę temperatur między latami

# d) Dodaj odpowiednie etykiety, legendę i tytuł