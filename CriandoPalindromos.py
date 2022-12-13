# Criando Palindromos

def palindromo_com_repeticao():
    palavra = input().lower().strip()

    palavra_teste = []
    palavra_invertida = []

    # laço que gera uma lista da string de entrada
    for letra in range(0, len(palavra)):
        palavra_teste.append(palavra[letra])

    # Laço que inverte a string de entrada
    for letra in range(len(palavra) - 1, -1, -1):
        palavra_invertida.append(palavra[letra])

    print(f"O inverso de {palavra_teste} é {palavra_invertida}")

    if palavra_teste == palavra_invertida:
        print("A palavra é um palindromo")
    else:
        print("A palavra não é um palindromo")


def palindromo_sem_repeticao():
    palavra = input().lower().strip()

    # Inversão da string de entrada
    palavra_invertida = palavra[::-1]

    print(f"O inverso de {palavra.capitalize()} é {palavra_invertida.capitalize()}")

    if palavra_invertida == palavra:
        print("A palavra é um palindromo")
    else:
        print("A palavra não é um palindromo")
