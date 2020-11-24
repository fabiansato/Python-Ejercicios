#Implementar las siguientes funciones:
#ObtenerCostoPorTiempo(seg)
#ObtenerCantidadLlamados(nroCliente)
#ObtenerCostoPorLlamada()
#ObtenerTiempoPorLlamada(nroCliente, nroLlamada)
#Alta(nroCliente)
#Baja(nroCliente)
#Esta(nroCliente)

def tarifaTelefonica(nroCliente):
    cantLlamados=ObtenerCantidadLlamados(nroCliente)
    costo=ObtenerCostoPorLlamada() * cantLlamados

    for nroLlamada in range(1,cantLlamados+1) :
        seg=ObtenerTiempoPorLlamada(nroCliente, nroLlamada)
        costo=costo+ObtenerCostoPorTiempo(seg)
        segundos=segundos+seg

    if(Esta(nroCliente)):
        Baja(nroCliente)
    else:
        if(segundos>7200):
            Alta(nroCliente)

    return costo

