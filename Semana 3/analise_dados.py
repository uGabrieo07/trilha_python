import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def analisar_dados():
    # Função para abrir a janela de diálogo e selecionar o arquivo .csv
    root = tk.Tk()
    root.withdraw()
    caminho_do_arquivo = filedialog.askopenfilename(title="Selecione o arquivo CSV", 
                                                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    df = pd.read_csv(caminho_do_arquivo)

    # Histograma da distribuição de milhas por galão (mpg)
    plt.figure(figsize=(10, 6))
    plt.hist(df['mpg'], bins=10, edgecolor='black', color='skyblue')
    plt.title('Distribuição de Milhas por Galão (mpg)')
    plt.xlabel('Milhas por Galão (mpg)')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

    # Gráfico de dispersão de peso (wt) vs. milhas por galão (mpg)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['wt'], df['mpg'], color='green', edgecolor='black')
    plt.title('Peso vs. Milhas por Galão')
    plt.xlabel('Peso (mil libras)')
    plt.ylabel('Milhas por Galão (mpg)')
    plt.grid(True)
    plt.show()

    # Gráfico de barras do número de carros por número de cilindros (cyl)
    cyl_counts = df['cyl'].value_counts()

    plt.figure(figsize=(10, 6))
    cyl_counts.plot(kind='bar', color='purple', edgecolor='black')
    plt.title('Número de Carros por Número de Cilindros')
    plt.xlabel('Número de Cilindros')
    plt.ylabel('Número de Carros')
    plt.grid(True)
    plt.show()
