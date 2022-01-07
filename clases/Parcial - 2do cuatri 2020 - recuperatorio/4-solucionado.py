def Operaciones(mes,idoperacion):

#genero una lista con los codigos de operación creados en cada mes, lo guardo en una 
    # matriz para tener mejor orden de las mismas
    mes = mes - 1 #pone menos uno para mostar el indice
    print(idoperacion[mes])


def MontoContrato(posicion, montooperacion):
     print(montooperacion[posicion])


def PorcenComisionComodato():
     comodato = 0.1
     return comodato


def PorcenComisionVenta():
    comisionventa = 0.2
    return comisionventa 

#guarda el id de la operacion realizada por mes en matrices
idoperacion = [ 
    [1, 2, 3, 4, 5, 6, 7],  # enero
    [8, 9, 10, 11],  # febrero
    [12, 13, 14, 15, 16, 17, 18, 19],  # marzo
    [20, 21, 22, 23, 24, 25],  # abril
    [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],  # mayo
    [39, 40, 41, 42, 43],  # junio
    [44, 45, 46, 47, 48, 49, 50],  # julio
    [51, 52, 53, 54, 55],  # agosto
    [56, 57, 58, 59],  # septiembre
    [60, 61, 62, 63, 64],  # ocrubre
    [65, 66, 67, 68, 69, 70],  # noviembre
    [71, 72, 73, 74]  # diciembre
]

#es una matriz con el monto de la operacion realizada en el mes ligada al monto de operacion
montooperacion = [
    [100, 200, 203, 554, 555, 556, 5557],  # enero
    [8333, 393, 1033, 11333],  # febrero
    [1233, 3313, 3314, 3315, 316, 3317, 3318, 1339],  # marzo
    [203, 213, 223, 233, 243, 2533],  # abril
    [326, 327, 328, 329, 330, 331, 332, 3333, 334, 435, 3236, 337, 338],  # mayo
    [339, 430, 431, 432, 433],  # junio
    [434, 435, 436, 437, 4448, 4449, 540],  # julio
    [541, 5442, 543, 544, 545],  # agosto
    [5446, 547, 548, 549],  # septiembre
    [640, 641, 642, 643, 644],  # ocrubre
    [64445, 64446, 6447, 6448, 6559, 7044],  # noviembre
    [7551, 752, 753, 745]  # diciembre
]

codigooperacion = [
    ['v', 'c', 'c', 'v', 'c', 'c','v'],  # enero
    ['v', 'c', 'c', 'v'],  # febrero
    ['v', 'c', 'c', 'v', 'v', 'c', 'c', 'v'],  # marzo
    ['v', 'c', 'c', 'v', 'v', 'c'],  # abril
    ['v', 'c', 'c', 'v', 'v', 'c', 'c', 'v', 'v',
        'c', 'c', 'v', 'v'],  # mayo
    ['v', 'c', 'c', 'v', 'v'],  # junio
    ['v', 'c', 'c', 'v', 'v', 'v', 'c'],  # julio
    ['v', 'c','v', 'c','v'],  # agosto
    ['v', 'c', 'v', 'c', 'v'],  # septiembre
    ['v', 'c', 'v', 'c', 'v'],  # ocrubre
    ['v', 'c', 'v', 'c', 'v'],  # noviembre
    ['v', 'c', 'v', 'c']  # diciembre
]
print(PorcenComisionComodato())
print(PorcenComisionVenta())
mes = int(input("Ingresa un mes elegido: del 1 al 12: \n"))
while ((mes < 0) or (mes > 12)):
    mes = int(input("El mes ingresado es invalido. Ingresa un mes elegido: del 1 al 12"))
Operaciones(mes, idoperacion) 

operacion = int(input("Ingrese un numero de operacion: \n"))


busqueda = ((x,  y) for x,  row in enumerate(idoperacion)
            for y,  elemento in enumerate(row) if elemento == operacion)

for e in busqueda:
    print(e)
    posicion = e

print(posicion)
#MontoContrato(, montooperacion)


