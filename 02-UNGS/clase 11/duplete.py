def Duplete(cadena):
    esDuplete=True
    cadenaOriginal=""
    if (len(cadena)%2!=0):
        esDuplete=False
    else:
        for i in range(0,len(cadena),2):
            if (cadena[i]!=cadena[i+1]):
                esDuplete=False
            cadenaOriginal+=cadena[i]
    if(esDuplete):
        print(cadena,"SI es duplete")
        print ("El original era:",cadenaOriginal)
    else:
        print(cadena,"NO es duplete")

Duplete("hhhhoooollllaaaa")


