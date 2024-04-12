# Ejercicio 11 - Repetir nombre
# Este programa pide al usuario su nombre y un número entero
# Luego, imprime el nombre del usuario tantas veces como el número introducido

# Solicitamos el nombre del usuario
nombre = input("¿Cómo te llamas? ")

# Solicitamos un número entero al usuario
n = input("Introduce un número entero: ")

# Convertimos el número a entero y repetimos el nombre
# tantas veces como el número introducido
print((nombre + "\n") * int(n))
