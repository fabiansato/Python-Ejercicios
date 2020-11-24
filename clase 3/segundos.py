
segundosIngresados=int(input("ingresar segundos"))
minutos=60 #segundos
horas=minutos*60 #3600 segundos
dias=horas * 24 #86400 segundos

print(segundosIngresados//dias, "dia(s)",
(segundosIngresados%dias)//horas, "hora(s)",
((segundosIngresados%dias)%horas)//minutos, "minuto(s)",
(((segundosIngresados%dias)%horas)%minutos), "segundo(s)"
)