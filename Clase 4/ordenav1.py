a = int(input("Ingrese una variable"))
b = int(input("Ingrese una variable"))
c = int(input("Ingrese una variable"))

# asumimos que los tres son distintos

if( a>b and a>c):
    mayor = a
else:
    if( b>a and b>c):
        mayor = b
    else:
        mayor = c

if( a<b and a<c):
    menor = a
else:
    if( b<a and b<c):
        menor = b
    else:
        menor = c

if( menor<a and a<mayor ):
    medio = a
else:
    if( menor<b and b<mayor ):
        medio = b
    else:
        medio = c

print("El mas grande es ", mayor,
    "\nEl del medio es ", medio,
    "\nEl mas chico es", menor)