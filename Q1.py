def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

while True:
    entrada = input("Digite uma lista de números inteiros, separados por vírgulas, ou digite (sair) para parar: ")
    if entrada.lower() == "sair":
        break
    lista = [int(x) for x in entrada.split(",")]
    resultado = soma_pares(lista)
    print(f"A soma dos números pares na lista é {resultado}.")