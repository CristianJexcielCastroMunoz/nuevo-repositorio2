# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.")
print("Tipos de pizza:")
print("\t1- Vegetariana")
print("\t2- No vegetariana\n")

tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")

# Decisión sobre el tipo de pizza
if tipo == "1":
    print("\nIngredientes de pizzas vegetarianas:")
    print("\t1- Pimiento")
    print("\t2- Tofu\n")
    
    ingrediente = input("Introduce el ingrediente que deseas: ")
    
    print("Has elegido una pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento.")
    else: 
        print("tofu.")
else:
    print("\nIngredientes de pizzas no vegetarianas:")
    print("\t1- Peperoni")
    print("\t2- Jamón")
    print("\t3- Salmón\n")
    
    ingrediente = input("Introduce el ingrediente que deseas: ")
    
    print("Has elegido una pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni.")
    elif ingrediente == "2":
        print("jamón.")
    else:
        print("salmón.")


#Comentario
#he agregado mensajes claros para indicar la elección del usuario después de que seleccionan sus ingredientes.
#he mantenido la lógica del código original, pero hay mejoras en la presentación y la claridad de los mensajes al usuario.