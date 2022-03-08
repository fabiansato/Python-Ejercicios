def esPrimo(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True

def proxPrimos(m,p):
    i=m+1
    cant=0
    primos=[]
    while cant<3:
        if esPrimo(i):
            cant+=1
            primos.append(i)
        i=i+1
    return primos

print(proxPrimos(8,3))
