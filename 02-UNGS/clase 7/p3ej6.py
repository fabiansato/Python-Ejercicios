#Ejercicio 6
#Hacer un programa que reciba un número n y muestre todas las potencias de 2 menores a n.
#Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8 16.
n=int (input("Ingrese un numero"))
resultado=1
while (resultado<n):
    print (resultado,end=" ")
    resultado=resultado*2

