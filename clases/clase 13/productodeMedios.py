#Producto de medios
def productoDeMedios(n):
    fin=n
    suma=0
    if (n%2==0):
        mitad=n//2
    else:
        mitad=n//2+1
    for i in range(1,mitad+1):
        suma=suma+i*(fin)
        fin=fin-1
    return (suma)

