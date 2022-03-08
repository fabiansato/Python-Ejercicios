#Ejercicio 12 F
#Hacer un programa que reciba un número m y determine el primer n para el cual la suma
#1+2+:::+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
#10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

m=int(input("Ingrese un numero"))
n=1
suma=0
while (suma<=m):
    print (n,end=" ")
    suma=suma+n
    n=n+1

print("\nRespuesta: ",n-1)