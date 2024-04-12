# Solicitar al usuario su renta anual
renta = float(input("¿Cuál es tu renta anual? "))

# Determinar el tipo impositivo en función de la renta
if renta < 10000:
    tipo_impositivo = 5
elif renta < 20000:
    tipo_impositivo = 15
elif renta < 35000:
    tipo_impositivo = 20
elif renta < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

# Calcular el impuesto a pagar
impuesto = renta * tipo_impositivo / 100

# Mostrar el impuesto a pagar
print(f"Tienes que pagar {impuesto:.2f}€ en impuestos.")

#comentarios:
#Se ha añadido un mensaje claro y descriptivo al solicitar la entrada del usuario. 


