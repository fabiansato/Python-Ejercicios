a=int(input("Ingrese un numero"))
b=int(input("Ingrese un numero"))

if(a==0 or b==0):
    print("0")
else:
    if (a>0 and b>0) or (a<0 and b<0):
            print("+")
    else:
        print("-")

