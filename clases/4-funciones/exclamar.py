
def exclamar(cadena):
    return("¡" + cadena + "!")


def gritar(cadena):
    return(exclamar(exclamar(exclamar(cadena))))

print(gritar("hola"))
