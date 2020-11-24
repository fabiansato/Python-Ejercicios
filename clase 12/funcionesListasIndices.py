#Buscar el mínimo de una lista

def minimo(unaLista):
    min = unaLista[0]
    for recorro in range(len(unaLista)):
        if(min>unaLista[recorro]):
            min = unaLista[recorro]
    return(min)

def indiceMinimo(unaLista):
    min = unaLista[0]
    posmin = 0
    for recorro in range(len(unaLista)):
        if(min>=unaLista[recorro]):
            if(min>unaLista[recorro]):
                min = unaLista[recorro]
                posmin = recorro
                lista = []
                lista.append(posmin)
            else:
                lista.append(posmin)
    return(lista)

