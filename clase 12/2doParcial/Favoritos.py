def indiceMax(cantLlamados):
    max=cantLlamados[0]
    pos=0
    for i in range(1,len(cantLlamados)):
        if(max<cantLlamados[i]):
            max=cantLlamados[i]
            pos=i
    return(pos)

def favorito(cantLlamados, amigos):
    listaFav=[]
    for i in range(3):
        indice=indiceMax(cantLlamados)
        listaFav.append(amigos[indice])
        cantLlamados.pop(indice)
        amigos.pop(indice)
    return listaFav

amigos=["Ariel","Diana","Santi","Oscar","Lucia","Diego","Pablo"]
cantLlamados=[5,2,0,7,5,1,3]
print(favorito(cantLlamados, amigos))


