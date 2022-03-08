def divisoresP(n): ##divisores Propios
    suma=0
    for i in range (1,n//2+1,1):
        if(n%i==0):
            suma=suma+i
    return suma

def perfecto(n):
    if(n==divisoresP(n)):
        return True
    else:
        return False


a=int(input("Ingrese un numero"))
b=divisoresP(a)
print (b)
while (b>1 and not perfecto(b)):
    b=divisoresP(b)
    print (b)

if(perfecto(b)):
    print ("El numero",a," SI es Ambicioso")
else:
    print ("El numero",a,"NO es Ambicioso")