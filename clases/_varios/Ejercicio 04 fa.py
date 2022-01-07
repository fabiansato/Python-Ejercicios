''' hacer un programa para ingresar el radio de un circulo y se reporte su area y
la longitud de la circunferencia

'''
import math #importamos el modulo math

radio = float(input("radio -> :"))
area = math.pi #modulo math y el valor de pi
longitud = 2 * math.pi * radio

print (f"El area es: {area:.2f}")
print ("La longitud de la circunferencia es : ", longitud)