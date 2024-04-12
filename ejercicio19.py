fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
# Separamos la fecha en día, mes y año utilizando el método split()
fecha_separada = fecha.split('/')
dia = fecha_separada[0]
mes = fecha_separada[1]
año = fecha_separada[2]

# Imprimimos los resultados
print('Día:', dia)
print('Mes:', mes)
print('Año:', año)
