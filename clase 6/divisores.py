print ("Este programa calcula la cantidad de divisores")
n=int (input("Ingresa un numero"))
divisores=0
for i in range(1,n+1):
    if(n%i==0):
        divisores=divisores+1

print ("la cantidad de divisores de ",n,"es",divisores)
