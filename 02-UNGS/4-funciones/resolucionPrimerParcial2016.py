#1 a) nunca     0
#  b) afirmativa
#  c) 4
#  d) 34
######################################################################
#ejercicio 2#
cantHombres=int(input("Indique la cantidad de hombre de la fiesta"))
cantMujeres=int(input("Indique la cantidad de mujeres de la fiesta"))
dineroDisponible= int(input("Indique el dinero recaudado"))
eleccion=int(input("Indique 0 si la mayoria selecciono pizzas o 1 si la mayoria eligio empanadas"))
especial=170
seleccionada=140
muzzarella=100
empanadas=90 #la docena

if (eleccion==0):
    if (cantHombres*4+cantMujeres*2)//8*especial<=dineroDisponible:
        print("Arnaldito festeja con la mejor pizza, le sobra:",dineroDisponible-((cantHombres*4+cantMujeres*2)//8*especial))
    elif (cantHombres*4+cantMujeres*2)//8*seleccionada<=dineroDisponible:
        print("Arnaldito festeja con pizzas seleccionadas, le sobra:",dineroDisponible-((cantHombres*4+cantMujeres*2)//8*seleccionada))
    elif (cantHombres*4+cantMujeres*2)//8*muzzarella<=dineroDisponible:
        print("Arnaldito festeja con pizzas de muzzarella, le sobra:",dineroDisponible-((cantHombres*4+cantMujeres*2)//8*muzzarella))
    else:
            if (cantHombres*4+cantMujeres*2)//8*especial>dineroDisponible:
                print("Arnaldito festeja con pizzas de muzzarella, solicita:",(cantHombres*4+cantMujeres*2)//8*especial-dineroDisponible)
else:
    if (cantHombres*6+cantMujeres*4)//12*90<=dineroDisponible:
        print("Arnaldito festeja con empanadas, le sobra:",dineroDisponible-((cantHombres*6+cantMujeres*4)//12*empanadas))
    else:
        print("Arnaldito festeja con empanadas, solicta:",(cantHombres*6+cantMujeres*4)//12*empanadas-dineroDisponible)

######################################################################
#Ejercicio 3
nombre=input("Ingrese el nombre de la aerolinea") #una o dos palabras

abreviatura=""
espacios=0
for letra in nombre: #busco cantidad de palabras
    if letra==" ":
        espacios=espacios+1
pos=0
listo=False

if espacios==0: #una sola palabra
    for letra in nombre:
        if pos==0:
            abreviatura+=letra.upper()
        else:
            if not listo and letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u":
                abreviatura+=letra.upper()
                listo=True
        pos=pos+1
else: #dos palabras
    pos=0
    encontre=False  #no encontre el espacio vacio
    for letra in nombre:
        if pos==0:
            abreviatura+=letra.upper()
        else:
            if letra==" ":
                encontre= True
            elif encontre:
                abreviatura+=letra.upper()
                encontre=False
        pos=pos+1
print(abreviatura)

######################################################################
#Ejercicio 4

n=int(input("Ingrese un numero natural"))
while n < 4:
   n=int(input("Ingrese un numero natural"))
suma=0
for i in range (1,n+1,4):
    suma=suma+ i/2**1 + (i+1)/2**1 + (i+2)/2**2 + (i+3)/2**2

print("Suma:",suma)


#Ejercicio 4

n=int(input("Ingrese un numero natural"))
while n < 4:
   n=int(input("Ingrese un numero natural"))
suma=0
j=1
cont=0
for i in range (1,n+1):
    suma=suma+ i/2**j
    cont=cont+1
    if cont >=3 and j==1:
        j=2
        cont=0
    else:
        if cont >=3 and j==2:
            j=1
            cont=0
        else:
            cont=cont+1

print("Suma:",suma)



#Ejercicio 4

n=int(input("Ingrese la cantidad de terminos"))
suma=0
for i in range(1,n+1):
    if i%4==1 or i%4==2:
        suma=suma+i/(2**1)
        print(i,2)
    else:
        suma=suma+i/(2**2)
        print(i,4)
print(suma)
