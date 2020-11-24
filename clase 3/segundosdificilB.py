print ("Este programa calcula los segundos en dias horas minutos y segundos BIEN")
s_tot=int(input("Ingrese la cantidad de segundos: "))

m_tot = s_tot // 60	# total minutos
h_tot = m_tot // 60	# total horas
d_tot = h_tot // 24	# total dias

s_res = s_tot - m_tot * 60	# resto segundos
m_res = m_tot - h_tot * 60	# resto minutos
h_res = h_tot - d_tot * 24	# resto horas

print ("La cantidad de dias es: ",d_tot)
print ("La cantidad de horas es: ",h_res)
print ("La cantidad de minutos es: ",m_res)
print ("La cantidad de segundos es: ",s_res)