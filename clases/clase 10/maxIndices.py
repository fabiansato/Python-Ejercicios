#Requiere lista no vacia
def Max(lista):
    max = lista[0]
    for i in range(1,len(lista)):
        if max < lista[i]:
            max = lista[i]

    return max

#Requiere lista no vacia
def IndiceDelMax(lista):
    IndMax = 0
    for i in range(1,len(lista)):
        if lista[IndMax] < lista[i]:
            IndMax = i

    return IndMax

#Requiere lista no vacia
def IndicesDelMax(lista):
    indMax = IndiceDelMax(lista)
    indices = []
    for i in range(0,len(lista)):
        if lista[indMax] == lista[i]:
            indices.append(i)

    return indices

#Requiere lista no vacia
def Max2(lista):
    i = IndiceDelMax(lista)
    return lista[i]

##cantNotas=int(input("Cuantas notas por alumno?"))
##cantAlumnos=int(input("Cuantos alumnos?"))
##promedios = []
##for i in range(cantAlumnos):
##    suma=0
##    for j in range(cantNotas):
##        cartel="Nota"+str(j+1)+"del alumno"+str(i+1)+":"
##        nota=float(input(cartel))
##        suma += nota
##    promedios.append(suma/cantNotas)
##
##print("Promedios:", promedios)
##
##print(Max(promedios))
##print(Max2(promedios))

lista = [3,4,6,8,2,8,2,4,8,3]
print(Max(lista))
print(Max2(lista))
print(IndiceDelMax(lista))
print(IndicesDelMax(lista))
