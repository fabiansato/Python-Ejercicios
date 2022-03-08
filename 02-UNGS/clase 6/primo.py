##print ("Este programa indica si un numero es primo")
##n=int (input("Ingresa un numero"))
##divisores=0
##for i in range(1,n+1):
##    if(n%i==0):
##        divisores=divisores+1
##if(divisores==2):
##    print ("El numero ",n,"es Primo")
##else:
##    print ("El numero ",n,"NO es Primo")


print ("Este programa indica si un numero es primo")
n=int (input("Ingresa un numero"))
i=2
esPrimo=True
while(esPrimo and i<(n//2)+1):
    if (n%i==0):
        esPrimo=False
    i=i+1

if(esPrimo):
    print ("El numero ",n,"es Primo")
else:
    print ("El numero ",n,"NO es Primo")