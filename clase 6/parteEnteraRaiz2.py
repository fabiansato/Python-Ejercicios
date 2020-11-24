import math
print ("Este programa calcula parte entera de la raiz cuadrada")
n=int(input("Ingrese un numero"))
i=1
while(i*i<=n):
    i=i+1

print("La parte entera de la raiz cuadrada de",n,"es: ",i-1)

if(int(math.sqrt(n))==i-1):
    print("Bien resuelto")
else:
    print("ERROR")
