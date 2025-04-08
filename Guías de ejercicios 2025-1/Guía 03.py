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
    
