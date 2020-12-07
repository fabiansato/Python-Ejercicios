'''Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
pantalla el resultado de evaluar las siguientes fórmulas:
a) raiz cuadrada de x
b) valor absoluto de x
C) valor absoluto de un numero - 3
d) raiz cuadrada de un valor absoluto de un numero - 5
'''
import math

def funcionA(valor):
    valor = math.sqrt(valor)
    return valor

def funcionB(valor):
    return valor
def funcionC(valor):
    return valor
def funcionD(valor):
    return valor

elige = 1
valor = float(input("ingrese un numero decimal\n"))
while elige != '5':
    elige = input("Elige que quieres hacer con el numero: \n1) raiz cuadrada de x \n2) valor absoluto de x \n3) El valor absoluto de un numero - 3 \n4) raiz cuadrada de un valor absoluto de un numero - 5\n5) salir\n")
    print ("elegiste el", elige)
    
    if elige == 1:
        print(funcionA(valor))
        
    elif elige == 2:
        funcionB(valor)
    elif elige == 3:
        funcionB(valor)
    elif elige == 3:
        funcionC(valor)
    elif elige == 4:
        funcionD(valor)


