'''
Teniendo estas deniciones de funciones:
de f cuak ( ) :
chan ( )
pr int ( "pienso que " , end="" )
chan ( )
de f chan ( ) :
pr int ( "yo" , end="" )
p l i n ( )
de f p l i n ( ) :
pr int ( "." )
Indicar qué se imprime en pantalla luego de ejecutar este programa:
pr int ( "No, yo " , end="" )
cuak ( )
pr int ( "Yo " , end="" )
chan ( )
AYUDA: Empezar describiendo con palabras qué hacen chan y cuak cuando se las llama.
REGLA: No vale correrlo en la computadora.

Respuesta: 
No, yo yo.
pienso que yo.
Yo yo.
'''

def cuak():
    chan()
    print("pienso que ", end="")
    chan()

def chan():
    print("yo", end="")
    plin()

def plin():
    print (".")

print ("No, yo ", end="")
cuak()
print ("Yo ", end="")
chan()
