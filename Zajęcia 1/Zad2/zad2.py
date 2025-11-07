portfolio = {
    'AAPL': {'liczba': 10, 'cena_zakupu': 150, 'cena_aktualna': 175},
    'GOOGL': {'liczba': 5, 'cena_zakupu': 2800, 'cena_aktualna': 2950},
    'MSFT': {'liczba': 15, 'cena_zakupu': 300, 'cena_aktualna': 320}
}

def poczatkowa_wartosc():
    calkowita_poczatkowa = 0

    for symbol, dane in portfolio.items():
        koszt_zakupu = dane['liczba'] * dane['cena_zakupu']

        calkowita_poczatkowa += koszt_zakupu

    print("Całkowita wartość początkowa portfolio:", calkowita_poczatkowa)

def aktualna_wartosc():
    calkowita_aktualna = 0

    for symbol, dane in portfolio.items():
        koszt_zakupu = dane['liczba'] * dane['cena_aktualna']

        calkowita_aktualna += koszt_zakupu

    print("Całkowita wartość aktualna portfolio:", calkowita_aktualna)

def zmiana():
    zmiany = []
    procent_zmiany = []

    for symbol, dane in portfolio.items():
        zmiana = dane['liczba'] * (dane['cena_aktualna'] - dane['cena_zakupu'])
        zmiany.append(zmiana)

        if zmiana >= 0:
            print("Zysk dla akcji", symbol, "wynosi", zmiana)
        else:
            print("Strata dla akcji", symbol, "wynosi", abs(zmiana))

        procent_zmiana = (dane['cena_aktualna'] - dane['cena_zakupu']) / dane['cena_zakupu'] * 100
        procent_zmiany.append(procent_zmiana)

    
    klucze_akcji = list(portfolio.keys())
    procent_zmiany_akcji = dict(zip(klucze_akcji, procent_zmiany))

    najlepsza_akcja = max(procent_zmiany_akcji, key=procent_zmiany_akcji.get)
    najwiekszy_procent = procent_zmiany_akcji[najlepsza_akcja]

    print(f"Największy zwrot przynoszą akcje: {najlepsza_akcja} o procentowej wartości: {najwiekszy_procent:.2f} %")


poczatkowa_wartosc()
aktualna_wartosc()
zmiana()

## a) Oblicz całkowitą wartość początkową portfolio

## b) Oblicz aktualną wartość portfolio

## c) Oblicz zysk/stratę dla każdej akcji

## d) Które akcje przynoszą największy zwrot (w %)?

