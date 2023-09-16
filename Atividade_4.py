import numpy as np
import pandas as pd

def ler_dados():
    """
    Lê os dados climáticos de um arquivo Excel e converte-os em um NumPy array.

    Returns:
        Tuple: Uma tupla contendo uma lista de meses e um array NumPy contendo temperaturas.
    """
    dataframe = pd.read_excel("C:\\Users\\Usuario\\Desktop\\Faculdade\\P7\\SO2\\pythonProject\\Dados_climaticos_historicos.xlsx", sheet_name="Historico_Clima_Rio_de_Janeiro", header=None)

    # Extraindo nomes dos meses da quarta linha (linha de índice 3)
    months = dataframe.iloc[3, 1:13].tolist()

    # Extrair apenas as colunas de interesse (Temperatura média, mínima e máxima) e convertendo para float
    min_temperatures = [float(str(value).replace(',', '.')) for value in dataframe.iloc[6, 1:13]]
    max_temperatures = [float(str(value).replace(',', '.')) for value in dataframe.iloc[7, 1:13]]
    avg_temperatures = [float(str(value).replace(',', '.')) for value in dataframe.iloc[5, 1:13]]

    # Criar um NumPy array com as temperaturas organizadas por colunas
    temperaturas = np.array([min_temperatures, max_temperatures, avg_temperatures]).T  # 'T' para transpor as colunas para linhas

    return months, temperaturas

def criar_arquivo_ascii(months, temperaturas):
    """
    Cria um arquivo ASCII com os dados de temperaturas.

    Args:
        months (list): Uma lista de meses.
        temperaturas (np.ndarray): Um array NumPy contendo as temperaturas.
    """
    with open("temperaturas_rio.txt", "w") as file:
        file.write("Mês Tmin Tmax Tmed\n")
        for i in range(len(months)):
            file.write(f"{months[i]}\t{temperaturas[i, 0]}\t{temperaturas[i, 1]}\t{temperaturas[i, 2]}\n")

def main():
    months, temperaturas = ler_dados()
    criar_arquivo_ascii(months, temperaturas)
    
    print("Meses:", months)
    print("Temperaturas:")
    print(temperaturas)

    print("Dimensão (shape) do array de temperaturas:", temperaturas.shape)
    print("Máximo valor na coluna de temperatura média:", np.max(temperaturas[:, 2]))
    print("Mínimo valor na coluna de temperatura média:", np.min(temperaturas[:, 2]))

    # Restante das operações com NumPy...
    # (Você já fez isso corretamente)
    
if __name__ == "__main__":
    main()
