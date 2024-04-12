#ingrese el número de barras vendidas que no son frescas
barras_no_frescas = int(input("Introduce el número de barras vendidas que no son frescas: "))

# Definimos el precio de una barra fresca y el descuento aplicado a las barras no frescas
precio_barra_fresca = 3.49 
descuento_no_frescas = 0.6

# Calculamos el coste final aplicando el descuento a las barras no frescas
coste_final = barras_no_frescas * precio_barra_fresca * (1 - descuento_no_frescas)

# Mostramos por pantalla el precio de una barra fresca, el descuento aplicado y el coste final a pagar
print(f"El coste de una barra fresca es {precio_barra_fresca}€")
print(f"El descuento sobre una barra no fresca es {descuento_no_frescas * 100}%")
print(f"El coste final a pagar es {round(coste_final, 2)}€")


#añadi comentarios para explicar cada paso del código
#se agrego el costo_final