import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def rzut_koscia():
    rzuty = np.random.randint(1, 7, 1000)
    tabela_wynikow = pd.DataFrame(rzuty, columns=['Rzut'])
    return tabela_wynikow

def wykres(df_wynikow):
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.hist(df_wynikow['Rzut'], bins=np.arange(0.5, 7.5, 1), 
             color='skyblue', edgecolor='black', alpha=0.7, rwidth=0.8)
    plt.xlabel('Liczba oczek')
    plt.ylabel('Liczba rzutów')
    plt.title('Częstość wyrzucania danej liczby oczek')
    plt.grid(axis='y', alpha=0.3)
    plt.savefig('wykres4.png')

def analiza(df_wynikow):
    empiryczne_prawd = df_wynikow['Rzut'].value_counts(normalize=True).sort_index() * 100
    teoretyczne_prawd = pd.Series(1/6 * 100, index=range(1, 7))

    print(f"Prawdopodobieństwo teoretyczne dla każdej liczby oczek średnio: {teoretyczne_prawd.mean():.2f}")
    print(f"Prawdopodobieństwa empiryczne: {empiryczne_prawd}")
    max_odchylenie = abs(empiryczne_prawd - teoretyczne_prawd).max()
    print(f"\nMaksymalne odchylenie od teorii: {max_odchylenie:.2f} pkt. proc.")
    print("""Wniosek: Wyniki są generalnie zgodne z teorią: Każda liczba ~16,67.
          Im więcej losowań (sprawdzono 100 - 1000 - 10000) tym prawdopodobieństwo 
          teoretyczne bardziej zbliżone do empirycznego)""")

wyniki_symulacji = rzut_koscia()
wykres(wyniki_symulacji)
analiza(wyniki_symulacji)

# Zasymuluj 1000 rzutów kostką (6-ścienną):

# a) Wygeneruj dane używając np.random.randint(1, 7, 1000)

# b) Stwórz histogram pokazujący częstość każdej liczby

# c) Oblicz teoretyczne i empiryczne prawdopodobieństwo każdej liczby

# d) Czy wyniki są zgodne z teorią? (każda liczba ~16.67%)