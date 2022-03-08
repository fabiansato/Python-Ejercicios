pswd=1234
dato=int(input(""))
cont=1

while(pswd!=dato and cont < 3):
    cont=cont+1
    dato=int(input(""))

if(pswd==dato):
    print("Acceso")
else:
    print("Usuario Bloqueado")