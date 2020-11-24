n = int(input("Ingrese cantidad de alumnos"))

listaAlumnos = []
listaNotas = []
suma = 0
for i in range(n):
    alumno = input("Ingrese el nombre")
    nota = int(input("Ingrese una nota"))
    listaAlumnos.append(alumno)
    listaNotas.append(nota)
    suma = suma + nota

promedio = suma/n

print("El promedio es:", promedio)

print("Las notas mayor al promedio son:")
for i in range(n):
    nota = listaNotas[i]
    if(nota >= promedio):
        print(nota)

print("Las notas mayor o igual a 7 son:")
for i in range(len(listaNotas)):
    nota = listaNotas[i]
    if(nota >= 7):
        print(nota)

print("Las notas entre 4 y menor a 7 son:")
for nota in listaNotas:
    if(nota >= 4 and nota < 7 ):
        print(nota)

print("Los alumnos desaprobados son:")
for i in range(n):
    nota = listaNotas[i]
    if(nota < 4):
        print("Nombre:", listaAlumnos[i])
        print("Nota:" ,nota)

