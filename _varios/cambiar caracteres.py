# cadena o string
# dada una cadena contar la cantidad de
# vocales a que tiene
# area ==> 2 vocales area
# solo ==> 0 vocales area
cadena=input("cadena")
cadena_final = " "


for char in cadena:
	if char == 'a':
        cadena_final = cadena_final + '*'
    else:
        cadena_final = cadena_final + char

 print(cadena_final)

