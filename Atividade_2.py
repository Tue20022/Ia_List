def contar_vogais(texto):
    """
    Conta o número de vogais em um texto.

    Args:
        texto (str): O texto no qual as vogais serão contadas.

    Returns:
        int: O número de vogais no texto.
    """
    vogais = "aeiouAEIOU"
    contador = 0

    for char in texto:
        if char in vogais:
            contador += 1

    return contador

def main():
    texto = ""
    while True:
        linha = input("Digite uma linha de texto e caso queira sair pressione Enter: ")
        if not linha:
            break
        texto += linha + "\n"

    total_vogais = contar_vogais(texto)
    print(f"Total de vogais no texto: {total_vogais}")

if __name__ == "__main__":
    main()
