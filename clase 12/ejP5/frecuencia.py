def frecuencia(lista,n):
    cont=0
    for numero in lista:
        if numero==n:
            cont+=1
    return cont
a=[2, 6,2,8,4,2]
x= 2
print(x,"aparece en:",a, frecuencia(a,2),"veces")
