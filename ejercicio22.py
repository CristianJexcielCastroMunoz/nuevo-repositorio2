# Definimos las constantes para el peso de los payasos y las muñecas
PESO_PAYASO = 112
PESO_MUÑECA = 75

# ingresa el número de payasos y muñecas a enviar
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))

# Calculamos el peso total del paquete
peso_total = PESO_PAYASO * payasos + PESO_MUÑECA * muñecas

# Mostramos el resultado al usuario
print(f"El peso total del paquete es {peso_total} gramos.")

#Se definio los pesos de los payasos y las muñecas en mayúsculas 
#Se agrego "gramos" al final para que sea mas claro para el usario
