def sumaDivProp(n):
    suma=0
    for i in range(1,n):
        if(n%i==0):
            suma += i
    return(suma)


numero = int(input("Ingrese un numero"))
if(sumaDivProp(numero)==numero):
    print(numero,"es perfecto")
else:
    print(numero,"no es perfecto")
