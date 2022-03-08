def esta(n,lista):
    for elem in lista:
        if elem==n:
            return True
    return False

def casiAmigos(lista1,lista2):
    lista3=[]
    for amigo in lista1:
        if not esta (amigo, lista2):
            lista3.append(amigo)
    return lista3


AmigosDe1=["Ariel","Diana","Santi","Oscar","Lucia"]
AmigosDe2=["Fabiana","Santi","Pablo","Daniel","Ariel","Susana","Diana"]

if len (AmigosDe1)>len(AmigosDe2):
    print(casiAmigos(AmigosDe1,AmigosDe2))
else:
    print(casiAmigos(AmigosDe2,AmigosDe1))

