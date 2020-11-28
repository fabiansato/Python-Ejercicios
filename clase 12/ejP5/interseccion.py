from frecuencia import*
def esta(lista, n):
    return frecuencia(lista, n)>0

def interseccion(lista1, lista2):
    lis=[]
    for numero in lista1:
        if esta(lista2, numero):
            lis.append(numero)
    return lis

a=[1,3,5,7,9,11]
b=[2,4,-1,3,9,7,11]
print (interseccion(a,b))

