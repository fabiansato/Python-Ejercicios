precio=[15,9.2,3,3,1.2,1,4.5,5.1,5.2,5,6.5,7.4,7.2,8,11,10,18,20,23,25,28.1,28,25,23]
precioC=[10,8.5,1,2,1.2,1,1.5,4.5,1.2,4,5.5,7.4,7.1,4,10,10,11,20,23,25,25.1,27,21,21]
compra=[10,10,1,2,5,19,15,18,4,0,21,4,9]
cant=len(precio)
totalPrecio=0
totalCuid=0

for elemento in compra:
        totalPrecio+=precio[elemento]
        totalCuid+=precioC[elemento]

print('Total con precios libres con bonificacion del 20%:',totalPrecio-totalPrecio*0.2)
print('Total con precios cuidados:',totalCuid)

if (totalPrecio-totalPrecio*0.2)<=totalCuid:
    print('te conviene compar con precios libres y aprovechar el 20% de descuento')
else:
    print('te conviene aprovechar los precios cuidados')
