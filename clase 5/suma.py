n=int(input("Indique hasta que numero quiere sumar"))
suma=0
for i in range(1, n, 1):
    suma=suma+i
    print(i, "+ ", end="")

suma=suma+n
print(n, end="")

print(" =", suma)

print("La suma de los primeros", n, "naturales es:", suma)