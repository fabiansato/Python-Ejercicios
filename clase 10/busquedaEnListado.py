#1- Hacer una función que recibe una lista y un entero e indique si el entero está en la #lista.

def busquedaSinIndices(listadoNumeros, entero):
    for i in listadoNumeros:
        if(i==entero):
            return True
    return False

def busquedaSinIndicesFlag(listadoNumeros, entero):
    flag=False
    for i in listadoNumeros:
        if(i==entero):
            flag=True
    return flag

def busquedaConIndices(listadoNumeros, entero):
    for i in range(len(listadoNumeros)):
        if(listadoNumeros[i]==entero):
            return True
    return False

def main():
    entero=int(input("ingresar un numero"))
    lista=[2,3,4,0,10,20,2]
    #llamados
    print(busquedaSinIndices(lista,entero))
    print(busquedaSinIndicesFlag(lista,entero))
    print(busquedaConIndices(lista,entero))

    if(busquedaSinIndices(lista,entero)):
        print("El numero esta en el listado")
    else:
        print("El numero NO esta en el listado")



if __name__ == '__main__':
    main()
