import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === DANE ===
miasta = ({
    'Rok': [2002, 2011, 2015, 2022],
    'Warszawa': [1672000, 1707000, 1740000, 1795000],
    'Łódź': [789318, 728892, None, 670642],
})

miasta_frame = pd.DataFrame(miasta)

miasta_frame.to_csv('populacja_miast.csv', index=False)
print("✓ Dane zapisane do pliku 'populacja_miast.csv'")

df_loaded = pd.read_csv('populacja_miast.csv')
print("\n✓ Dane wczytane z pliku:")
print(df_loaded.head())

# === WYKRES ===
df_melted = miasta_frame.melt(id_vars='Rok', var_name='Miasto', value_name='Populacja')

plt.figure(figsize=(8, 5))
sns.lineplot(
    data=df_melted,
    x='Rok', y='Populacja', hue='Miasto',
    style='Miasto', markers=True, dashes=False, linewidth=2.5
)
plt.title('Populacja miast w czasie (Seaborn)', fontsize=16, fontweight='bold')
plt.xlabel('Rok', fontsize=13)
plt.ylabel('Populacja', fontsize=13)
plt.legend(title='Miasto')
plt.tight_layout()
plt.savefig('wykres_seaborn.png')
plt.show()

# === WERSJA MATPLOTLIB ===
plt.figure(figsize=(8, 5))
plt.plot(miasta_frame['Rok'], miasta_frame['Warszawa'], marker='o', label='Warszawa')
plt.plot(miasta_frame['Rok'], miasta_frame['Łódź'], marker='s', label='Łódź')
plt.title('Populacja miast w czasie (Matplotlib)', fontsize=16, fontweight='bold')
plt.xlabel('Rok', fontsize=13)
plt.ylabel('Populacja', fontsize=13)
plt.legend()
plt.tight_layout()
plt.savefig('wykres_matplotlib.png')
plt.show()


# === WERSJA PANDAS ===
miasta_frame.set_index('Rok')[['Warszawa', 'Łódź']].plot(
    marker='o', figsize=(8,5), title='Populacja miast w czasie (Pandas)'
)
plt.xlabel('Rok', fontsize=13)
plt.ylabel('Populacja', fontsize=13)
plt.tight_layout()
plt.savefig('wykres_pandas.png')
plt.show()


