def distribuir():
    listaTareas=misTareas()
    errores=[]
    for tarea in listaTareas:
        tipo=tipoTarea(tarea)
        if tipo==0:
            if (servidorEstandar(tarea)):
                cant=cant+1
            else:
                errores.append(tarea)
        elif(tipo==1):
            if (servidorPrecision(tarea)):
                cant=cant+1
            else:
                errores.append(tarea)
        else:
            if(servidorEspecial(tarea)):
                cant=cant+1
            else:
                errores.append(tarea)

    if len(listaTareas)*.75>cant:
        emitiralerta(100-(100/len(listaTareas)*cant))
    return (errores)














