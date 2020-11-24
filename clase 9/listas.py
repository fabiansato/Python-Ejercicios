import random
def funcEstaEnLaLista (Lista ,numero):
    bandera=False
    for elemento in Lista:
        if (elemento == numero):
            bandera=True
    return bandera

def funcCantApariciones (Lista , numero):
    cont=0
    for i in range (len(Lista)):
        if(Lista[i]==numero):
            cont+=1
    return cont

def funcEsta2 (Lista,Num):
    bandera=True
    if(funcCantApariciones(Lista,Num)==0):
        bandera=False
    return bandera
# Programa Principal

def funcMaximoElemento(ListaDeNumeros):
    maximo=ListaDeNumeros[0]
    for i in range (len(ListaDeNumeros)):
        if(ListaDeNumeros[i]>maximo):
            maximo=ListaDeNumeros[i]
    return maximo

def funcQuitarRep (Lista):
    listanueva=[]
    for i in range (len(Lista)):
        if(not (funcEsta2(listanueva,Lista[i]))):
            listanueva.append(Lista[i])
    return listanueva

def funcSacaRep (Lista):
    i=0
    while(i<len(Lista)):
        if((funcCantApariciones(Lista,Lista[i])>1)):
            Lista.pop(i)
        else:
            i=i+1
    return Lista



# Programa Principal

ListaDeNumeros = []
for i in range (10):
   var= random.randrange(5)
   ListaDeNumeros.append(var)
print(ListaDeNumeros)



#print(funcEsta2(ListaDeNumeros,4))
#print(funcCantApariciones(ListaDeNumeros,4))
#print(funcMaximoElemento(ListaDeNumeros))
#print(funcQuitarRep(ListaDeNumeros))
print(funcSacaRep(ListaDeNumeros))




