'''
Ejercicio 5:
Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuanto debera pagar finalmente por su compra 
'''
precio = float(input("Digite el precio:"))

descuento = precio * 0.15
precio_final = precio - descuento

print("El precio final es : ",precio_final)