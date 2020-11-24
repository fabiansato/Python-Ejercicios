import random
def printMatrix(Matricita,filas,columnas):
    for i in range(filas):
        print()
        for j in range(columnas):
            print(Matricita[i][j],end="  ")

def llenarRandom(M,filas,columnas,max):
    for i in range(filas):
        for j in range(columnas):
            M[i][j]=random.randint(0,max)

def ConstruirIdentidad(M, filas):
      for i in range(filas):
        for j in range(filas):
            if i==j:
                M[i][j]=1
            else:
                M[i][j]=0

def EsIdentidad(M,filas,columnas):
    for i in range(filas):
        for j in range(filas):
            if i==j and M[i][j]!=1:
                return False
            if i!=j and M[i][j]!=0:
                return False
    return True


def SumaEnVector(M,filas, columnas):
    lista=[]
    for i in range(filas):
        suma=0
        for j in range(filas):
            suma=suma+M[i][j]
        lista.append(suma)
    return lista


FILAS = 4
COLUMNAS = 4

Vec = [0 for j in range(COLUMNAS)]  # Vec = [0,0,0,0,0,0]
print(Vec)

Mat = [ [0 for j in range(COLUMNAS)] for i in range(FILAS)]

printMatrix(Mat,FILAS,COLUMNAS)
print()
max=10
llenarRandom(Mat,FILAS,COLUMNAS,max)
printMatrix(Mat,FILAS,COLUMNAS)

print ()

ConstruirIdentidad(Mat,FILAS)
printMatrix(Mat,FILAS,COLUMNAS)

print ()

print(EsIdentidad(Mat,FILAS,COLUMNAS))

print()
print(SumaEnVector(Mat,FILAS,COLUMNAS))


