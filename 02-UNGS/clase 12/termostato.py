##●	obtenerGradosF(n) que retorna la temperatura del ambiente n en grados Farenheit.
##●	transformar(gradosF) que recibe la temperatura en grados Farenheit y devuelve su correspondiente en grados Celsius.
##●	encenderCalefon(n), apagarCalefon(n), encenderAire(n), apagarAire(n) que controlan el calefon (o aire) en el ambiente n
##●	estaPrendidoCalefon(n), estaPrendidoAire(n) que indica si esta prendido o apagado el calefon (o aire) en el ambiente n.
##●	esperarSegundos(n), que pausa el programa por n segundos
n=10
for i in range(n):
    gradosF=obtenerGradosF(i)
    gradosC=transformar(gradosF)
    if(gradosC>26 and not estaPrendidoAire(i)):
        encenderAire(i)
    elif(gradosC <17 and not estaPrendidoCalefon(i)):
        encenderCalefon(i)
    else:
        if (estaPrendidoAire(i)):
            apagarAire(i)
        if(estaPrendidoCalefon(i)):
            apagarCalefon(i)



