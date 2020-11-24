def aparece(laLetra,enLaCadena):
    for caracter in enLaCadena:
        if(caracter == laLetra):
            return(True)
    return(False)

def vecesQueAparece(letra,cadena):
    contador = 0
    for caracter in cadena:
        if(caracter == letra):
            contador += 1
    return(contador)

def tieneRepetidas(cadena):
    for caracter in cadena:
        if(vecesQueAparece(caracter,cadena)>1):
            return(True)
    return(False)