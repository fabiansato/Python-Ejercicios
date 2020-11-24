def cantDivisores(n):
    cant=0
    for i in range(1,n+1):
        if n%i==0:
            cant+=1
    return cant

def esPrimo(n):
    if (cantDivisores(n)==2):
        return(True)
    else:
        return (False)


n=int(input("ingrese un numero: "))

if (esPrimo(n)):
    print("El numero ",n," es primo")
else:
    print("El numero ",n," NO es primo")