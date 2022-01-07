def compruebav(valor): #funcion que comprueba si es un valor numerico
    try: #con un try trata de verificar si es un valor numerico
        valor = float(valor)
        print("Lo que escribiste es un valor numerico")
        
    except ValueError: #si es un valor numerico erroneo saca algo por teclado
        print("Lo que ingresaste NO es un numero")    


valor = input("Ingrese el valor de esta variable: ")
compruebav(valor)

