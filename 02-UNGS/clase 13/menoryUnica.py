#primero buscamos los unicos
def unicos(lista):
    listaNueva = []
    for i in range(len(lista)):
        if cantApariciones(lista[i],lista)==1:
            listaNueva.append(lista[i])
    return (listaNueva)

def cantApariciones(elemento, lista):
    contador = 0
    for i in range(len(lista)):
        if elemento == lista[i]:
            contador+=1
    return(contador)

#despues, de los unicos, busco el mas chico
def minimo(lista):
    masChico = lista[0]
    for i in range(len(lista)):
        if lista[i] < masChico:
            masChico = lista[i]
    return(masChico)

lista = [0.2, 0.2, 0.2, 0.3, 1.2, 0.3, 0.8, 0.5, 0.5, 2, 0.9]
vacia = []
menorYUnico = minimo(unicos(vacia))
print(menorYUnico)