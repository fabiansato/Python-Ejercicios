#Ejercicio 2 de parcial
#Capicua Circular

def cadenaDesde(cadena,indice):
    cadenaNueva=""
    i=indice
    while i < len(cadena):
        cadenaNueva=cadenaNueva+cadena[i]
        i+=1
    i=0
    while i < indice:
        cadenaNueva=cadenaNueva+cadena[i]
        i+=1
    return(cadenaNueva)

def esCapicuaCircular(cadena):
    esCC=False
    for i in range(len(cadena)):
        if (esCapicua(cadenaDesde(cadena,i))):
            esCC=True
    return (esCC)

