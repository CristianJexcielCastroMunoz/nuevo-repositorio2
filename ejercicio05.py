# Solicitamos la edad y los ingresos mensuales del usuario
edad = int(input("¿Cuál es tu edad? "))
ingresos_mensuales = float(input("¿Cuáles son tus ingresos mensuales? "))

# Verificamos si el usuario debe cotizar
if edad > 16 and ingresos_mensuales >= 1000:
    print("Debes cotizar.")
else:
    print("No necesitas cotizar.")



#comentarios 
#Añadi un espacio después del signo de interrogación en los mensajes de entrada para mejorar.
#Modifique los mensajes de salida para que sean más claros y directos.
