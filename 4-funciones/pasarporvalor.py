'''
Ejemplo de paso por valor

Como ya sabemos los números se pasan por valor y crean una copia dentro de la función, por eso no les afecta externamente lo que hagamos con ellos:
'''

def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)