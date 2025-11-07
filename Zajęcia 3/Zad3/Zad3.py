import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

wynagrodzenie = pd.DataFrame({
    'Miasto' : ['Warszawa', 'Kraków', 'Wrocław', 'Poznań', 'Gdańsk', 'Łódź'],
    'Wynagrodzenie [PLN]': [8500, 7200, 7400, 7100, 6900, 6300]
})

wynagrodzenie = wynagrodzenie.sort_values(by='Wynagrodzenie [PLN]', ascending=False)

colors = plt.cm.RdYlGn( 
    np.linspace(0, 1, len(wynagrodzenie))
)

# === WYKRES ===
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(
    wynagrodzenie['Miasto'],
    wynagrodzenie['Wynagrodzenie [PLN]'],
    color=colors,
    alpha=0.9
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 100,                 
        bar.get_y() + bar.get_height()/2, 
        f'{int(width):,} PLN', 
        va='center',
        fontsize=11
    )


ax.set_title('Średnie wynagrodzenie w polskich miastach', fontsize=16, fontweight='bold')
ax.set_xlabel('Wynagrodzenie [PLN]', fontsize=13)
ax.set_ylabel('Miasto', fontsize=13)
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)
ax.margins(x=0.25)

plt.tight_layout()
plt.savefig('wykres_wynagrodzenie_poziomy.png')
plt.show()
