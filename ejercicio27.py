# Solicitamos al usuario que ingrese su fecha de nacimiento en formato día/mes/año
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")

# Separamos la fecha en día, mes y año utilizando el método split()
partes_fecha = fecha.split('/')

# Asignamos cada parte de la fecha a una variable correspondiente
dia = partes_fecha[0]
mes = partes_fecha[1]
año = partes_fecha[2]

# Imprimimos el día, mes y año por separado
print('Día:', dia)
print('Mes:', mes)
print('Año:', año)


#he agragado comentarios al explicar cada paso del código