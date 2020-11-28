import random

def esta(a,lista):
    for elem in lista:
        if elem==a:
            return True
    return False


def sonCoprimos(n,m):
    for i in range(2,n+1):
        if n%i==0 and m%i==0:
            return False
    return True

def sumaFraccionesCoprimas(n):
    a=random.randrange(1,100)
    b=random.randrange(1,100)
    suma=0
    lista=[]
    for i in range(n):
        while not sonCoprimos(a,b) or esta(a/b,lista):
            a=random.randrange(1,100)
            b=random.randrange(1,100)
        lista.append(a/b)
        #print(a,b)
        suma+=a/b
    return suma

n=int(input("Indique la cantidad de terminos que desea: "))
suma=sumaFraccionesCoprimas(n)
print(suma)






