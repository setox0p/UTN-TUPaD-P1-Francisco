# ejercicios_recursivos.py

# Factorial recursivo y mostrar factoriales hasta el número dado
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def ejercicio_1():
    max_num = int(input("Ejercicio 1 - Ingrese un número entero positivo: "))
    for i in range(1, max_num + 1):
        print(f"Factorial de {i} = {factorial(i)}")


# Fibonacci recursivo y mostrar la serie completa hasta la posición indicada
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

def ejercicio_2():
    max_pos = int(input("Ejercicio 2 - Ingrese la posición máxima para la serie Fibonacci: "))
    for i in range(max_pos + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")


#Potencia recursiva: base^exponente
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def ejercicio_3():
    b = int(input("Ejercicio 3 - Base: "))
    e = int(input("Ejercicio 3 - Exponente: "))
    print(f"{b} elevado a {e} es {potencia(b, e)}")


# Conversión recursiva de decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def ejercicio_4():
    num = int(input("Ejercicio 4 - Ingrese un número entero positivo: "))
    resultado = decimal_a_binario(num)
    print(f"Binario: {resultado if resultado != '' else '0'}")


#Verificar palíndromo recursivamente
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def ejercicio_5():
    pal = input("Ejercicio 5 - Ingrese una palabra sin espacios ni tildes: ").lower()
    print(es_palindromo(pal))


#  Suma recursiva de dígitos sin convertir a string
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

def ejercicio_6():
    num = int(input("Ejercicio 6 - Ingrese un número entero positivo: "))
    print(f"Suma de dígitos: {suma_digitos(num)}")


#  Contar bloques para la pirámide
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

def ejercicio_7():
    n = int(input("Ejercicio 7 - Número de bloques en el nivel más bajo: "))
    print(f"Total de bloques para la pirámide: {contar_bloques(n)}")


# Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if (numero % 10) == digito else 0) + contar_digito(numero // 10, digito)

def ejercicio_8():
    numero = int(input("Ejercicio 8 - Ingrese un número entero positivo: "))
    digito = int(input("Ejercicio 8 - Ingrese un dígito (0-9) para contar: "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")


#Menú para ejecutar ejercicios
def menu():
    while True:
        print("\nEjercicios recursivos")
        print("1) Factorial")
        print("2) Fibonacci")
        print("3) Potencia")
        print("4) Decimal a binario")
        print("5) Palíndromo")
        print("6) Suma de dígitos")
        print("7) Contar bloques pirámide")
        print("8) Contar dígito en número")
        print("0) Salir")
        opcion = input("Elija un ejercicio para ejecutar: ")

        if opcion == '1':
            ejercicio_1()
        elif opcion == '2':
            ejercicio_2()
        elif opcion == '3':
            ejercicio_3()
        elif opcion == '4':
            ejercicio_4()
        elif opcion == '5':
            ejercicio_5()
        elif opcion == '6':
            ejercicio_6()
        elif opcion == '7':
            ejercicio_7()
        elif opcion == '8':
            ejercicio_8()
        elif opcion == '0':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
