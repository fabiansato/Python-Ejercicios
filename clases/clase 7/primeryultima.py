print("Primer y ultima letra")
palabra=input("Ingrese una palabra")
cont=1
abreviatura=""
for letra in palabra:
    if cont==1 or cont==len(palabra):
        abreviatura=abreviatura+letra.upper()
    cont=cont+1

print(abreviatura)