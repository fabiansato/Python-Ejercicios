

def Operaciones(mes, monto, codigo):
    mes = mes
    if (mes == 1):
        print("Elegiste enero")
        monto = [100, 200, 203, 100, 200, 203, 554, 555, 556, 5557]
        codigo = ['v', 'c', 'c', 'v', 'c', 'c', 'v', 'c', 'c', 'v']
        return(mes, monto, codigo)

    elif(mes == 2):
        print("Elegiste febrero")
        monto = [100, 200, 203, 554, 555, 556, 5557, 554, 555, 556, 5557]
        codigo = ['v', 'c', 'c', 'v', 'c', 'c', 'v', 'v', 'c', 'c', 'v']
        return(monto, codigo)
    elif(mes == 3):
        print("Elegiste marzo")
        monto = [100, 200, 2053, 554, 555, 556, 5557, 556, 5557]
        codigo = ['v', 'c', 'c', 'v', 'c', 'c', 'v', 'c', 'v']
        return monto, codigo
    elif(mes == 4):
        print("Elegiste abril")
        monto = [100, 200, 203, 5544, 555, 556, 5557,
             100, 200, 203, 554, 555, 556, 5557]
        codigo = ['v', 'c', 'c', 'v', 'c', 'c',
              'v', 'v', 'c', 'c', 'v', 'c', 'c', 'v']
        return monto, codigo
    elif(mes == 5):
        mayo()
    elif(mes == 6):
        junio()
    elif(mes == 7):
        julio()
    elif(mes == 8):
        agosto()
    elif(mes== 9):
        septiembre()
    elif(mes == 10):
        octubre()
    elif(mes == 11):
        noviembre()
    elif(mes == 12):
        diciembre()
          

def MontoContrato(operacion):
    mostrarmonto = monto[operacion]
    print(mostrarmonto)

mes = 0
monto = []
codigo = []

mes = int(input("Ingresa un mes elegido: del 1 al 12: \n"))
while ((mes < 0) or (mes > 12)):
    mes = int(
        input("El mes ingresado es invalido. Ingresa un mes elegido: del 1 al 12"))

Operaciones(mess)
print(monto)