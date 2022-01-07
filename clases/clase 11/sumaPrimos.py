def cantDivisores(a):
    cant=0
    for i in range(1,a+1):
        if(a%i==0):
            cant+=1
    return(cant)

def esPrimo(a):
    if(cantDivisores(a)==2):
        return(True)
    else:
        return(False)

def sumaPrimo(z):
    suma=0
    for i in range(1,z+1):
        if(esPrimo(i)):
            suma+=i
    return(suma)



num=int (input("Ingrese un numero"))
print(sumaPrimo(num))