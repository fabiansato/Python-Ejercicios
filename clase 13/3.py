##Ejercicio 3 del 2do Parcial...antes de p y b m pondre

def corrector (palabra):
    for i in range (1,len(palabra)):
        if (palabra[i]=='p' or palabra[i]=='b' and palabra[i-1]=='n'):
            palabra[i-1]='m'



cadena=input("Ingrese una palabra")
palabra=list(cadena)
corrector (palabra)
print ("palabra inicial: ",cadena,"palabra final:",palabra)



##hicieron mucho lio para  palabra[i-1]='m'