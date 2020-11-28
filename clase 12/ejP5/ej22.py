from frecuencia import*
from interseccion import*
def ej22(cadena):
    lista=list(cadena)
    mostrados=[]
    i=0
    while i<len(lista):
        if not esta (mostrados,lista[i]):

            print(lista[i], "=",frecuencia(lista, lista[i]))
            mostrados.append(lista[i])
        i+=1

ej22("conocido")


