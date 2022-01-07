#correlativas(materia): Devuelve una lista de las correlativas a esa materia.
#aprobada(dni, materia): Devuelve verdadero si el estudiante tiene aprobada la materia.
#horario(materia): Devuelve el horario de la materia.
#controlaSuperposicion(dni, horario) Devuelve verdadero si el estudiante tiene libre ese horario.


listaDNI =    [30435473,35552144    ,11421159,28667796  ,26959663  ,30435473    ,29927766]
listaMaterias=[InglesI ,Programacion,InglesI ,Matematica,Matematica,Programacion,InglesI ]
i=0
while i <len(listaDNI):
    baja=False
    materiasCorr= correlativas(listaMateria[i])
    for materia in materiasCorr:
        if not aprobada(listaDNI[i], materia):
            baja= True
    hora=horario(listaMateria[i])
    if not controlaSuperposicion(listaDNI[i], hora):
        baja=True
    if baja:
        listaDni.pop(i)
        listaMateria.pop(i)
    else:
        i=i+1

