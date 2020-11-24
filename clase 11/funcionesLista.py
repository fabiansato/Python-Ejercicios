def Esta(lista, a):
    for elem in lista:
        if elem == a:
            return True
    return False

def Cuantos(lista, a):
    cont = 0
    for elem in lista:
        if elem == a:
            cont += 1

    return cont

def Esta2(lista, a):
    return( Cuantos(lista, a) > 0 )



def TieneRepetidos(lista):
    for elem in lista:
        if Cuantos(lista, elem) >= 2:
            return True
    return False

def TieneRepetidos2(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def Eliminar(lista, elem):
    i = 0
    while i < len(lista):
        if elem == lista[i]:
            lista.pop(i)
        else:
            i += 1
    return lista


def EliminarRepetidos(lista):
    i = 0
    while i < len(lista):
        if Cuantos(lista,lista[i]) > 1:
            Eliminar(lista,lista[i])
        else:
            i += 1
    return lista


# Deja uno de cada elemento
def EliminarRepe(lista):
    i = 0
    while i < len(lista):
        j = i+1
        while j < len(lista):
            if lista[i] == lista[j]:
                lista.pop(j)
            else:
                j += 1
        i += 1

    return lista

def EliminarDesde(num, lista, pos):
    i = pos
    while i < len(lista):
        if num == lista[i]:
            lista.pop(i)
        else:
            i += 1
    return lista

def EliminarRepeti2(lista):
    i = 0
    while i < len(lista):
        lista = EliminarDesde(lista[i], lista, i+1)
        i += 1
    return lista

print(EliminarRepetidos([1,3,8,1,-2,8,1]))











