# son COPRIMOS
def coprimos(a,b):
    for i in range(2,a+1):
        if(a%i == 0 and b%i == 0):
            return(False)
    return(True)

a = int(input("un numero"))
b = int(input("otro numero"))
if(coprimos(a,b)):
    print("son coprimos")
else:
    print("no son coprimos")