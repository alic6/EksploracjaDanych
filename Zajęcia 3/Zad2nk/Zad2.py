import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/workspaces/EksploracjaDanych/Zajęcia 3/Zad2nk/LungDisease.csv")

x = df['Exposure']
y = df['PEFR']
mean_x = np.mean(x)
mean_y = np.mean(y)

cov_xy = np.sum((x - mean_x) * (y - mean_y)) / (len(x) - 1)

std_x = np.std(x, ddof=1)
std_y = np.std(y, ddof=1)

pearson_coefficient = cov_xy / (std_x * std_y)

print("Współczynnik korelacji Pearsona:", pearson_coefficient)

var_x = np.sum((x - mean_x)**2) / (len(x) - 1)
a = cov_xy / var_x
b = mean_y - a * mean_x

y_pred = a * x + b

print(f"Współczynnik kierunkowy a: {a:.3f}")
print(f"Wyraz wolny b: {b:.3f}")

plt.plot(x, y_pred, color='red', label=f'Regresja liniowa: y = {a:.2f}x + {b:.2f}')
plt.legend()
plt.scatter(df['Exposure'], df['PEFR'], s=10, label="Dane", alpha=0.5)
plt.xlabel("Exposure")
plt.ylabel("PEFR")
plt.grid(alpha=0.3)
plt.savefig("wykres_punktowy.png", dpi=300)
plt.show()