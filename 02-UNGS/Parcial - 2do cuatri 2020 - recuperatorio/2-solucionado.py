'''
Una veterinaria tiene la información de los nombres de animales que atiende  en una lista y desea generar una nueva lista con la información encriptada de la siguiente manera:
Quitando las vocales de cada cliente y añadiendo * en lugar de ellas y además invirtiendo el orden de la lista.
'''

#funcion que toma las listas y traaja con ellas
def EncriptarLista(Listaanimales, Listaencriptada, Listadadavuelta): 
    vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') #guarda en una lista las vocales
    
    #con este for recorre el array y sustituye las vocales con un asterisco
    for i in range(len(Listaanimales)):
        textoactual = Listaanimales[i]
        for letra in vocales:
            textoactual = textoactual.replace(letra, "*")

   
        Listaencriptada.append(textoactual)

    #con este for invierte la lista y va guardando en forma descendiente
    for e in range(len(Listaencriptada)-1, -1, -1):
        textofinal = Listaencriptada[e]

        Listadadavuelta.append(textofinal)
        

    return(Listaencriptada,Listadadavuelta) #devuelve lo guardado en lista encriptada


#lista d eanimales que carga
Listaanimales = ["Gaty", "Sultan", "Paco", "Monito"]

Listaencriptada = []
Listadadavuelta = []


EncriptarLista(Listaanimales, Listaencriptada, Listadadavuelta)


#muestra por pantalla la lista dada vuelta e encriptada
print("La lista encriptada es: ", Listadadavuelta)

