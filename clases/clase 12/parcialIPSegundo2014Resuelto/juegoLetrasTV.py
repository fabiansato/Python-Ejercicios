def cantidad(cadena,letra):
    cant=0
    for elemento in cadena:
        if elemento== letra:
            cant+=1
    return cant

def esCorrecta(pantalla,cadena):
    if len(pantalla)==len(cadena):
        for elemento in cadena:
            if cantidad(cadena,elemento)!=cantidad(pantalla,elemento):
                return False
        return True
    else:
        return False

letrasPantalla="ieahlerda"
cadena="heladeria"
print(esCorrecta(letrasPantalla,cadena))

