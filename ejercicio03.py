try:
    n = float(input("Introduce el dividendo: "))
    m = float(input("Introduce el divisor: "))
    if m == 0:
        print("¡Error! No se puede dividir por 0. Por favor, introduce un divisor diferente de 0.")
    else:
        resultado = n / m
        print(f"El resultado de la división es: {resultado}")
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")


#comentarios 
#agrege un mensaje para mas claro para el usuario al pedir los valores y al mostrar el resultado.
#cambie un mensaje de error para que sea más específico y guíe al usuario a poner un divisor diferente de 0.
 