def esta(a, lista):
    for elem in lista:
        if a==elem:
            return True
    return False

lista1=[5,10,8,9,6,7,5,3,10]
lista2=[6,9,1,6,9,2,7,7,8,15,22]
salida=[]

n=int(input("ingrese uin entero"))
if len(lista1)<len(lista2):
    corto=lista1
    largo=lista2
else:
    corto=lista2
    largo=lista1

for i in range(len(corto)):
    numero=corto[i]+largo[i]
    if numero>n and not esta(numero, salida):
        salida.append(numero)
print(salida)





