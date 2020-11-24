#Suponga que una persona desea invertir su capital en un banco y quiere saber cuanto dinero tendra
#después de cada mes si el banco incrementa el 6% mensual(no acumulativo).

dinero=float(input("Ingrese su capital a invertir: "))
meses=int(input("Indique cuantos meses deja el dinero en el banco: "))

capital=dinero+dinero*0.06*meses

print("Usted recibira:$", capital)