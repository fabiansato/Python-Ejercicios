n=int(input("Ingrese cantidad de terminos"))
suma=1
signo=1
while n < 4:
    print ("no se puede")
    n=int(input("Ingrese cantidad de terminos"))

for i in range(2,n+1):
      suma=suma+1/2**i * signo
      signo=-signo

print("Suma: ",suma)
