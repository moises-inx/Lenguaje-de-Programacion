# Problema 1 

numero= int(input("Ingrese un número entero: "))

def capicula(numero):
    # Convertir el número a una cadena, para poder invertirlo y evaluar si es copicúa o no.
    numero_str = str(numero)
    
    # Verificar si la cadena es igual a su reverso
    return numero_str == numero_str[::-1]
        # El comando [::-1] invierte la cadena y == evalua si el número es igual a su inversa.

while True:
    if numero < 10 or numero > 10**10:
        print("Error, número fuera de rango.")
        numero = int(input("Ingrese un número entero: "))
    else: 
        if capicula(numero):
            print(f"El número {numero} es capicúa.")
        else:
            print(f"El número {numero} no es capicúa.")
        break
    
# Problema 2

#Forma 1
while True: 
    pelotas_producidas_diario = int(input("Ingrese la cantidad de pelotas producidas hoy: "))
    tamaños = []
    if pelotas_producidas_diario < 1 or pelotas_producidas_diario >= 1000: 
        print("Error, número fuera de rango.")
    else:
        for i in range(pelotas_producidas_diario):
            tamaño = int(input(f"Ingrese el radio de la pelota {i+1}: "))
            while tamaño < 0 or tamaño >= 100:
                print("Error, número fuera de rango.")
                tamaño = int(input(f"Ingrese el radio de la pelota {i+1}: "))
            else:
                tamaños.append(tamaño)
                    #El comando append agrega el tamaño de la pelota a la lista tamaños.
        # Calcular el tamaño más pequeño y su frecuencia
        tamaño_mas_pequeño = min(tamaños)
        frecuencia = tamaños.count(tamaño_mas_pequeño)
        # Mostrar el resultado
        print(f"Se han producido {frecuencia} pelotas de radio {tamaño_mas_pequeño} hoy.")
        break
    
#Forma 2
def pelotas():
    while True: 
        pelotas_producidas_diario = int(input("Ingrese la cantidad de pelotas producidas hoy: "))
        tamaños = []
        if pelotas_producidas_diario < 1 or pelotas_producidas_diario >= 1000: 
            print("Error, número fuera de rango.")
        else:
            for i in range(pelotas_producidas_diario):
                tamaño = int(input(f"Ingrese el radio de la pelota {i+1}: "))
                while tamaño < 0 or tamaño >= 100:
                    print("Error, número fuera de rango.")
                    tamaño = int(input(f"Ingrese el radio de la pelota {i+1}: "))
                else:
                    tamaños.append(tamaño)
                        #El comando append agrega el tamaño de la pelota a la lista tamaños.
            # Calcular el tamaño más pequeño y su frecuencia
            tamaño_mas_pequeño = min(tamaños)
            frecuencia = tamaños.count(tamaño_mas_pequeño)
            # Mostrar el resultado
            print(f"Se han producido {frecuencia} pelotas de radio {tamaño_mas_pequeño} hoy.")
            break        
pelotas()

# Problema 3

autos = 0
while True:
    try:
        autos_por_minutos = int(input("Ingrese la cantidad de autos que pueden cruzar a PROGRAMALANDIA en un minuto: "))
        tiempo_de_observación = int(input("Ingrese la cantidad de minutos transcurridos desde el comienzo de la observación: "))
        if autos_por_minutos <= 0 or tiempo_de_observación <= 0:
            print("Error, número fuera de rango.")
            continue
        else:
            break
    except ValueError:
        print("Error, ingrese un número entero positivo.")
for i in range(tiempo_de_observación):
    while True:
        try:
            autos_en_el_cruce = int(input(f"Ingrese la cantidad de autos que se acercaron al cruce durante el minuto {i+1}: "))
            if autos_en_el_cruce < 0:
                print("Error, número fuera de rango.")
                continue
            else:
                break
        except ValueError:
            print("Error, ingrese un número entero positivo.")
    autos += autos_en_el_cruce - autos_por_minutos
    if autos < 0:
        autos = 0
print(f"La cantidad de autos que se encuentran actualmente en la congestión de ingreso al parque es: {autos}")

#Forma 2

def autos():
    autos = 0
    while True:
        try:
            autos_por_minutos = int(input("Ingrese la cantidad de autos que pueden cruzar a PROGRAMALANDIA en un minuto: "))
            tiempo_de_observación = int(input("Ingrese la cantidad de minutos transcurridos desde el comienzo de la observación: "))
            if autos_por_minutos <= 0 or tiempo_de_observación <= 0:
                print("Error, número fuera de rango.")
                continue
            else:
                break
        except ValueError:
            print("Error, ingrese un número entero positivo.")
    for i in range(tiempo_de_observación):
        while True:
            try:
                autos_en_el_cruce = int(input(f"Ingrese la cantidad de autos que se acercaron al cruce durante el minuto {i+1}: "))
                if autos_en_el_cruce < 0:
                    print("Error, número fuera de rango.")
                    continue
                else:
                    break
            except ValueError:
                print("Error, ingrese un número entero positivo.")
        autos += autos_en_el_cruce - autos_por_minutos
        if autos < 0:
            autos = 0
    print(f"La cantidad de autos que se encuentran actualmente en la congestión de ingreso al parque es: {autos}")
autos()