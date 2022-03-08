
a=input("Ingrese una palabra")
palabra=list(a)

print (palabra)

for i in range(0,len(palabra)):
    for j in range(i+1,len(palabra)):
        if (palabra[i]==palabra[j]):
            print ("la letra", palabra[i],"esta repetida", "en las posiciones", i+1, " y ",j+1)
