## Abrimos los archivos para lectura (r) y escritura (w)
entrada = open("3-archivo1.txt","r")
salida = open("3-archivo2.txt","w")

##leemos el archivo y copiamos éste línea a línea en un
##nuevo archivo.Ademas se muestra por pantalla.
lineas=entrada.readlines()

for linea in lineas:
    salida.write(linea)
    print (linea)

salida.write("\nCopiado desde mi PC con Python 3")
# Ahora cerramos los archivos

entrada.close()
salida.close()