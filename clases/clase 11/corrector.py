a=input("Ingrese una palabra")
palabra=list(a)

print (palabra)

for i in range(len(palabra)-1):
    if (palabra[i]=='n' and (palabra[i+1]=='b' or palabra[i+1]=='p')):
        palabra[i]='m'

print (palabra)

