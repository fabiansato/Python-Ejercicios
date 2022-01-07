def cantDivisores(n):
    cant=0
    for i in range(1,n+1):
        if n%i==0:
            cant=cant+1
    return(cant)

def esPrimo(m):
    if cantDivisores(m)==2:
        return True
    else:
        return False