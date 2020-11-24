a=input("Ingrese una palabra")
palabra=list(a)

print (palabra)

i=0
while (i<len(palabra)):
    cont=1
    j=i+1
    while(j<len(palabra)):
        if (palabra[i]==palabra[j]):
            cont+=1
            palabra.pop(j)
        j+=1
    print (palabra[i],": ",end="")
    for k in range(cont):
        print ("*",end="")
    print()
    i+=1



