def cantApariciones(numero, lista):
    cant=0
    for i in range(len(lista)):
        if (numero==lista[i]):
            cant+=1
    return (cant)

def Moda(A):
    cantMaxApar=0
    elValorModa=A[0]
    for i in range(len(A)):
        if(cantApariciones(A[i],A)>cantMaxApar):
            cantMaxApar=cantApariciones(A[i],A)
            elValorModa=A[i]
    return(elValorModa)

def indices(numero, lista):
    listaIndices=[]
    for i in range(len(lista)):
        if (lista[i]==numero):
            listaIndices.append(i)
    return(listaIndices)


lista=[4,2,1,8,1,9,2,2,4,2]
laModa=Moda(lista)

print (laModa)

print(indices(laModa,lista))
