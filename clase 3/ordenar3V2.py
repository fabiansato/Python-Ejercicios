a = int(input("Ingrese una variable"))
b = int(input("Ingrese una variable"))
c = int(input("Ingrese una variable"))

# asumimos que los tres son distintos
#busco mayor
if a>b and a>c:
    mayor=a
elif b>a and b>c:
    mayor=b
else:
    mayor=c

#busco medio
if a>b and a<c or a<b and a>c:
    medio=a
elif b>a and b<c or b<a and b>c:
    medio=b
else:
    medio=c

#busco menor
if a<b and a<c:
    menor=a
elif b<a and b<c:
    menor=b
else:
    menor=c

print("El mas grande es ", mayor,
    "\nEl del medio es ", medio,
    "\nEl mas chico es", menor)