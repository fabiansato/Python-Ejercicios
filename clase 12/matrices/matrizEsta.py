def estaMatriz(a,Mat):
    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            if (Mat[i][j]==a):
                return True

    return False

numeros = [[1,2,4],[4,3,2],[9,8,7],[6,4,3],[5,6,8]]
elemento=10
print(estaMatriz(elemento,numeros))


