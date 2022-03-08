#Ejercicio 11
#a) Hacer un programa que permita al usuario elegir un número n y luego muestre en
#pantalla todos los divisores de n.
#b) Hacer un programa que permita al usuario elegir dos números c y n y luego muestre
#en pantalla los primeros c divisores de n.
#c) Hacer un programa que permita al usuario elegir dos números c y n y luego muestre
#en pantalla los últimos c divisores de n.

n=int(input("Ingrese un numero"))
c=int(input("Ingrese un numero"))
cant=0
for i in range (1,n+1,1):
    if(n%i==0 and cant<c):
        print (i,"divide a ",n)
        cant=cant+1

if (cant<c):
    print(n,"no tiene",c,"divisores, solo: ", cant)