
# Abrimos un archivos para lectura (r) 
archivo = open("1-archivo.txt","r")
lista=[]

# leemos 10 líneas del archivo y guardamos los elementos en una lista

for i in range(10):
	  lista.append(archivo.readline())
print (lista)

# Ahora cerramos el archivos
archivo.close()
