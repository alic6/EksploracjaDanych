import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/workspaces/EksploracjaDanych/Zajęcia 3/wykresy/train.csv')

def histogram(dataframe, column_name):
    plt.figure(figsize=(10, 6))
    dataframe[column_name].plot(kind='hist', bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f'Histogram of {column_name}', fontsize=16)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', alpha=0.75)
    plt.show()


def skrzynkowy(dataframe, kolumna_numeryczna, kolumna_kategoryczna):
    
    plt.figure(figsize=(14, 6))
    
    sns.boxplot(
        x=kolumna_kategoryczna, 
        y=kolumna_numeryczna, 
        data=dataframe, 
        palette='Set2'
    )
    
    plt.title(f'Rozkład {kolumna_numeryczna} według {kolumna_kategoryczna}', fontsize=16)
    plt.xlabel(kolumna_kategoryczna, fontsize=12)
    plt.ylabel(kolumna_numeryczna, fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    plt.savefig('boxplot.png')
    plt.show()

def slupkowy(dataframe, kolumna_kategoryczna):
    plt.figure(figsize=(10, 6))
    counts = dataframe[kolumna_kategoryczna].value_counts()
    counts.plot(kind='bar', color='lightgreen', edgecolor='black', alpha=0.7)
    plt.title(f'Wykres słupkowy dla {kolumna_kategoryczna}', fontsize=16)
    plt.xlabel(kolumna_kategoryczna, fontsize=14)
    plt.ylabel('Liczba wystąpień', fontsize=14)
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.savefig('barplot.png')
    plt.show()

def punktowy(dataframe, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe[x_column], dataframe[y_column], color='coral', s=40, alpha=0.7)
    plt.title(f'Scatter Plot of {y_column} vs {x_column}', fontsize=16)
    plt.xlabel(x_column, fontsize=14)
    plt.ylabel(y_column, fontsize=14)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.savefig('scatter_plot.png')
    plt.show
    
def liniowy(dataframe, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sorted_df = dataframe.sort_values(by=x_column)
    plt.plot(sorted_df[x_column], sorted_df[y_column], color='purple', linewidth=2, alpha=0.7)
    plt.title(f'Line Plot of {y_column} vs {x_column}', fontsize=16)
    plt.xlabel(x_column, fontsize=14)
    plt.ylabel(y_column, fontsize=14)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

histogram(df, 'SalePrice')
skrzynkowy(df, 'SalePrice', 'Neighborhood')
slupkowy(df, 'OverallQual')
liniowy(df, 'YearBuilt', 'SalePrice')
punktowy(df, 'GrLivArea', 'SalePrice')