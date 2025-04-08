# Problema de referencia (hecho por mi cuenta).

#Ingresan N (N > 0)) clientes a un supermercado, cada uno de ellos compra P (P > 0) productos. Construya un programa en Python que lea la cantidad de clientes y, por cada uno de ellos, lea la cantidad de productos que lleva. El programa luego debe permitir el ingreso de los precios de cada uno de los P productos comprados, calculando el valor total de la compra de cada cliente. Finalmente, por cada cliente, si el total de la compra es menos de $10000 no se le aplica descuento y el cliente paga el valor total calculado, si el valor total de la compra de un cliente es mayor o igual a $10000 y menos de $20000 se le aplica 10 % de descuento. Finalmente, si el total de la compra de un cliente es mayor o igual a $20000 se le aplica un 15 % de descuento.

numero_de_clientes = int(input("Ingrese la cantidad de clientes: "))
productos = []
for i in range(numero_de_clientes):
    cliente = []
    numero_de_productos = int(input("Ingrese la cantidad de productos que lleva el cliente: "))
    for j in range(numero_de_productos):
        precio_producto = float(input("Ingrese el precio del producto: "))
        cliente.append(precio_producto)
        if precio_producto <= 0:
            print("El precio del producto debe ser mayor a cero.")
            break
        elif precio_producto < 10000:
            total = precio_producto
            print("El total de la compra es: ", total)
        elif precio_producto >= 10000 and precio_producto < 20000:
            total = precio_producto * 0.1
            print("El total de la compra es: ", total)
        else:
            total = precio_producto * 0.15
            print("El total de la compra es: ", total)

            cliente.append(precio_producto)
    productos.append(cliente)
    
# Problema 1.

#Construya un programa en Python que genere la secuencia de números enteros entre el −10 y el 10

numeros= []
for i in range(-10,11):
    numeros.append(i)
print(numeros)

#Problema 2.

#Construya un programa en Python que lea un número entero n y que genere la secuencia de números enterosentre el −|n| y el |n|.

#Problema 2, forma 1.
n= int(input("Ingrese un número entero: "))
numeros= []
for i in range(-abs(n),abs(n)+1):
    print(i, end=" ")
    
#Problema 2, forma 2.
n= int(input("Ingrese un número entero: "))
numeros= []
for i in range(-abs(n),abs(n)+1):
    numeros.append(i)
    print(numeros)
    
#Problema 3.

#Construya un programa usando lenguaje de programación Python que lea un conjunto de números enteros y que por cada uno despliegue la palabra “Positivo” si el número ingresado es mayor que cero, si el número ingresado es menor que cero el programa debe desplegar “Negativo” y de lo contrario el programa debe desplegar “Cero”. El programa termina cuando se ingresa el valor cero.

while True:
    numero = int(input("Ingrese un número entero (el programa termina al ingresar el número cero): "))
    if numero == 0:
        print("Cero")
        break
    elif numero > 0:
        print("Positivo")
    else:
        print("Negativo")
        
#Problema 4.

#Construya un programa usando lenguaje de programación Python que lea un conjunto de números enteros y que por cada uno despliegue la palabra “Positivo” si el número ingresado es mayor que cero, si el número ingresado es menor que cero el programa debe desplegar “Negativo” y de lo contrario el programa debe desplegar “Cero”. El programa termina cuando se ingresa la letra “F”.
while True:
    numero = input("Ingrese un número entero (el programa termina al ingresar la letra F): ")
    if numero == "F":
        print("Fin del programa")
        break
    try:
        numero = int(numero)
        if numero > 0:
            print("Positivo")
        elif numero < 0:
            print("Negativo")
        else:
            print("Cero")
    except ValueError:
        print("Por favor, ingrese un número entero o 'F' para salir.")
        
#Problema 5.

#Construya un programa usando lenguaje de programación Python que lea el valor de un número entero y que lo despliegue solo si el valor es mayor que cero. Mientras no se ingrese un valor positivo, el algoritmo debe generar el mensaje “Error, valor mal ingresado”.

#Construya un programa usando lenguaje de programación Python que lea el valor de un número entero y que lo despliegue solo si el valor es mayor que cero. Mientras no se ingrese un valor positivo, el algoritmo debe generar el mensaje “Error, valor mal ingresado”.

while True:
    numero = int(input("Ingrese un número entero (el programa termina al ingresar un número positivo): "))
    if numero > 0:
        print("Número ingresado:", numero)
        break
    else:
        print("Error, valor mal ingresado")
        
#Problema 6.

#Construya un programa usando lenguaje de programación Python que lea y valide el valor de un número entero mayor que cero y que calcule y despliegue la suma de todos los enteros entre 1 y el número ingresado.

while True:
    numero = int(input("Ingrese un número entero mayor que cero: "))
    if numero > 0:
        suma = sum(range(1, numero + 1))
        print("La suma de todos los enteros entre 1 y", numero, "es:", suma)
        break
    else:
        print("Error, valor mal ingresado. Intente nuevamente.")

#Problema 7.

#En un almacén se hace un 10 % de descuento a los clientes cuya compra supere los $100000. Construya un programa Python que, dado el valor de un conjunto de productos, determine cuál será la cantidad que pagará una persona por su compra.

#En un almacén se hace un 10 % de descuento a los clientes cuya compra supere los $100000. Construya un programa Python que, dado el valor de un conjunto de productos, determine cuál será la cantidad que pagará una persona por su compra.

while True:
    cantidad_productos = int(input("Ingrese la cantidad de productos: "))
    for i in range(cantidad_productos):
        precio_producto = int(input("Ingrese el precio del producto: "))
        if precio_producto < 0:
            print("Error, valor mal ingresado. Intente nuevamente.")
        else:
            if precio_producto > 100000:
                descuento = precio_producto * 0.10
                precio_final = precio_producto - descuento
                print("El precio final del producto con descuento es:", precio_final)
            else:
                print("El precio del producto sin descuento es:", precio_producto)
    break
