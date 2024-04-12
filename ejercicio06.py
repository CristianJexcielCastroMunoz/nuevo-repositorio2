# Solicitamos el nombre y el sexo del usuario
nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")

# Eliminamos espacios en blanco al inicio y al final del nombre
nombre = nombre.strip()

# Asignamos el grupo en base a la primera letra del nombre y el sexo
if sexo.upper() == "H":
    if nombre[0].lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
elif sexo.upper() == "M":
    if nombre[0].lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
else:
    grupo = "Inválido"

# Imprimimos el grupo asignado
print(f"Tu grupo es {grupo}")


#comentarios: 
#he añadido un mensaje de "Inválido" en caso de que el sexo ingresado no sea ni "M" ni "H".
#tambien mas comentarios como para explicar mas el codigo