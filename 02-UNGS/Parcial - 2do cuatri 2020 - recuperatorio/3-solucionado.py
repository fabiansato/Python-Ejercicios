'''
Se tienen tres cotizacioness, una de jugadores, otra de sus equipos y otra de sus cotizaciones en el mercado de pases.

Se debe hacer una función que reciba como parámetros estas tres cotizacioness, devuelva quién es el jugador más cotizado y cuál es su equipo. Posteriormente hacer el programa principal que invoca a dicha función.
'''


#Esta funcion determina el maximo ganado y lo muestra por pantalla
def Max(cotizaciones):
    max = cotizaciones[0]
    for i in range(1, len(cotizaciones)):
        if max < cotizaciones[i]:
            max = cotizaciones[i]

    return max

#Esta función guarda el indice del maximo ganado
def IndiceDelMax(cotizaciones):
    IndMax = 0
    for i in range(1, len(cotizaciones)):
        if cotizaciones[IndMax] < cotizaciones[i]:
            IndMax = i

    return IndMax

#esta funcion saca si hay mas uno que gane igual y es el mayor, y guarda sus indices
def IndicesDelMax(cotizaciones):
    indMax = IndiceDelMax(cotizaciones)
    indices = []
    for i in range(0, len(cotizaciones)):
        if cotizaciones[indMax] == cotizaciones[i]:
            indices.append(i)

    return indices

#Requiere cotizaciones no vacia


jugadores = ['Frodo', 'Gollum', 'Arwen', 'Sauron', 'Gimli', 'Frodo', 'Elrod', 'Saruman', 'Tom', 'Faramir']
equipos = ['Boca', 'River', 'Racing', 'Independiente', 'Talleres', 'Newells old boys', 'Racing', 'Velez', 'River', 'Boca']
cotizaciones = [3588500, 85000000, 6, 85000000, 2, 85000000, 2, 4, 85000000, 3]


print("Lo maximo ganado es: $", Max(cotizaciones))



sihaymas = list(IndicesDelMax(cotizaciones)) #llama la funcion indices del max para guardar si hay mas de 1 jugador que gane mas
sihaymas2 = sihaymas.copy() #guarda la lista para trabajar con int

#con este if sabemos si existen 2 o mas jugadores que ganen el maximo e igual
if (len(sihaymas2)>1): 
    print("En total hay ",len(sihaymas2)," que cotizan lo mismo y son los siguientes:")
    for e in range(len(sihaymas)):
        print("",jugadores[e],"del equipo",equipos[e])
# si solo encuentra uno muestra quien es
else: 
    print("Solamente hay ",len(sihaymas2)," que cotiza ese total y es el siguiente:")
    for y in range(len(sihaymas)):
        print("",jugadores[y],"del equipo",equipos[y])

