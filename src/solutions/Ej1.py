while True:
    # Pedir el primer número
    num1 = int(input("Ingresa el primer número: "))

    # Pedir el segundo número
    num2 = int(input("Ingresa el segundo número: "))

    # Mostrar el menú de opciones
    print("""
    Menú:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
""")
    
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1 * num2}")
    elif opcion == "4":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("No se puede dividir entre 0.")
    elif opcion == "5":
        print("Adiós!")
        break
    else:
        print("Opción no válida.")
