a=int (input("Ingrese un numero"))
b=int (input("Ingrese otro numero"))

print("Los divisores pares de",a,"son:",end=" ")
sumaParesA=0
for i in range(1,a):
   if (a%i==0 and i%2==0):
            sumaParesA=sumaParesA+i
            print (i,end=" ")

print("\nLos divisores impares de",b,"son:",end=" ")
sumaImparesB=0
for i in range(1,b):
    if (b%i==0 and i%2!=0):
        sumaImparesB=sumaImparesB+i
        print (i,end=" ")

if (sumaParesA == sumaImparesB):
    print ("\nSon amistosos",a,b)
else:
    print ("\nNO son amistosos",a,b)

