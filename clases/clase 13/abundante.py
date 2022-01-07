def sumaDiv(n):
    suma=0
    for i in range (1,n//2+1):
        if (n%i==0):
            suma=suma+i
    return suma

def abundante(n):
    if(sumaDiv(n)>n):
        return True
    else:
        return False

n=int(input("Ingrese un numero"))
if(abundante(n)):
    print ("El numero",n,"es abundante")
else:
    print ("El numero",n," NO es abundante")

