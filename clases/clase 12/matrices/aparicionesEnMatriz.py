def AparicionesEnMatriz(a,Mat):
    lista=[]
    for i in range(len(Mat)):
        cont=0
        for j in range(len(Mat[i])):
            if (Mat[i][j]==a):
                cont+=1
        lista.append(cont)
    return lista



numeros = [[1,2,4],[4,3,2],[9,8,7],[6,4,3],[5,6,8]]
elemento=2
print(AparicionesEnMatriz(elemento,numeros))