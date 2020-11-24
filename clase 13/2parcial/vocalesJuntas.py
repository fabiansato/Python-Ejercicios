def esta(letra, cadena):
    for a in cadena:
        if a==letra:
            return True
    return False

def vocalesJuntas(cadena):
    vocales=["a","e","i","o","u"]
    for i in range(len(cadena)-1):
        if esta(cadena[i],vocales) and esta(cadena[i+1],vocales):
            return True
    return False

print (vocalesJuntas("aire"))