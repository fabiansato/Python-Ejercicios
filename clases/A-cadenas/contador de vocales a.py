# cadena o string
# dada una cadena contar la cantidad de
# vocales a que tiene
# area ==> 2 vocales area
# solo ==> 0 vocales area
cadena=input("ingresar cadena")
alreves = ""

for char in cadena:
    if char != "":
       alreves = char + alreves


print(alreves)