def posicion(elemento,lista):
    for i in range(len(lista)):
        if elemento==lista[i]:
            return i

listaMonedas=["euro","dolar","peso chileno","peso uruguayo","real"]
cotizacionVenta=[11.26,9.57,0.018,0.43,3.02]
cantidad=int(input("Ingrese cantidad de monedas a cotizar"))
listaFinal=[]
for i in range(cantidad):
    moneda=input("Ingrese tipo de moneda")
    listaFinal.append(moneda)
    pos=posicion(moneda,listaMonedas)
    listaFinal.append(cotizacionVenta[pos]*100*1.35)
print(listaFinal)
print(len(listaFinal)//2)





