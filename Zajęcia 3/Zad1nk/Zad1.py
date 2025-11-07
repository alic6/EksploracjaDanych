import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42) 
x = np.linspace(0, 10, 1000)

a_true = 2.5
b_true = 1.0

noise = np.random.normal(0, 2, size=1000)

y = a_true * x + b_true + noise

df = pd.DataFrame({'x': x, 'y': y})

slope, intercept, r_value, p_value, std_err = stats.linregress(df['x'], df['y'])

print(f"Wyniki regresji:")
print(f"a (slope) = {slope:.3f}")
print(f"b (intercept) = {intercept:.3f}")
print(f"R^2 = {r_value**2:.3f}")

plt.scatter(df['x'], df['y'], s=10, label="Dane", alpha=0.5)
plt.plot(df['x'], slope*df['x'] + intercept, color='red', label="Regresja liniowa")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig('wykres_nk.png')
plt.show()