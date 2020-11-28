pos=[]

while(True):
    listaAntenas=antenasCercanas()
    if len(listaAntenas)<3:
        suspender()
        desactivarTransmision()
        señalSoS()
    else:
        if (elevacion()<50 or elevacion()>75):
            corrigeElevacion()
        listaDistancias=[]
        for antena in listaAntenas:
            listaDistancias.append(distancia(antena))
        pos=fijarUbicacion(listaAntenas,listaDistancias,elevacion())
        activarTransmision(pos)
