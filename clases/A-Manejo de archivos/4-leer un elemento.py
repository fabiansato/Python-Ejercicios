# Leer un archivo en el cual el primer elemento indica la cantidad de líneas y lo guarda en una lista

f = open("4-archivo.txt", "w")
numeros=[1,2,3,4,5]
for i in range(len(numeros)):
    a=f.write(str(numeros[i]))
f.close()
