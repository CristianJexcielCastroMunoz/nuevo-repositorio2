# introduzca el precio del producto con dos decimales
precio = input("Introduce el precio del producto con dos decimales (ejemplo: 12.50): ")

# Dividimos el precio en euros y céntimos utilizando el punto como separador
euros, centimos = precio.split('.')

# Imprimimos el resultado en un formato más legible
print(f"{euros} euros y {centimos} céntimos.")
