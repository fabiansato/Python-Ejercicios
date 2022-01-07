def esPrimo(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def funcion(a,b):
    for i in range(2,a+1):
        if a%i==0 and b%i==0 and esPrimo(i):
            return i
    return False

print (funcion(20,24))