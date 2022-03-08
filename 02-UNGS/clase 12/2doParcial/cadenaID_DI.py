def revisaDerIzq(cadena, lista):
    i=0
    for letra in cadena:
        if letra !=lista[i]:
            return False
        i=i+1
    return True

def revisaIzqDer(cadena, lista):
    i=len(lista)-1
    for letra in cadena:
        if letra !=lista[i]:
            return False
        i=i-1
    return True

def control(cadena,lista):
    if(len(cadena)!=len(lista)):
        return (False)
    else:
        return (revisaIzqDer(cadena,lista) or revisaDerIzq(cadena, lista))


cadena="palomar"
lista1=["p","a","l","o","m","a","r"]
lista2=["r","a","m","o","l","a","p"]
print(control(cadena,lista1))

