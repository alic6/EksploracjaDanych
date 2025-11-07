## Import bibliotek
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

plt.rcParams.update({'font.size': 12})
plt.rcParams['figure.figsize'] = (10, 6)

miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
sprzedaz = [12500, 13200, 15800, 14200, 16500, 18200, 17800, 19200, 20500, 21300, 23500, 25200]



def statistics(lista):
    srednia = sum(lista) / len(lista)

    sprzedaz_sort = sorted(lista)
    sprzedaz_miesiac = dict(zip(miesiace, lista))
    dlugosc = len(sprzedaz_sort)

    indeks_prawy = dlugosc // 2
    indeks_lewy = indeks_prawy - 1
    mediana = (lista[indeks_lewy] + lista[indeks_prawy]) / 2

    minimum = sprzedaz_sort[0]
    maksmimum = sprzedaz_sort[dlugosc - 1]

    wysoka_sprzedaz = []

    for miesiac, sprzedaz_v in sprzedaz_miesiac.items():
        if sprzedaz_v > srednia:
            wysoka_sprzedaz.append(miesiac)

    procentowy_wzrost = (sprzedaz_sort[dlugosc - 1] - sprzedaz_sort[0]) / sprzedaz_sort[0] * 100

    print("Średnia =", srednia)
    print("Mediana =", mediana)
    print("Minimum =", minimum)
    print("Maksimum =", maksmimum)
    print("Sprzedaż wyższa niż średnia wystąpiła w miesiącach:", wysoka_sprzedaz)
    print("Wzrost sprzedaży (styczeń / grudzień) wyniósł:", procentowy_wzrost)

def wykres(lista):
    skrot_miesiace = [m[:3] for m in miesiace]
    srednia = sum(lista) / len(lista)
    plt.figure(figsize=(12, 6))
    plt.plot(skrot_miesiace, lista)
    plt.axhline(y = srednia,
                color = 'green',
                label=f'Średnia ({srednia:.0f} PLN)')
    plt.title("Sprzedaż roczna")
    plt.xlabel("Miesiąc")
    plt.ylabel("Sprzedaż")
    plt.savefig('wykres1.png')

statistics(sprzedaz)
wykres(sprzedaz)


