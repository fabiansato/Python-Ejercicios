#Hacer un programa que calcule la siguiente suma:  …  (5 términos)
#Solicitar al usuario la cantidad de términos que desea sumar.

n=int(input("Ingrese un numero natural"))

acum=0
for i in range (1,n+1):
    acum=acum + ((-1)**(i+1))*i/((i+1)**i)
    print ((-1)**(i+1)*i,"/(",i+1,"**",i,")")
print(acum)