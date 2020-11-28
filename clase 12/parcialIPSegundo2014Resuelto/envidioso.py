def perfecto(num):
    suma=0
    for i in range(1,num):
        if(num%i==0):
            suma+=i
    if suma==num:
        return True
    else:
        return False

def envidioso(num):
    if (not perfecto(num)):
        for i in range(1,num):
            if(num%i==0 and perfecto(i)):
                return True
    return False

numero=int(input('Ingrese un numero entero para comprobar si es Envidioso'))

if (envidioso(numero)):
    print(numero, "es un numero envidioso")
else:
    print(numero, "NO es numero envidioso")
