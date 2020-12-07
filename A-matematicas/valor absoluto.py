def pasaa_float(valor):
    esstring = isinstance(valor, str)
    while esstring == "true":
        valor = input("Lo que ingresaste no es un número, vuelve a ingresar otra vez:\n")
    
    return float(valor)
  
valor = input("Ingrese un número entero: \n")

pasaa_float(valor)
print(valor)
