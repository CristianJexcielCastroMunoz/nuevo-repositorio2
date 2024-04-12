#  ingrese su peso en kilogramos
peso = float(input("Por favor, ingresa tu peso en kilogramos (ej. 70.5): "))

#  ingrese su estatura en metros
estatura = float(input("Por favor, ingresa tu estatura en metros (ej. 1.75): "))

# Calculamos el Índice de Masa Corporal (IMC) y lo redondeamos a dos decimales
imc = round(peso / estatura ** 2, 2)

# Mostramos el resultado al usuario
print(f"Tu índice de masa corporal es {imc}")
