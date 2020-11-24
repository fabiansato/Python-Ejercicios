import random

a=random.randrange(1,100)
d=float(input("Ingrese el monto: "))
pago=70*d

n=a-1   #asignamos un valor a n para que entre al ciclo
cont=0
while( a != n and cont<3):
    n=int(input("Ingrese un numero: "))

    if( a==n ):
        print("Gano $", pago)
    else:
        print("Lo siento, trata otra vez")
        if( n<a ):
            print("El numero es mayor")
        else:
            print("El numero es menor")
    cont+=1

print("El numero sorteado es: ", a)