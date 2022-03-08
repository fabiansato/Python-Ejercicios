#obtenerCantidadLlamados(nroCliente): devuelve cuantos llamados hizo
#obtenerTiempoPorLlamada(nroCliente, nroLlamada): devuelve cuanto hablo
#                                               en la llamada nroLlamada
#obtenerCostoPorLlamada(): devuelve el costo fijo de cada llamada
#obtenerCostoPorTiempo(cantSegundos): devuelve el costo de una llamada de
#                                       cantSgundos


# cuento con una lista de clientes

def calcularCostos(lista):
    for nroCliente in lista:
        cantLlamadas = obtenerCantidadLlamados(nroCliente)
        costo = cantLlamadas * obtenerCostoPorLlamada()
        for nroLlamada in range(cantLlamadas):
            costo = costo + obtenerCostoPorTiempo(obtenerTiempoPorLlamada(nroCliente, nroLlamada))
        print(nroCliente,": $", costo)

# ---  Programa Principal  ---#
listaClientes = [1,2,4,5,6,7,8,12]
calcularCostos(listaClientes)
