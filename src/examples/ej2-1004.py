'''
Escribe un programa que calcule el factorial de un número entero positivo ingresado por el usuario. El programa debe:

Pedir al usuario que ingrese un número entero positivo.
Validar que el número ingresado sea válido (es decir, que sea un entero positivo).
Calcular el factorial del número utilizando únicamente un bucle while.
Mostrar el resultado al usuario.
Nota: El factorial de un número n (denotado como n!) se define como el producto de todos los números enteros positivos desde 1 hasta n. Por ejemplo:


Si el número es 0, el factorial es 1 por definición.

Inicializar una variable para almacenar el resultado del factorial (por ejemplo, factorial = 1).

Usar un bucle while para multiplicar los números desde 1 hasta n.
Mostrar el resultado al usuario.
3. Pistas para llegar al pseudocódigo:

Cálculo: Usa un bucle while para multiplicar factorial por i y luego incrementar i hasta que alcance el número ingresado.
Salida: Imprime el valor de factorial.
    
    '''
numero = int(input("Ingresa tu tontera: "))
if numero > 0:
    i = 1 #contador
    y = 1 #acumulado
    while i <= numero:
        y = y * i
        i +=1 # i = i + 1
    print(y)

elif numero == 0:
    print("Factorial de 0 es 1")
else:
    print("Mala tu cuestion")