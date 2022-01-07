def union1(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
    for i in range(len(lista2)):
        lista3.append(lista2[i])
    return(quitarRepetidos(lista3))

def union2(lista1,lista2):
    lista3=lista1+lista2
    return(quitarRepetidos(lista3))

def union3(lista1,lista2):
    return(quitarRepetidos(lista1+lista2))
