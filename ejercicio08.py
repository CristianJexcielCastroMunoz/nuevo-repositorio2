# Valores de referencia para los niveles de rendimiento
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
bonificacion = 2400

# Solicitar la puntuación al usuario
try:
    puntoss = float(input("Introduce tu puntuación: "))
except ValueError:
    print("Por favor, introduce un número válido.")
    puntoss = None

if puntoss is not None:
    # Clasificación por niveles de rendimiento
    if puntoss == inaceptable:
        nivel = "Inaceptable"
    elif puntoss == aceptable:
        nivel = "Aceptable"
    elif puntoss == meritorio:
        nivel = "Meritorio"
    else:
        nivel = "No definido"

    # Mostrar nivel de rendimiento
    if nivel == "No definido":
        print("Esta puntuación no es válida.")
    else:
        print("Tu nivel de rendimiento es: " + nivel)
        bonificacion_total = puntoss * bonificacion
        print("Te corresponde cobrar %.2f€" % bonificacion_total)

