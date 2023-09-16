# Função para ler N números float
def ler_numeros_float(n):
    """
    Lê N números float digitados pelo usuário e os retorna como uma lista.

    Args:
        n (int): A quantidade de números float a serem lidos.

    Returns:
        list: Uma lista contendo os números float lidos.
    """
    numeros = []
    for i in range(n):
        numero = float(input(f"Digite o {i + 1}º número float: "))
        numeros.append(numero)
    return numeros

# Função para mostrar os valores digitados
def mostrar_valores_originais(numeros):
    """
    Mostra os valores originais (float) em uma lista.

    Args:
        numeros (list): Uma lista de números float.
    """
    print("Valores digitados (originais):")
    for numero in numeros:
        print(numero)

# Função para mostrar os pares
def mostrar_valores_indices_pares(numeros):
    """
    Mostra os valores originais (float) em índices pares de uma lista.

    Args:
        numeros (list): Uma lista de números float.
    """
    print("Valores originais em índices pares:")
    for i in range(len(numeros)):
        if i % 2 == 0:
            print(numeros[i])

# Função para mostrar os ímpares
def mostrar_valores_indices_impares(numeros):
    """
    Mostra os valores originais (float) em índices ímpares de uma lista.

    Args:
        numeros (list): Uma lista de números float.
    """
    print("Valores originais em índices ímpares:")
    for i in range(len(numeros)):
        if i % 2 != 0:
            print(numeros[i])

# Função para arredondar os valores para 1 casa decimal
def arredondar_valores(numeros):
    """
    Arredonda os valores float em uma lista para 1 casa decimal e retorna a lista resultante.

    Args:
        numeros (list): Uma lista de números float.

    Returns:
        list: Uma lista de números float arredondados para 1 casa decimal.
    """
    valores_arredondados = [round(numero, 1) for numero in numeros]
    return valores_arredondados

# Função para calcular o somatório e arredondar para 2 casas decimais
def calcular_somatorio(numeros):
    """
    Calcula o somatório dos valores float em uma lista e arredonda o resultado para 2 casas decimais.

    Args:
        numeros (list): Uma lista de números float.

    Returns:
        float: O somatório arredondado para 2 casas decimais.
    """
    somatorio = sum(numeros)
    somatorio_arredondado = round(somatorio, 2)
    return somatorio_arredondado

# Função para mostrar valores inteiros em binário, octal e hexadecimal
def mostrar_valores_inteiros_base(numeros):
    """
    Mostra os valores inteiros em binário, octal e hexadecimal.

    Args:
        numeros (list): Uma lista de números float.
    """
    print("Valores inteiros em binário, octal e hexadecimal:")
    for numero in numeros:
        numero_inteiro = int(numero)
        print(f"Valor: {numero_inteiro}")
        print(f"Binário: {bin(numero_inteiro)}")
        print(f"Octal: {oct(numero_inteiro)}")
        print(f"Hexadecimal: {hex(numero_inteiro)}")
        print()

# Main
def main():
    """
    Função principal que executa todas as operações.

    Solicita ao usuário a quantidade de números float, lê os números, realiza diversas operações e exibe os resultados.
    """
    n = int(input("Digite a quantidade de números float que deseja inserir: "))
    numeros = ler_numeros_float(n)

    mostrar_valores_originais(numeros)
    mostrar_valores_indices_pares(numeros)
    mostrar_valores_indices_impares(numeros)

    valores_arredondados = arredondar_valores(numeros)
    print("Valores arredondados para 1 casa decimal:")
    for valor in valores_arredondados:
        print(valor)

    somatorio_arredondado = calcular_somatorio(numeros)
    print(f"Somatório arredondado para 2 casas decimais: {somatorio_arredondado}")

    mostrar_valores_inteiros_base(numeros)

if __name__ == "__main__":
    main()
