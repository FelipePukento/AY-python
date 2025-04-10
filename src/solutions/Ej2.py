# Pedir al usuario un número entero positivo
n = -1  # Inicializamos con un valor inválido para entrar al bucle
while n < 0:
    input_value = input("Enter a positive integer to calculate its factorial: ")
    if input_value.isdigit():  # Verificar si la entrada es un número positivo
        n = int(input_value)
        if n < 0:
            print("Please enter a positive integer.")
    else:
        print("Invalid input. Please enter an integer.")

# Caso especial: factorial de 0 es 1
if n == 0:
    print("The factorial of 0 is: 1")
else:
    # Inicializar variables
    factorial = 1
    i = 1

    # Calcular el factorial usando un bucle while
    while i <= n:
        factorial *= i
        i += 1

    # Mostrar el resultado
    print(f"The factorial of {n} is: {factorial}")