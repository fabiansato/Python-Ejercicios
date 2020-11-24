print("Este programa verifica si un anio es bisiesto")

anio = int(input("Ingrese un anio"))

if(anio % 4 != 0):
    print("el anio", anio, "No es bisiesto")
else:
    if(anio % 100 != 0):
        print("el anio", anio, "Si es bisiesto")
    else:
        if(anio % 400 !=0):
            print("el anio", anio, "NO Es bisiesto")
        else:
            print("el anio", anio, "Si es bisiesto")