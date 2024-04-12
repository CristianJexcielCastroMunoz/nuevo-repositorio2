# ingrese el nombre del producto
producto = input('Introduce el nombre del producto: ')

# ingrese el precio unitario del producto y lo convertimos a float
precio = float(input('Introduce el precio unitario: '))

# ingrese el número de unidades del producto y lo convertimos a int
unidades = int(input('Introduce el número de unidades: '))

# Calculamos el total multiplicando el precio por las unidades
total = unidades * precio

# Imprimimos el recibo con el formato adecuado
print(f'{producto}: {unidades} unidades x {precio:.2f}€ = {total:.2f}€')

