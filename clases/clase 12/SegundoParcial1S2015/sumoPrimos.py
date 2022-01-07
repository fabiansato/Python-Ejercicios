def esPrimo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def sumoPrimos(n):
    i=2
    suma=0
    cont=0

    while(suma<=n):
        while( not esPrimo(i)):
            i=i+1
        suma=suma+i
        cont=cont+1
        i=i+1
    return cont

n=15
print(sumoPrimos(n))



