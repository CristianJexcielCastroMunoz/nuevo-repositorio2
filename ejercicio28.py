# Se solicita al usuario que ingrese el precio del producto con dos decimales
precio = input("Introduce el precio del producto con dos decimales (ejemplo: 12.99):  ")

# Se verifica que el usuario haya ingresado un precio con dos decimales
if '.' in precio and len(precio.split('.')[1]) == 2:
    # Se separa el precio en euros y céntimos utilizando el punto decimal como referencia
    euros = precio.split('.')[0]
    centimos = precio.split('.')[1]

    # Se imprime el resultado en formato legible
    print(f"{euros} euros y {centimos} céntimos.")
else:
    # Si el usuario no ingresó el precio en el formato correcto, se le informa
    print("Por favor, ingresa el precio en el formato correcto (ejemplo: 12.99).")


#añadi un mensaje de error en caso de que el usuario no cumpa con el formato

