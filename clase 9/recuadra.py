
def recuadra(cadena):
    n=len(cadena)
    for i in range(n+4):
        print ("*",end="")

    print ("\n*",cadena,"*")

    for i in range(n+4):
        print ("*",end="")


a=input("Ingrese una palabra")

recuadra(a)