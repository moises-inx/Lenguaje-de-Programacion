
### Problema 3

#Cuando un programa Python requiere que se le ingrese un número entero positivo, muchas veces al poner en su entrada:

#n = int(input("Introduce un número entero: "))

#el programa falla cuando por error el usuario digita algún símbolo distinto de un dígito. Por tanto, se pide escriba una función que lea un string y que se asegure que todos los símbolos ingresados son dígitos.

#<ins>**Entradas**:</ins> La  ́unica entrada a la función es una string de símbolos posiblemente lleno con dígitos.

#<ins>**Salidas**:</ins> La salida de la función es True si la cadena de entrada esta compuesta sólo de dígitos y False de lo contrario.

#**Observación**: En el programa principal, si la cadena de entrada esta compuesta por algún símbolo que no es un dígito se debe marcar el error y reingresar la cadena.

def es_digito(cadena):
    """
    Verifica si la cadena de entrada está compuesta solo por dígitos.

    Args:
        cadena (str): La cadena a verificar.

    Returns:
        bool: True si la cadena contiene solo dígitos, False de lo contrario.
    """
    for caracter in cadena:
        if not caracter.isdigit():
            return False
    return True

def main():
    """
    Función principal que solicita al usuario una cadena y verifica si contiene solo dígitos.
    """
    while True:
        cadena = input("Introduce una cadena: ")
        if es_digito(cadena):
            print("La cadena contiene solo dígitos.")
            break
        else:
            print("Error: La cadena contiene símbolos no válidos. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
# En este código, la función `es_digito` verifica si todos los caracteres de la cadena son dígitos.