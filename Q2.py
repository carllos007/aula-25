def palindromo(string):
    string = string.lower()
    inversa = string[::-1]
    if string == inversa:
        return True
    else:
        return False

while True:
    entrada = input("Digite uma palavra ou frase, ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    resultado = palindromo(entrada)
    if resultado:
        print(f"A palavra ou frase '{entrada}' é um palíndromo.")
    else:
        print(f"A palavra ou frase '{entrada}' não é um palíndromo.")
