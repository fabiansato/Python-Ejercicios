#Hacer un programa que permita al usuario elegir un número n y un número c, y
#luego muestre los c números naturales que le siguen a n (n + 1; n + 2;    ; n + c).

n=int (input("Ingrese un numero"))
c=int (input("Ingrese otro numero"))

for i in range(n,n+c+1,1):
    print (i) #uno debajo del otro

#for i in range(n,n+c+1,1):
#    print (i,end=" ") #uno al lado del otro