# Poderoso!
def EsPrimo(m):
    for i in range(2,m):
        if m%i == 0:
            return False
    return True

def Poderoso(n):
    for i in range(1,n+1):
        if n%i == 0 and EsPrimo(i):
            if n%(i*i) != 0:
                return False

    return True

n = int(input("Ingrese un numero"))
if Poderoso(n):
    print(n, "es poderoso")
else:
    print(n, "no es poderoso")
