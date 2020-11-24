#NÃºmero poderoso: todo nÃºmero natural n que cumple que si un primo p es un
#divisor suyo entonces p2 tambiÃ©n lo es. Por ejemplo, el nÃºmero 36 es un
#nÃºmero poderoso ya que los Ãºnicos primos que son divisores suyos son 2 y 3
# y se cumple que 4 y 9 tambiÃ©n son divisores de 36.

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


