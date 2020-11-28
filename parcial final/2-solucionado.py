totalcontra=1
vocales = ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U')
letraA = ('a', 'A',)
salir=1
ListaContrasenias = [ ] #inicializa el array sin valores
ListaContraSinVocal = [  ] #inicializa el array sin valores
ListaContraSinA = [  ] #inicializa el array sin valores
Listacontrainvertidas = []
Listacontrainvertidasmas = []

while salir == 1:  
    contraseniaactual=input("Ingrese contraseña: \n")



    for i in range(len(ListaContrasenias)):
        if contraseniaactual == ListaContrasenias[i]:
            contraseniaactual=input("La contraseña actual esta registrada: \n Ingrese nuevamente una contraseña:\n")


    ListaContrasenias.append(contraseniaactual)
    contraseniaactualinvertida = contraseniaactual[::-1]
    contraseniaactualinvertidamas = contraseniaactualinvertida + "*"

    Listacontrainvertidas.append(contraseniaactualinvertida)
    Listacontrainvertidasmas.append(contraseniaactualinvertidamas)

    for letra in letraA:
        contraseniaactual = contraseniaactual.replace(letra, "")
    ListaContraSinA.append(contraseniaactual)


    for letra in vocales:
        contraseniaactual = contraseniaactual.replace(letra, "")
    ListaContraSinVocal.append(contraseniaactual)



    salir=int(input("ingresa cualquier NUMERO para SALIR...: \n ingresa 1 para ingresar otra contraseña:\n"))

print("\nLista de contraseñas:\n",ListaContrasenias)
print("\nLista de contraseñas sin letra A:\n",ListaContraSinA)
print("\nLista de contraseñas sin vocales:\n",ListaContraSinVocal)
print("\nLista de contraseñas invertidas:\n",Listacontrainvertidas)
print("\nLista de contraseñas con asterisco:\n",Listacontrainvertidasmas)


