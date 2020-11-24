print ("Calcularemos E")
n=int(input("Ingrese la cantidad de terminos"))
suma = 1
factorial=1
for i in range(1,n): # 1,2,3,4,5,...,n
    factorial=factorial*i
    suma = suma + 1/factorial
print(suma)

