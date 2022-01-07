def resta(a=3, b=2): #argumentos que son tomados y su valor inicials
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return   # indicamos el final de la función aunque no devuelva nada
    return a-b


print(resta(1, 5)) #argumentos que son enviados dentro de la funcion
