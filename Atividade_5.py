import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Função principal que cria gráficos de temperatura para Macaé e Rio de Janeiro.
    """
    # Dados de temperaturas para Macaé e Rio de Janeiro
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    temperatura_minima_macae = [20, 21, 22, 20, 18, 16, 16, 17, 18, 19, 20, 21]
    temperatura_maxima_macae = [28, 29, 30, 28, 26, 24, 23, 24, 25, 26, 27, 28]
    temperatura_media_macae = [(min + max) / 2 for min, max in zip(temperatura_minima_macae, temperatura_maxima_macae)]

    temperatura_minima_rio = [22, 23, 24, 22, 20, 18, 18, 19, 20, 21, 22, 23]
    temperatura_maxima_rio = [30, 31, 32, 30, 28, 26, 26, 27, 28, 29, 30, 31]
    temperatura_media_rio = [(min + max) / 2 for min, max in zip(temperatura_minima_rio, temperatura_maxima_rio)]

    plt.figure(figsize=(10, 5))

    # Temperaturas de Macaé
    plt.plot(meses, temperatura_minima_macae, marker='o', linestyle='-', label='Macaé - Mínima')
    plt.plot(meses, temperatura_maxima_macae, marker='o', linestyle='-', label='Macaé - Máxima')
    plt.plot(meses, temperatura_media_macae, marker='o', linestyle='-', label='Macaé - Média')

    # Temperaturas do Rio de Janeiro
    plt.plot(meses, temperatura_minima_rio, marker='o', linestyle='-', label='Rio de Janeiro - Mínima')
    plt.plot(meses, temperatura_maxima_rio, marker='o', linestyle='-', label='Rio de Janeiro - Máxima')
    plt.plot(meses, temperatura_media_rio, marker='o', linestyle='-', label='Rio de Janeiro - Média')

    plt.title('Temperaturas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Temperatura (°C)')
    plt.xticks(meses)
    plt.legend()
    plt.grid(True)

    # Salvar o gráfico como figura
    plt.savefig('temperaturas.png')

    plt.show()

    plt.figure(figsize=(10, 5))

    bar_width = 0.35
    index = np.arange(len(meses))

    plt.bar(index - bar_width/2, temperatura_media_macae, bar_width, label='Macaé', color='b')
    plt.bar(index + bar_width/2, temperatura_media_rio, bar_width, label='Rio de Janeiro', color='g')

    plt.title('Temperaturas Médias Mensais - Macaé vs. Rio de Janeiro')
    plt.xlabel('Mês')
    plt.ylabel('Temperatura Média (°C)')
    plt.xticks(index, meses)
    plt.legend()
    plt.grid(True)

    # Salvar o gráfico como figura
    plt.savefig('temperaturas_medias.png')

    plt.show()

if __name__ == "__main__":
    main()
