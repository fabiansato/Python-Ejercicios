import random

print("La Quiniela")
elegido = int(input("Ingrese un numero"))
apuesta = float(input("Ingrese el monto de la apuesta"))
aleatorio = random.choice(range(0,100,1))
premio = 70

if(elegido == aleatorio):
    print("Gane: ", premio*apuesta)
else:
    print("Segui participando :-) ")
    print("El numero era: ", aleatorio)