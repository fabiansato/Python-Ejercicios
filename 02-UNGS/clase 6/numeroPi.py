print ("Calcularemos PI")
n=int(input("Ingrese la cantidad de terminos"))
suma = 0
signo = 1
for i in range(1,n+1,2): # 1,3,5,...,n
    suma = suma + 1/i * signo
    signo=-signo
print(4*suma)



import math
print ("Calcularemos PI")
epsilon=0.000001
suma = 0
signo = 1
i=1
pi=math.pi
while(abs(4*suma-pi)>epsilon):
    suma = suma + 1/i * signo
    signo=-signo
    i=i+2
print(4*suma)