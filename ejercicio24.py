# ingrese los datos necesarios al usuario
cantidad_invertida = float(input("Ingrese la cantidad a invertir: "))
tasa_interes = float(input("Ingrese el interés porcentual anual: "))
periodo_inversion = int(input("Ingrese la cantidad de años: "))

# Calculamos el capital final aplicando la fórmula del interés compuesto
capital_final = round(cantidad_invertida * ((1 + tasa_interes / 100) ** periodo_inversion), 2)

# Mostramos el resultado al usuario
print(f"El capital final tras {periodo_inversion} años será de: {capital_final}")

