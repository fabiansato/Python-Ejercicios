def Max(lista):
    maximo=lista[0]
    posMax=0
    for i in range(1,len(lista)):
        if lista[i]>maximo:
            maximo=lista[i]
            posMax=i
    return posMax

def GandeAlFondoMatriz(Mat):
    for i in range(len(Mat)):
        pos= Max(Mat[i])
        aux= Mat[i][pos]
        Mat[i][pos]= Mat[i][len(Mat[i])-1]
        Mat[i][len(Mat[i])-1]= aux
    return Mat

numeros = [[1,2,4],[4,3,2],[9,8,7],[6,4,3],[5,6,8]]
elemento=2
print(GandeAlFondoMatriz(numeros))