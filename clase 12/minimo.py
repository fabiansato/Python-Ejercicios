def minimo(palabra):
    posmin = 0
    for i in range(1, len(palabra)):
        if(palabra[posmin] > palabra[i]):
            posmin = i

    return posmin

pal = input("Ingrese una palabra")
print(pal)
pala2 = list(pal)
lista = []

cant = 0
while(cant < len(pal)):
    pos = minimo(pala2)
    lista.append(pala2[pos])
    pala2.pop(pos)
    cant = cant + 1

print(lista)