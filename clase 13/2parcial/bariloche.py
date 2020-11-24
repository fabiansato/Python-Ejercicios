def bariloche(listaTuristas, listaEstadia):
    listaContadora=[0,0,0,0]
    for elemento in listaEstadia:
        if elemento<7:
            listaContadora[0]+=1
        elif elemento >=7 and elemento <=15:
            listaContadora[1]+=1
        elif elemento >15 and elemento <=30:
            listaContadora[2]+=1
        else:
            listaContadora[3]+=1
    return listaContadora

listaTurista=["santiago", "marcelo","daniel", "javier", "esteban"
             ,"juan", "jose", "juan", "jorge"]
listaEstadia=[4,8,9,16,31,25,8,15,14]
print(bariloche(listaTurista,listaEstadia))