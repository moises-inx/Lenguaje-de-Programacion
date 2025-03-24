# Problema 01 

# "Construya un programa usando lenguaje de programación Python que lea el valor de un número entero y que lo despliegue"

numero_entero = int(input("Ingrese un número entero: "))

print("El número entero ingresado es: ", numero_entero)

# Problema 02

#"Construya un programa usando lenguaje de programación Python que lea el valor de un número entero, que calcule su sucesor y que despliegue simultáneamente el número ingresado y su sucesor."

numero_entero01 = int(input("Ingrese un número entero: ")) 

print("El número entero ingresado es: ", numero_entero01, "el sucesor del número ingresado es: ", numero_entero01 + 1 )

# Problema 03

#"Construya un programa usando lenguaje de programación Python que lea el valor de un número real x, quecalcule −3x^3 + 5x^2 + 6x − 6 y que despliegue simultáneamente el número ingresado y el resultado de evaluar x en la ecuación"

numero_para_calcular = float(input("Ingrese un número real: "))

resultado_ecuacion = -3 * numero_para_calcular ** 3 + 5 * numero_para_calcular ** 2 + 6 * numero_para_calcular - 6

print("El número real ingresado es: ", numero_para_calcular) 

print("El resultado de evaluar x en la ecuación es: ", resultado_ecuacion)

# Problema 04

#"Construya un programa usando lenguaje de programación Python que lea el valor de dos números enteros, que los almacene en distintas variables, que luego se intercambien los valores entre las variables y finalmente que las despliegue."

n = int(input("Ingrese un número entero (n): "))
m = int(input("Ingrese otro número entero (m): "))

n, m = m, n

print("El valor de n es: ", n)
print("El valor de m es: ", m)

# Problema 05

#"Construya un programa usando lenguaje de programación Python que lea dos strings, el nombre y el apellido de una persona, luego debe desplegar una variable que contenga el nombre completo"

nombre = (input("Ingrese su nombre: "))

apellido = (input("Ingrese su apellido: "))

nombre_completo = nombre + " " + apellido

print("El nombre completo es: ", nombre_completo)

# Problema 06

#"Construya un programa usando lenguaje de programación Python que lea un símbolo y un número entero n. Luego el programa debe desplegar un rectángulo de lados 3 y n dibujados con el símbolo ingresado."

simbolo = input("Ingrese un símbolo: ")

tamaño= int(input("Ingrese un número entero: "))

print(simbolo * tamaño)

print(simbolo + " " * (tamaño - 2) + simbolo)

print(simbolo * tamaño)

#Fin.
