#Ejercicio 9 F
#a) Hacer un programa que, mediante un ciclo, pida al usuario 10 números naturales y los
#vaya multiplicando. Al terminar el ingreso de números deberá mostrar el resultado
#en pantalla.
#b) Hacer un programa que permita al usuario elegir un número n y luego multiplique los
#números naturales que el usuario vaya ingresando hasta haber ingresado n números.
#c) Hacer un programa que multiplique números naturales que el usuario vaya ingresando
#hasta que el número que ingrese sea 1.

a=5 ##cualquier valor distinto de 1
res=1
while(a!=1):
    a=int(input("Ingrese un numero"))
    res=res*a
print ("El resultado es:", res)