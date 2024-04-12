# ingrese la cantidad de dinero que desea invertir
inversion_inicial = float(input("Introduce la inversión inicial: "))

# Establecemos la tasa de interés anual
tasa_interes = 0.04

# Calculamos el balance después del primer año
balance_ano_1 = inversion_inicial * (1 + tasa_interes)
print(f"Balance tras el primer año: {round(balance_ano_1, 2)}")

# Calculamos el balance después del segundo año
balance_ano_2 = balance_ano_1 * (1 + tasa_interes)
print(f"Balance tras el segundo año: {round(balance_ano_2, 2)}")

# Calculamos el balance después del tercer año
balance_ano_3 = balance_ano_2 * (1 + tasa_interes)
print(f"Balance tras el tercer año: {round(balance_ano_3, 2)}")

#solo añadi varios comentarios en el codigo para que el usario lo use de manera mas facil.