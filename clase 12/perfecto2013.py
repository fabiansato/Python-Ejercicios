def sumaDivProp(n):
    suma=0
    for i in range(1,n):
        if(n%i==0):
            suma += i
    return(suma)

def esPerfecto(n):
    return(n==sumaDivProp(n)):

numero = int(input("Ingrese un numero"))
if(esPerfecto(numero)):
    print(numero,"es perfecto")
else:
    print(numero,"no es perfecto")
