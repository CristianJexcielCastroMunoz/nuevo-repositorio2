key = "contraseña"  # Definimos la contraseña correcta en una variable
password = input("Introduce la contraseña: ")  # Pedimos al usuario que introduzca la contraseña

# Comparamos la contraseña introducida con la correcta, sin importar si está en mayúsculas o minúsculas
if key == password.lower(): 
    print("La contraseña coincide")  # Si coincide, mostramos un mensaje de confirmación
else: 
    print("La contraseña no coincide")  # Si no coincide, mostramos un mensaje de error



#comentarios
#Añadir comentarios para explicar cada paso del código, haciéndolo más legible y comprensible para otros usarios.
#Eliminar los espacios innecesarios para el código para mejorar la legibilidad y seguir las buenas prácticas de codificación.