#autos(): devuelve una lista de autos recientemente fabricados o reparados.
#verificador(auto): recibe un auto y retorna True si el auto funciona correctamente y False si se detecta alguna falla.
#pedido(): indica cuantos autos solicitan las concesionarias.
#enviarTaller(listaAutosRotos): recibe una lista de autos y los envía al taller para su reparación.
#enviarVenta(listaAutosOK): recibe una lista de autos y los envía a las concesionarias.
#enviarDeposito(listaAutosSobran): recibe una lista de autos y los envía al playón.


listaAutosRotos=[]
listaAutosOK=[]
listaAutosSobran=[]

listaAutos=autos()
cantPedidos=pedidos()

for auto in listaAutos:
    if verificador(auto):
        if len(listaAutosOK)<cantPedidos:
            listaAutosOK.append(auto)
        else:
            listaAutosSobran.append(auto)
    else:
        listaAutosRotos.append(auto)

enviarTaller(listaAutosRotos)
enviarVenta(listaAutosOK)
enviarDeposito(listaAutosSobran)

#suppongo que si me piden mas de lo que tengo mando lo que tengo
#supongo que las funciones no hacen nada si reciben listas vacias