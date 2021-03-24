def maximosRelativos(lista):
    listaNueva = []
    for i in range(1, len(lista)-1):
        if (lista[i] > lista[i-1] and lista[i] > lista[i+1]):
            listaNueva.append(lista[i])
    return(listaNueva)