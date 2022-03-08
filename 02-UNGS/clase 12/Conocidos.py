#Hacer un programa que solicite al usuario 2 numeros e indique si son numeros Conocidos
#Son dos enteros positivos a y b tales que a es la suma de los primeros divisores de b y b es la suma de los primeros divisores de a.
#Un ejemplo es el par (220,284), ya que:
#Los primeros divisores de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284.
#Los primeros  divisores 284 son 1, 2, 4, 71 y 142, que suman 220.
#AdemÃ¡s el programa debe indicar cuantos divisores fueron necesarios sumar para llegar al otro nÃºmero conocido. (220,284) fueron necesarios 11 y 5 divisores. Si no son conocidos, indicar si alguno conoce al otro.

a=int (input("ingrese un numero"))
b=int (input("ingrese otro numero"))

sumaA=0
contA=0
for i in range (1,a+1,1):
    if (a%i==0 and sumaA<b):
        sumaA=sumaA+i
        contA=contA+1

sumaB=0
contB=0
for i in range (1,b+1,1):
    if (b%i==0 and sumaB<a):
        sumaB=sumaB+i
        contB=contB+1

if (sumaA==b and sumaB==a):
    print (a,b,"Son conocidos")
    print ("Hizo falta",contA,"y",contB,"divisores")
elif (sumaA==b):
    print (a,"Conoce a ",b)
elif (sumaB==a):
    print (b,"Conoce a ",a)
else:
    print ("No son conocidos")
#print ("SumaA",sumaA,"SumaB",sumaB)