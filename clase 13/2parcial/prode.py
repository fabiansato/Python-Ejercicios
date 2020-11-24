def CantidadDeAciertos(listaResultado, listaApostada):
    cont=0
    for i in range(len(listaResultado)):
        if listaResultado[i]==listaApostada[i]:
            cont+=1
    return cont

def controlProde(fecha):
    listaResultados= Resultado(fecha)
    apostadores= Nombres(fecha)
    listaGanadores=[]
    for dni in apostadores:
        listaApostada= Apuesta(dni, fecha)
        aciertos= CantidadDeAciertos(listaResultados, listaApostada)
        if aciertos>=7:
            listaGanadores.append(DNI)
    return listaGanadores

