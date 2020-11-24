def esPrimo(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def factores(n):
    lista=[]
    i=2
    while i<=n:
        if(n%i==0 and esPrimo(i)):
            lista.append(i)
            n=n/i
        else:
            i=i+1
    return lista

print(factores(24))

