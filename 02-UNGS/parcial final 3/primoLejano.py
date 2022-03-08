#ejercicio 1 PARCIAL
#primos lejanos
def esPrimoLejano(n):
    cont=0
    for i in range(1,n+1):
        if(n%i==0):
            cont+=1
    if cont<=3:
        return(True)
    else:
        return(False)

def primosLejanos(cantidad,inicio):
    lista=[]
    i=inicio
    while(len(lista)<cantidad):
        if(esPrimoLejano(i)):
            lista.append(i)
        i+=1
    return(lista)

print (primosLejanos(3,4))

