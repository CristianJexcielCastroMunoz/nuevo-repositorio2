# ingrese una frase
frase = input("Introduce una frase: ")
# ingrese una vocal en minúscula
vocal = input("Introduce una vocal en minúscula: ")

# Verificamos el ingreso de una sola letra y que sea una vocal minúscula
if len(vocal) == 1 and vocal in "aeiou":
    frase_modificada = frase.replace(vocal, vocal.upper())
    # Mostramos la frase modificada
    print(frase_modificada)
else:
    # Si no ingresó una vocal minúscula válida, mostramos un mensaje de error
    print("Error: Debes introducir una vocal en minúscula.")


#añadi una verificacion para asegurar de que se hubiera puesto una vocal minúscula. 
#se agrego un mensaje de error por si no se hubiera puesto una vocal en minúscula
#mas comentarios en cada parte del codigo 