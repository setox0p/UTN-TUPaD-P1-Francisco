# Ejercicio 1

cont = 0
while cont <= 100:
    print(cont)
    cont = cont + 1


# Ejercicio 2

num_ent = input("Ingrese un nro. entero: ")

print(len(num_ent))


# Ejercicio 3

valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor: "))

if valor_1 > valor_2:
    valor_1, valor_2 = valor_2, valor_1


suma = 0
for i in range(valor_1 + 1, valor_2):
    suma += i
    
print("la suma entre", valor_1, "y", valor_2, "es", suma)



# Ejercicio 4

cant_numeros = 3
sum = 0

for cont in range(1,cant_numeros + 1):
    print("ingrese un numero", cont)
    num = int(input())
    sum = sum + num
    
print("El resultado es ", sum)



# Ejercicio 5

import random

nro_az = random.randint(0,9)

intentos = 0


while True:
    adiv = int(input("Adivina el nro: "))
    intentos += 1
    
    if adiv == nro_az:
        print(f"Correcto, el nro es {nro_az}, lo conseguiste en {intentos} intentos")
        break
    else:
        print("Casi, seguí intentando.")


# Ejercicio 6

cont = 100
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)



# Ejercicio 7

num_us = int(input("ingrese un numero para calcular la suma: "))
suma = 0


for i in range(num_us + 1):
    suma += i

print(f"El resultado es {suma}")