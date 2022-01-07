def esta(m,lista):
    for elem in lista:
        if m==elem:
            return True
    return False

def hayInterseccion(lista1,lista2):
    for elem in lista1:
        if esta(elem,lista2):
            return True
    return False

def valida(clave,lisNum,lisLetMin,lisLetMay,lisCaract):
    if len(clave)<8:
        return False
    if not hayInterseccion(clave,lisNum) or not hayInterseccion(clave, lisLetMin) or not hayInterseccion(clave, lisLetMay) or not hayInterseccion(clave, lisCaract):
        return False
    else:
        return True


lisNum=["0","1","2","3","4","5","6","7","8","9"]
lisLetMin=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lisLetMay=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lisCaract=["¡","!","-","_","¿","?"]

clave="¿River-o-Boca?"

print(valida(clave,lisNum,lisLetMin,lisLetMay,lisCaract))
