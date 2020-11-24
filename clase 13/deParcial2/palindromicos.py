#palindromicos
def esPalindromico(lista):
    n=len(lista)
    for i in range(n): # se podría recorrer solo la mitad
      if (lista[i]!=lista[n-1-i]):
          return False
    return True

a=input("ingrese un numero") #lo dejo como cadena
print (esPalindromico(a))


