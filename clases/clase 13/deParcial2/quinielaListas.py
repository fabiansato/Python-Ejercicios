import random
lista1= [2,15 , 5 ,89,2 ,91,98 ,89, 2 ,9]
lista2= [2,2.5,0.5,3 ,12,5 ,4.5,5 ,2.5,3]

ganador=random.randint(0,99)  #para que sea mas divertido
paga=70
cant=0
recaudacion=0
perdida=0
for i in range(len(lista1)):
    if (lista1[i]==ganador):
        print("Apostador", i+1,"Gano",lista2[i]*paga," pesos")
        if cant==0:
            unico=i
        cant+=1
        perdida+=lista2[i]*paga
    recaudacion+=lista2[i]
if cant==1:
    print ("por ser el unico gana",lista2[unico]*70*1.1, "en total")
    perdida=lista2[unico]*70*1.1  #no acumula pisa lo anterior
saldo=recaudacion-perdida
if saldo>=0:
    print("Gano: ", saldo)
else:
    print("Perdio: ", saldo)

