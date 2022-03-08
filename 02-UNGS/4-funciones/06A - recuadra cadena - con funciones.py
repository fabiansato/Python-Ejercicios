'''

1 - Hacer una función(no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
Por ejemplo si la cadena fuera Sobrevivir, la función debería imprimir

***********
* sobrevivir *
***********

Luego hacer un programa que use la función.
¿Cómo haría para que la función sea pura?

'''

def recuadra(cadena):
    n=len(cadena)
    for i in range(n+4):
        print ("*",end="")

    print ("\n*",cadena,"*")

    for i in range(n+4):
        print ("*",end="")


a=input("Ingrese una palabra")

recuadra(a)
