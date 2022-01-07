




import math
log2=math.log(2)
print(log2)

suma=0
i=1
while(abs(log2-suma)>=0.0001):
    termino=1/i
    if i%2==0:
        suma=suma-termino
    else:
        suma=suma+termino
    i=i+1
print(i,suma)
