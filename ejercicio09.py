# Se solicita la edad del usuario y se convierte a entero
edad = int(input("Introduce tu edad: "))

# Se inicializa la variable precio
precio = 0

# Se decide el precio en función de la edad
if edad < 4:
    # Si la edad es menor a 4 años, la entrada es gratuita
    precio = 0
elif edad <= 18:
    # Si la edad está entre 4 y 18 años, el precio es de 4 euros
    precio = 4
else:
    # Si la edad es mayor a 18 años, el precio es de 10 euros
    precio = 10 

# Se muestra el precio de la entrada
print(f"El precio de la entrada es {precio} €")
 

 #Comentarios:
 # he agregado un comentario al principio para explicar que se solicita la edad al usuario y que se convierte a entero.
 #he agregado comentarios en cada condición para explicar la lógica de los precios en función de la edad.