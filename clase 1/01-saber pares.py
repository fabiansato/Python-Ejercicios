#ingresar un numero y saber si es par

nombre=input("Ingrese su nombre")
numero=int(input("Ingrese un numero entero"))


if numero%2 == 0:
    print (numero,"es par",nombre)

else:
    print (numero,"es impar",nombre)