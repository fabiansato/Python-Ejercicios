def intercambiar(lista, a,b):
    aux=lista[a]
    lista[a]=lista[b]
    lista[b]=aux

a=[3,5,7,9,11]
print (a)
x=1
y=3
intercambiar(a,x,y)
print(a)
