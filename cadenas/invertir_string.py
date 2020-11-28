#con esta funcion podremos invertir cualquier string
def inviertecadena(sg,n): #toma los argumentos sg (el string ingresado) y el numero el tamaño del texto
    if n>0: #valida si el tamaño de n es mayor a 0
        k=len(sg)-n #guarda el tamaño del string segun el tamaño 
        inviertecadena(sg,n-1) 
        print(sg[k],end='')
    elif n==0: # si el estring no tiene nada manda cierra la función
        return
s=input() #toma por teclado el envio del texto
inviertecadena(s,len(s)) #llama la funcion y manda como argumentos el contenido de s y el tamaño de s