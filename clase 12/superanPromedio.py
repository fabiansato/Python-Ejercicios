#Hacer un programa que solicite una cantidad de números reales e indique al usuario aquellos que superan el promedio.
def superanPromedio(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]

    promedio=suma/len(lista)

    listaN=[]
    for i in range(len(lista)):
        if lista[i]>promedio:
            listaN.append(lista[i])
    return listaN

lista=[2,2.5,0.5,3,12,5,4.5,5,2.5,3]
print(superanPromedio(lista))
