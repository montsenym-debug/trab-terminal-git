# Lista de objetos a evaluar
elementos = ["pinza", "tijera", "pinza"]

# Cantidad esperada de pinzas
esperadas = 2

# Inicializamos el contador en 0
contador = 0

# Bucle for para recorrer cada elemento de la lista
for elemento in elementos:
    # Condicion para contar solo si el elemento es "pinza"
    if elemento == "pinza":
        contador = contador + 1

# Comparacion final usando if, elif y else
if contador < esperadas:
    print("Faltan pinzas.")
elif contador > esperadas:
    print("Sobran pinzas.")
else:
    print("Las pinzas coinciden.")