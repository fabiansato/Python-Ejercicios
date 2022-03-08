#inicializa las variables con el valor correspondiente
potencia=1
divisor=1
dividendo=2
numerofinal=0.0
numerosasumar = { } #inicializa el array sin valores
numero=int(input("Ingrese un numero entero: \n"))


for i in range (0,numero,1):
    numerosasumar[i] =  (divisor**potencia)/dividendo  #guarda en el array los numeros a sumar
   
    if (i + 1) % 2 == 0: #detecta si estamos en primer termino resta en segundo suma 
        numerofinal = numerofinal - numerosasumar[i] 
        print("resta")
    else:
        numerofinal = numerofinal + numerosasumar[i]
        print("suma")
 
    potencia = potencia + 2
    divisor = divisor + 1
    dividendo = dividendo + 2

print ("La suma de todos los numeros es :",numerofinal)
