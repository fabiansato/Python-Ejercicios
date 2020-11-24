nombre=input("dame nombre")
apellido=input("dame apellido")
documento=input("dame D.N:I")
legajo="" # tres primeros de dni + _ tres letras ap _1 nom ult nom
cont=0
for letra in documento:
    if(cont<3):
        legajo=legajo+letra
        cont=cont+1
legajo=legajo+"_"
cont=0
for letra in apellido:
    if(cont<3):
        legajo=legajo+letra
        cont=cont+1
print(legajo)
cont=0
for letra in nombre:
    if(cont==0 or cont==len(nombre)-1):
        legajo=legajo+letra
    cont=cont+1
print ("el legajo de la persona",nombre,apellido,"es:",legajo)










