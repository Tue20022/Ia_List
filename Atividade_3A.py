import pandas as pd
import matplotlib.pyplot as plt

def ler_dados():
    """
    Lê os dados do arquivo Excel e extrai informações relevantes.

    Returns:
        Tuple: Uma tupla contendo quatro listas - months, min_temperatures, max_temperatures e avg_temperatures.
    """
    # Lê os dados do arquivo Excel
    df = pd.read_excel("Dados_climaticos_historicos.xlsx", sheet_name="Historico_Clima_Macae", header=None)
    # Extrair nomes dos meses da quarta linha (linha de índice 3)
    months = df.iloc[3, 1:13].tolist()
    
    # Extrair dados de temperaturas das linhas 5, 6 e 7
    min_temperatures = df.iloc[4, 1:13].tolist()
    max_temperatures = df.iloc[5, 1:13].tolist()
    avg_temperatures = df.iloc[6, 1:13].tolist()
    
    return months, min_temperatures, max_temperatures, avg_temperatures

def estrutura_de_dados(months, min_temperatures, max_temperatures, avg_temperatures):
    """
    Cria uma estrutura organizada de dados a partir das informações de temperaturas.

    Args:
        months (list): Lista de nomes dos meses.
        min_temperatures (list): Lista das temperaturas mínimas.
        max_temperatures (list): Lista das temperaturas máximas.
        avg_temperatures (list): Lista das temperaturas médias.

    Returns:
        dict: Um dicionário onde as chaves são os meses e os valores são dicionários com as temperaturas correspondentes.
    """
    climatic_data = {}
    for i in range(len(months)):
        month_data = {
            "Tmin": min_temperatures[i],
            "Tmax": max_temperatures[i], 
            "Tmedia": avg_temperatures[i]
        }
        climatic_data[months[i]] = month_data
    return climatic_data

def arquivo_ascii(months, min_temperatures, max_temperatures, avg_temperatures):
    """
    Cria um arquivo ASCII (txt) com os dados climáticos.

    Args:
        months (list): Lista de nomes dos meses.
        min_temperatures (list): Lista das temperaturas mínimas.
        max_temperatures (list): Lista das temperaturas máximas.
        avg_temperatures (list): Lista das temperaturas médias.
    """
    # Cria o arquivo ASCII (txt)
    with open("dados_climaticos_macae.txt", "w") as file:
        file.write("Mês Tmed Tmin Tmax\n")
        for i in range(len(months)):
            file.write(f"{months[i]} {min_temperatures[i]} {max_temperatures[i]} {avg_temperatures[i]}\n")

def main():
    """
    Função principal que executa todas as operações.

    Chama as funções ler_dados, estrutura_de_dados e arquivo_ascii para processar os dados climáticos
    e exibe informações relevantes.
    """
    months, min_temperatures, max_temperatures, avg_temperatures = ler_dados()
    
    climatic_dict = estrutura_de_dados(months, min_temperatures, max_temperatures, avg_temperatures)

    # Escrever os dados em um arquivo ASCII
    arquivo_ascii(months, min_temperatures, max_temperatures, avg_temperatures)
    
    # Exibir o conteúdo do dicionário
    print("Dicionário de dados climáticos:")
    for month, data in climatic_dict.items():
        print(f"{month}: Tmin={data['Tmin']}, Tmax={data['Tmax']}, Tmedia={data['Tmedia']}")

    # Exibir a temperatura média de julho
    july_avg_temperature = climatic_dict["Julho"]["Tmedia"]
    print(f"Temperatura média do mês de julho: {july_avg_temperature}")

if __name__ == "__main__":
    main()
