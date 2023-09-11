def maximo(lista):
    if not lista:
        return None
    minu = lista[0]
    for numero in lista:
        if numero > maximo:
            minu = numero
    return minu

lista = []
while True:
    n = int(input("digite um numero :"))
    if n == 0:
        break
    else:
        lista.append(n)

resultado = maximo(lista)
print (resultado)