def esta(entero,lista):
    for i in lista:
        if(i == entero):
            return(True)
    return(False)

def interseccion(lista1,lista2):
    lista3 = []
    for i in lista1:
        if(esta(i,lista2)):
            lista3.append(i)
    return(lista3)

def divisores(a):
    lista=[]
    for i in range(1,a+1):
        if (a%i==0):
            lista.append(i)
    return lista

def maximo(lista):
    max=lista[0]
    for elem in lista:
        if max<elem:
            max=elem
    return max


def MCD(a,b):
    divA=divisores(a)
    divB=divisores(b)
    divComunes=interseccion(divA,divB)
    MCD= maximo(divComunes)
    return (MCD)

a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))

print ("El MCD entre ", a," y ", b," es: ",MCD(a,b))


