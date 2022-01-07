print("Este programa verifica si un anio es bisiesto")

anio = int(input("Ingrese un anio"))

esMultiploDe4 = anio % 4 == 0
esMultiploDe100 = anio % 100 == 0
esMultiploDe400 = anio % 400 == 0

esExcepcion = esMultiploDe100 and (not esMultiploDe400)

if(esMultiploDe4 and (not esExcepcion)):
    print("El anio", anio, "Es bisiesto")
else:
    print("El anio", anio, "NO es bisiesto")
