# Ejercicio 1

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

else:
    print("Es menor de edad")
    
# Ejercicio 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
    
else:
    print("Reprobado")
    

# Ejercicio 3

num_par = int(input("Ingrese un número par: "))

if num_par % 2 == 0:
     print ("Ha ingresado un número par")

else:
    print("Por favor, ingrese un número par.")
    

# Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es un niño/a.")

elif edad >= 12 and edad < 18:
    print("Es un adolescente.")

elif edad >= 18 and edad < 30:
    print("Es un adulto/a joven")

else:
    print("Es un adulto/a mayor")
    
    
# Ejercicio 5

contras = input("Ingresa una contraseña de entre 8 y 14 caracteres: ")


if len(contras) >= 8 and len(contras) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6


import random
num_aleat = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean




mod = mode(num_aleat)
print("La moda es ", mod)
med = median(num_aleat)
print("La mediana es ", med)
mea = mean(num_aleat)
print("La media es ", mea)


if mean(num_aleat) > median(num_aleat) > mode(num_aleat):
    print("Sesgo positivo")
    
elif mean(num_aleat) < median(num_aleat) < mode(num_aleat):
    print("Sesgo negativo")
    
else:
    print("No hay sesgo")
    

# Ejercicio 7

frase = str(input("Ingrese una frase o palabra: "))

ult_let = frase[len(frase) - 1]


if ult_let == "a" or ult_let == "e" or ult_let == "i" or ult_let == "o" or ult_let == "u":
     print(f"{frase}!")
     
else:
    print(frase)
    
    
# Ejercicio 8

nomb = str(input("Ingrese su nombre: "))
opc = int(input("Ingrse la opción que desee (1, 2 o 3): "))

if opc == 1:
    print(nomb.upper())
    
elif opc == 2:
    print(nomb.lower())
    
else:
    print(nomb.title())
    
    
# Ejercicio 9

magn = int(input("Ingrese la magnitud del terremoto: "))

if magn < 3:
    print("El terremoto es muy leve")
    
elif magn >= 3 and magn < 4:
    print("El terremoto es leve")
    
elif magn >= 4 and magn < 5:
    print("El terremoto es moderado")
    
elif magn >= 5 and magn < 6:
    print("El terremoto es fuerte")
    
elif magn >= 6 and magn < 7:
    print("El terremoto es muy fuerte")
    
else:
    print("El terremoto es extremadamente fuerte")
    
    
# Ejercicio 10

hemis = input("Ingrese su hemisferio (N/S): ")

mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día del mes es?: "))

# Convierto mes y día en una sola fecha

fecha = mes * 100 + dia


def ver_estacion(hemis, fecha):
    if hemis == "N" or hemis == "n":
        if 1221 <= fecha <= 320:
            return "Invierno"
        elif 321 <= fecha <= 620:
            return "Primavera"
        elif 621 <= fecha <= 920:
            return "Verano"
        elif 921 <= fecha <= 1220:
            return "Otoño"
        else:  
            return "Invierno"
    elif hemis == "S" or hemis == "s":
        if 1221 <= fecha <= 320:
            return "Verano"
        elif 321 <= fecha <= 620:
            return "Otoño"
        elif 621 <= fecha <= 920:
            return "Invierno"
        elif 921 <= fecha <= 1220:
            return "Primavera"
        else:
            return "Verano"
    else:
        return "Hemisferio inválido"
    
    
estacion = ver_estacion(hemis, fecha)
print(f"Estas en {estacion}.")