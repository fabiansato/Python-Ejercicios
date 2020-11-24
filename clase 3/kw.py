print ("Este programa calcula el precio a pagar en la factura de LUZ")
kwinicial=float(input("Ingrese KW iniciales"))
kwfinal=float(input("Ingrese KW final"))
kw=kwfinal-kwinicial
tarifafija=20
impuestos=7.8

if(kw<200):
    monto=tarifafija+impuestos
else:
    monto=tarifafija+impuestos+0.5*(kw-200)

print("El precio a pagar es:",monto)