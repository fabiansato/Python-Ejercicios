# Abrimos un archivos para lectura (r)
archivo = open("2-archivo.txt","r")
lista=archivo.readlines()
print (lista)
# Ahora cerramos el archivos
archivo.close()
