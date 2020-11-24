dinero=int(input("Ingrese el monto de dinero"))
dineroInicial=dinero

cien= dinero//100
dinero= dinero % 100

cincuenta= dinero//50
dinero= dinero % 50

veinte= dinero//20
dinero= dinero % 20

diez= dinero//10
dinero= dinero % 10

cinco= dinero//5
dinero= dinero % 5

dos= dinero//2
dinero= dinero % 2

print(dineroInicial, "son", cien,"de 100 pesos")
print(cincuenta ,"de 50 pesos")
print(veinte,"de 20 pesos")
print(diez,"de 10 pesos")
print(cinco,"de 5 pesos")
print(dos,"de 2 pesos")
print(dinero ,"de 1 peso")