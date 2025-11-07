import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/workspaces/EksploracjaDanych/Zajęcia 3/Zad3nk/anscombe (1).csv")

df.columns = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']
df.index.name = "id"
df = df.drop(index=0).reset_index(drop=True)
df = df.astype(float)
print(df)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
pairs = [('x1', 'y1'), ('x2', 'y2'), ('x3', 'y3'), ('x4', 'y4')]
for i, (x_col, y_col) in enumerate(pairs):
    ax = axs[i // 2, i % 2]
    ax.scatter(df[x_col], df[y_col], color='blue', s=30, alpha=0.7)
    ax.set_title(f"Wykres {x_col}-{y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('wykres3.png')
plt.show()

