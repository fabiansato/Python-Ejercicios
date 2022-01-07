##edad=int(input("Ingrese su edad",))
##distancia=float(input("indique la distancia a la que se encuentra en Km de su centro de votacion"))
##noVota=edad<18 or edad>70 or ((edad>=18 and edad<=70) and distancia>500)
##if noVota:
##    print("Ud esta excento de votar")
##else:
##    print("Ud debe ir votar")


edad=int(input("Ingrese su edad",))
distancia=float(input("indique la distancia a la que se encuentra en Km de su centro de votacion"))
vota=edad>=18 and edad<=70 and distancia<=500
if vota:
    print("Ud debe ir votar")
else:
    print("Ud esta excento de votar")
