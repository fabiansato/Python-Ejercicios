#LLamamos a la funcionador calculador que le pasamos el parametro denominador que llamaremos adelante

def calculador(denominador):
    #inicialización de variables
    denominador = denominador
    exponente = 1
    exponenteneg = 0
    numerador = 1
    numfinal = 0.0
    numasumar = {}  # inicializa el array sin valores
    for i in range(0, denominador, 1):
        if (exponenteneg == 0):
            # detecta si estamos en la primer posicion del arrray trata de no elevarlo a 0
            numasumar[i] = (numerador**exponente)/(denominador)

        else:
            # guarda en el array los denominadors a sumar
            numasumar[i] = (numerador**exponente)/(denominador**exponenteneg)

        if (i + 1) % 2 == 0:  # detecta si estamos en primer termino resta en segundo suma
            numfinal = numfinal - numasumar[i]

        else:
            numfinal = numfinal + numasumar[i]


        exponente = exponente + 2
        numerador = numerador + 1
        exponenteneg = exponenteneg - 1
    print("La suma/resta de todos los numeros ingresados es :", numfinal)


denominador = int(input("ingresar un valor")) 
while(denominador < 0): #corrobora con un while que los datos ingresados sean mayor = a 0
    denominador = int(input("El numero ingresado es menor a 0. ingrese nuevamente un valor"))
calculador(denominador)

