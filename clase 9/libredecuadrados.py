#Número libre de cuadrados: todo número natural que cumple que en su
#descomposición en factores primos no aparece ningún factor repetido.
#Por ejemplo, el número 30 es un número libre de cuadrados.

def primo(n):
    bandera=True
    for i in range(2,n//2+1):
        if(n%i==0):
            bandera=False
    return bandera


a=int(input("Ingrese un numero"))
producto=1
for i in range(1,a+1):
    if(a%i==0 and primo(i)):
        producto=producto*i;

if(producto==a):
    print(a,"SI es libre de cuadrados")
else:
    print(a,"NO es libre de cuadrados")