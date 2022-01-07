#generacion de codigos
def Esta(a, palabra):
    for letra in palabra:
        if letra==a:
            return True
    return False

def generaCodigo(destino, transporte):
    vocales=["a","e","i","o","u"]
    cadena=destino[0]+destino[1]
    cadena+="_"
    for letra in transporte:
        if not Esta(letra, vocales):
            cadena+=letra
    return cadena

n=int(input("Idique cuantos codigos quiere generar: "))
for i in range(n):
    destino=input("Ingrese Destino: ")
    transporte=input("Ingrese transporte: ")
    print(generaCodigo(destino, transporte))



