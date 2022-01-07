print ("Este programa calcula la cantidad de cifras de un numero")
n=int(input("Ingrese un numero"))
if n==0:
    print("El numero tiene 1 cifra")
else:
    if n<0:
        n=n*(-1)
    cont=0
    while(n>=1):
        n=n/10
        cont=cont+1
    print("El numero tiene",cont,"cifras")