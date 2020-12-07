from FuncionesDePrimo import *

def esPrimo2(n):
    primo=True
    i=2
    while(primo and i<=n//2):
        if n%i==0:
            primo=False
        i=i+1
    return primo



for n in range(2,100000):
    if esPrimo2(n):
        print(n, end=(" "))
