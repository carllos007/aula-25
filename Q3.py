def conta_strings(lista):
    contagem = 0
    for string in lista:
        if len(string) > 5:
            contagem += 1
    return contagem

lista = []
resultado = conta_strings(lista)
print(f"A lista inicial tem {resultado} strings com mais de 5 caracteres.")
resposta = input("Você deseja adicionar mais strings à lista? (S/N) ")
if resposta.upper() == "S" or "s":
    while True:
        nova_string = input("Digite uma nova string, ou 'sair' para encerrar: ")
        if nova_string.lower() == "sair":
            break
        lista.append(nova_string)
    resultado = conta_strings(lista)
    print(f"A lista atualizada tem {resultado} strings com mais de 5 caracteres.")
else:
    print("Obrigado por usar o programa.")
