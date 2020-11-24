palabra=input("Ingrese la Palabra")

listaP=list(palabra)
print(listaP)

letra=input("Ingrese la letra")
print(letra)

pos=0
for i in palabra:
    if (i==letra):
        print("La posicion es:",pos+1,"esta", letra)
    pos=pos+1

#opcion2
#for i in range(len(palabra)):
#    if(letra==listaP[i]):
#        print("La posicion es:",i+1,"esta", letra)
