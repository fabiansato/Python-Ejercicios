'''
Hacer una función que indique si un número es Poderoso:
Número poderoso: todo número natural n que cumple que si un primo p es un divisor suyo entonces p2 también lo es. Por ejemplo, el número 36 es un número poderoso ya que los únicos primos que son divisores suyos son 2 y 3 y se cumple que 4 y 9 también son divisores de 36.
Luego hacer un programa que use la función.

'''
def primo(n):
    bandera=True
    for i in range(2,n//2+1):
        if(n%i==0):
            bandera=False
    return bandera

a=int(input("Ingrese un numero"))
poderoso=True
for i in range (1,a+1):
    if(a%i==0 and primo(i)):
        if(a%(i*i)!=0):
            poderoso=False

if (poderoso==True):
    print(a,"Si es poderoso")
else:
    print(a,"NO es poderoso")


