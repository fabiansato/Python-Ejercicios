from interseccion import*
def max(lista):
    max=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>max:
             max=lista[i]
    return max
def listadiv(num):
    liz=[]
    for i in range(1,num+1):
        if num%i==0:
            liz.append(i)
    return liz
def mcd(a,b):
    lista1=listadiv(a)
    lista2=listadiv(b)
    lista3=interseccion(lista1, lista2)
    return max(lista3)
print (mcd(60,15))