from misFunciones import *

def factPrimos(n):
    for i in range(2,n+1):
        if n%i==0 and esPrimo(i):
            print(i,end=" ")


n=int(input("ingrese un numero"))

factPrimos(n)

