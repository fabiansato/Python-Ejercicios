numero=int(input("ingresar un numero"))
div=1
cont=0

while(div<=numero):
    if(numero%div==0):
        cont=cont+1
    div=div+1
if(cont==2):
    print("el numero", numero, "es primo")
else:
    print("el numero", numero, "_no_ es primo")

##
##

numero=int(input("ingresar un numero"))
cont=0
for div in range(1,numero+1):
    if(numero%div==0):
        cont=cont+1
if(cont==2):
    print("el numero", numero, "es primo")
else:
    print("el numero", numero, "_no_es primo")