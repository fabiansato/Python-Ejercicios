#Punto B
Aero=input("Ingresa el nombre\n")
minusculas=Aero.lower() #pone todo en minusculas
Espacio=" " #guarda el espacio
Final=""
cont=1 #inicializa en 1

Final=Final+minusculas[0]

noHayEspacio = True #flag en espacio

for m in range(len(minusculas)): #range del primer hasta el ultim numero #m es la variable del ciclo
    if minusculas[m] == Espacio: #si existe un espacio en una vuelta del array del m
        Final=Final+minusculas[m+1] 
        noHayEspacio = False

if noHayEspacio:
  for m in range(1, len(minusculas)):
    k = minusculas[m]
    if (k!="a")and(k!="e")and(k!="i")and(k!="o")and(k!="u")and cont<=1:
      Final=Final+k
      cont=cont+1

print(Final.upper())