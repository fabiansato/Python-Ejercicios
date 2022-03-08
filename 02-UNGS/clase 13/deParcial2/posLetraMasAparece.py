def cantApariciones(letra, cadena):
    cant=0
    for a in cadena:
        if a == letra:
            cant+=1
    return cant

def letraMasAparece(cadena):
    max=0
    letraMasAparecida=cadena[0]
    for letra in cadena:
        if cantApariciones(letra, cadena)>max:
            max=cantApariciones(letra, cadena)
            letraMasAparecida=letra
    return letraMasAparecida

def buscaPosiciones(letra, candea):
    listaPos=[]
    for i in range(len(cadena)):
        if cadena[i] == letra:
            listaPos.append(i)
    return listaPos


cadena="cerealera"
a=letraMasAparece(cadena)
lista=buscaPosiciones(a, cadena)
print (lista)
