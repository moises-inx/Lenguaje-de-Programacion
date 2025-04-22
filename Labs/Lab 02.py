#Problema 1

while True:
    notas = float(input("Ingrese sus notas: "))
    if notas < 1.0 or notas > 7.0:
        print("Nota fuera de rango. Por favor, ingrese una nota entre 1.0 y 7.0.")
        continue
    certamen1 = float(input("Ingrese la nota del primer certamen: "))
    certamen2 = float(input("Ingrese la nota del segundo certamen: "))
    certamen3 = float(input("Ingrese la nota del tercer certamen: "))
    tarea = float(input("Ingrese la nota de la tarea semestral: "))
    autoevaluacion = float(input("Ingrese la nota de la autoevaluación: "))
    desempeño = float(input("Ingrese la nota de desempeño: "))

    if not (1.0 <= certamen1 <= 7.0 and 1.0 <= certamen2 <= 7.0 and 1.0 <= certamen3 <= 7.0 and
            1.0 <= tarea <= 7.0 and 1.0 <= autoevaluacion <= 7.0 and 1.0 <= desempeño <= 7.0):
        print("Una o más notas están fuera de rango. Por favor, ingrese notas entre 1.0 y 7.0.")
        continue

    promedio_certamenes = (certamen1 * 0.25) + (certamen2 * 0.35) + (certamen3 * 0.40)
    nota_final = (promedio_certamenes * 0.50) + (tarea * 0.40) + (autoevaluacion * 0.04) + (desempeño * 0.06)

    print(f"Promedio de certámenes: {promedio_certamenes:.2f}")
    print(f"Nota final: {nota_final:.2f}")

    if nota_final >= 4.0:
        print("APROBADO")
    else:
        print("REPROBADO")
    break

#Problema 2

while True:
    notas = float(input("Ingrese sus notas: "))
    if notas < 1.0 or notas > 7.0:
        print("Nota fuera de rango. Por favor, ingrese una nota entre 1.0 y 7.0.")
        continue
    certamen1 = float(input("Ingrese la nota del primer certamen: "))
    certamen2 = float(input("Ingrese la nota del segundo certamen: "))
    certamen3 = float(input("Ingrese la nota del tercer certamen: "))
    tarea = float(input("Ingrese la nota de la tarea semestral: "))
    autoevaluacion = float(input("Ingrese la nota de la autoevaluación: "))
    desempeño = float(input("Ingrese la nota de desempeño: "))

    if not (1.0 <= certamen1 <= 7.0 and 1.0 <= certamen2 <= 7.0 and 1.0 <= certamen3 <= 7.0 and
            1.0 <= tarea <= 7.0 and 1.0 <= autoevaluacion <= 7.0 and 1.0 <= desempeño <= 7.0):
        print("Una o más notas están fuera de rango. Por favor, ingrese notas entre 1.0 y 7.0.")
        continue
    elif tarea <=1.0:
        promedio_certamenes = (certamen1 * 0.25) + (certamen2 * 0.35) + (certamen3 * 0.40)
        print(f"Promedio de certámenes: {promedio_certamenes:.2f}")
        print("NCR")
        break
    else:
        promedio_certamenes = (certamen1 * 0.25) + (certamen2 * 0.35) + (certamen3 * 0.40)
        nota_final = (promedio_certamenes * 0.50) + (tarea * 0.40) + (autoevaluacion * 0.04) + (desempeño * 0.06)
        print(f"Promedio de certámenes: {promedio_certamenes:.2f}")
        print(f"Nota final: {nota_final:.2f}")
    if nota_final >= 4.0:
        print("APROBADO")
    else:
        print("REPROBADO")
    break

#Problema 3

salario = float(input("Ingrese el salario del empleado: "))

if salario >= 1000000:
    nuevo_salario = salario
    print("El nuevo salario es: $", nuevo_salario)
elif salario >= 500000 and salario < 1000000:
    nuevo_salario = salario * 1.05
    print("El nuevo salario es: $", nuevo_salario)
else:
    nuevo_salario = salario * 1.10
    print("El nuevo salario es: $", nuevo_salario)
    
# Problema 4

def determinar_territorio(N, M, X, Y):
    if X == N or Y == M:
        return "Frontera"
    elif X < N and Y > M:
        return "Nlogonia Noroccidental"
    elif X > N and Y > M:
        return "Nlogonia Nororiental"
    elif X > N and Y < M:
        return "Nlogonia Sudoriental"
    elif X < N and Y < M:
        return "Nlogonia Sudoccidental"

def main():
    # Entrada
    N, M = map(int, input("Ingrese puntos de división, separados con un espacio: ").split())  # Punto de división
    X, Y = map(int, input("Ingrese puntos de recidencia, separados con un espacio: ").split())  # Residencia

    # Salida
    resultado = determinar_territorio(N, M, X, Y)
    print(resultado)

if __name__ == "__main__":
    main()

# Problema 5

def validacion():
    while True:
        try:
            vehiculos = int(input("Ingrese la cantidad de vehículos que cruzan el pórtico (entre 1 y 1000): "))
            if 1 <= vehiculos <= 1000:
                return vehiculos
            else:
                print("Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def tiempo_vehiculo():
    while True:
        try:
            tiempo = int(input("Ingrese el tiempo de cruce (entre 1 y 10 segundos): "))
            if 1 <= tiempo <= 10:
                return tiempo
            else:
                print("Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def velocidad_vehiculo():
    while True:
        try:
            velocidad = int(input("Ingrese la velocidad de cruce (entre 1 y 14 m/s): "))
            if 1 <= velocidad <= 14:
                return velocidad
            else:
                print("Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

for i in range(validacion()):
    tiempo = tiempo_vehiculo()
    velocidad = velocidad_vehiculo()
    longitud = velocidad * tiempo
    print(f"La longitud del vehículo es: {longitud} metros")
    recaudacion = longitud * 2
    print(f"La recaudación por este vehículo es: ${recaudacion}")