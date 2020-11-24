from funcionesLista import*

def diferencia(l1,l2):
    l3=[]
    for elem in l1:
        if not Esta(l2,elem):
            l3.append(elem)
    return(l3)

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [1,3,12,13,15,6,18]
print(diferencia(lista1,lista2))

