def controlDeUbicación():
    while(True):
        antenasCercanas=dameNrosAntenasCercanas()
        if len(antenasCercanas)>=3:
            if(estoyDormido()):
                despertar()
            for antena in antenasCercanas:
                listaDis.append(distancia(antena))
            determinarUbicacion(antenasCercanas, listaDis)
        else:
            if(not estoyDormido()):
                dormir()