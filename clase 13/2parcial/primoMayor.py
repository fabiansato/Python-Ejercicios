def esPrimo(n):
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
    return primo

def primoMayor(n):
    numero=int(n)+1 #tomo el proximo entero
    while(not esPrimo(numero)):
        numero+=1
    return numero

print(primoMayor(25.7))