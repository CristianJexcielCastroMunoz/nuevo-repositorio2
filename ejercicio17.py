# Pedimos al usuario que introduzca su correo electrónico
email = input("Introduce tu correo electrónico: ")

# Extraemos la parte del usuario del correo electrónico (antes de la @)
usuario_email = email[:email.find('@')]

# Concatenamos la parte del usuario con el dominio de la universidad
nuevo_email = usuario_email + '@ceu.es'

# Mostramos el nuevo correo electrónico al usuario
print(nuevo_email)


#añadi comentarios en cada parte del codigo para que sea mas facil entender
