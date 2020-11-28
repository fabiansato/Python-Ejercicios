
texto = input("introduzca el texto")

vocales = ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U')

for letra in vocales:
    texto = texto.replace(letra, "")

#Invierte la cadena
texto = texto[::-1]
print (texto)