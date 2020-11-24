##Ejercicio 2 del 2do Parcial...Apuesta menor y única
n=int(input("Indique la cantidad de apuestas"))
lista=[]
for i in range(n):
    lista.append(float(input("Ingrese la apuesta")))
unicos=[]
cant=0
for i in range(n):
    unico=True
    for j in range(n):
        if (i!=j and lista[i]==lista[j]):
            unico=False
    if(unico==True):
        unicos.append(lista[i])
        cant=cant+1
menor=unicos[0]
for i in range(1,cant):
    if(unicos[i]<menor):
        menor=unicos[i]


print ("La menor y unica es", menor)

##ojo con recorrer solo los que estan despues del elemento
##ojo con elegir a la menor a la primera, hace falata elegir a la priemra y unica