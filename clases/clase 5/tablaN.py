print("Este programa calcula la tabla que usted quiera")
n=int(input("Ingrese un numero: "))
k=int(input("Ingrese hasta donde quiere calcular: "))
for i in range (1,k+1,1):
    print (n,"*",i,"=",n*i)