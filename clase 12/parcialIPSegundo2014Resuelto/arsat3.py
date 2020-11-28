#una forma de resolverlo

sat=3
lista=Estacionar(Localizacion_geo(sat),"81Oeste")
motor=lista[0]
tiempo=lista[1]
for t in range(tiempo):
    if motor=="sur":
        Motor_sur()
    elif motor=="norte":
        Motor_norte()
    elif motor=="este":
        Motor_este()
    else:
        Motor_oeste()
Desplegar_celdas(sat)
while Carga_baterias(sat)>=80:
    Transmitir(sat)