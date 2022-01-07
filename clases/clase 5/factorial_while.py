#Version de Calculo Factorial iterando, unicamente con while.
#Un while dentro de otro (anidados ejer 18 Practica3).

respuesta=input("Ingrese un numero o cuaquier letra para salir") #cargo respuesta
while(respuesta!="n" and respuesta.isdigit()):                   #diferente a n entro en el while -- Primer while externo. (isdigit() opcional)
    cont=1                                                       #cargo y/o reseteo posteriormente count y acum
    acum=1
    if(respuesta!="n"):                                          #si respuesta es un numero, busco el factorial
        respuesta=int(respuesta)                                 #transformo la cadena en numero
        while(cont<=respuesta):                                  #algoritmo de factorial -- Segundo while interno
            acum=acum*cont
            cont=cont+1
        print("factorial de", respuesta,":", acum)
    respuesta=input(
    "Ingrese un numero o cuaquier letra para salir")            #pregunto para volver a iterar
print("\nTerminado")
