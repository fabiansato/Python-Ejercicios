
cadena=input("Ingrese una palabra")

cont=0
for letra in cadena:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        cont=cont+1
print("la palabra",cadena,"tiene", cont,"vocales")

