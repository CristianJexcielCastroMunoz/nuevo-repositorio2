# Solicitamos al usuario que ingrese un número de teléfono con un formato específico
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")

# Extraemos la parte del número de teléfono sin el código de país ni el código final
numero_telefono = tel[4:-3]

# Mostramos el número de teléfono extraído
print('El número de teléfono es', numero_telefono)
