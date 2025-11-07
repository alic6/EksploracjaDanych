import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def godziny_nauki():
    godziny = np.random.randint(0, 10, 100)
    szum = np.random.uniform(-10, 10, 100)
    ocena = 50 + godziny * 5 + szum

    tabela_wynikow = pd.DataFrame({
            'Godziny nauki': godziny,
            'Ocena' : ocena
    })
    

    plt.figure(figsize=(8, 4))
    sns.scatterplot(data=tabela_wynikow, x='Godziny nauki', y='Ocena',
                s=100, alpha=0.7, color='purple')
    sns.regplot(data=tabela_wynikow, x='Godziny nauki', y='Ocena',
            scatter=False, color='red', line_kws={'linewidth': 2})

    plt.title('Zależność oceny od liczby godzin nauki', fontsize=16, fontweight='bold')
    plt.xlabel('Godziny nauki', fontsize=14)
    plt.ylabel('Ocena', fontsize=14)
    plt.ylim([10, 120])
    plt.tight_layout()
    plt.savefig('wykres_oceny.png') 
    plt.show()

    return tabela_wynikow


df = godziny_nauki()
print(df.head())