print("Cantidad de palabras")
frase=input("Ingrese una frase")
cont=1
for letra in frase:
    if letra==" ":
        cont=cont+1

print(frase,"tiene",cont,"palabras")