def interseccion(lista1,lista2):
    lista3 = []
    for i in lista1:
        if(esta(i,lista2)):
            lista3.append(i)
    return(lista3)

def esta(entero,lista):
    for i in lista:
        if(i == entero):
            return(True)
    return(False)

a = [2,4,6,7,3,1,9]
b = [1,2,3,4,5,6,78,8,9,0]
guardoLista = interseccion(a,b)
print(guardoLista)