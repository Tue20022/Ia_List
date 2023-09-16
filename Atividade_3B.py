import matplotlib.pyplot as plt

def ler_dados_climaticos(nome_arquivo):
    """
    Lê os dados climáticos de um arquivo de texto e retorna listas de meses, temperaturas mínimas,
    temperaturas máximas e temperaturas médias.

    Args:
        nome_arquivo (str): O caminho para o arquivo de dados climáticos.

    Returns:
        tuple: Uma tupla contendo quatro listas - meses, min_temperatures, max_temperatures e avg_temperatures.
    """
    months = []
    min_temperatures = []
    max_temperatures = []
    avg_temperatures = []

    with open(nome_arquivo, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:  # Ignorar a primeira linha (cabeçalho)
            data = line.strip().split()  # Dividir a linha em palavras
            months.append(data[0])
            min_temperatures.append(float(data[1]))
            max_temperatures.append(float(data[2]))
            avg_temperatures.append(float(data[3]))

    return months, min_temperatures, max_temperatures, avg_temperatures

def criar_dicionario_dados_climaticos(months, min_temperatures, max_temperatures, avg_temperatures):
    """
    Cria um dicionário de dados climáticos a partir das listas de meses e temperaturas.

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

def main():
    nome_arquivo = "C:\\Users\\Usuario\\Desktop\\Faculdade\\P7\\SO2\\pythonProject\\dados_climaticos_macae.txt"
    
    months, min_temperatures, max_temperatures, avg_temperatures = ler_dados_climaticos(nome_arquivo)
    
    climatic_dict = criar_dicionario_dados_climaticos(months, min_temperatures, max_temperatures, avg_temperatures)

    # Exibir o conteúdo do dicionário
    print("Dicionário de dados climáticos:")
    for month, data in climatic_dict.items():
        print(f"{month}: Tmin={data['Tmin']}, Tmax={data['Tmax']}, Tmedia={data['Tmedia']}")

    # Exibir a temperatura média de julho
    july_avg_temperature = climatic_dict.get("Julho", {}).get("Tmedia", "N/A")
    print(f"Temperatura média do mês de julho: {july_avg_temperature} °C")

    # Plotar um gráfico de temperatura
    plt.figure(figsize=(10, 6))
    plt.plot(months, min_temperatures, marker='o', label='Tmin')
    plt.plot(months, max_temperatures, marker='o', label='Tmax')
    plt.plot(months, avg_temperatures, marker='o', label='Tmedia')
    plt.xlabel('Meses')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperaturas Mensais')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()
