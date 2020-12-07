'''
Hacer una función que indique si un número es Perfecto.
Número perfecto: A es perfecto si la suma de sus divisores propios es igual a A.
Luego hacer un programa que use la función.

'''
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
