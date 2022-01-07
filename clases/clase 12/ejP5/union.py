from interseccion import*
def union(lista1,lista2):
    lis=lista1
    for numero in lista2:
        if not esta(lis,numero):
            lis.append(numero)
    return lis

a=[1,2,3]
b=[1,2,4,8,9]
print (union(a,b))



