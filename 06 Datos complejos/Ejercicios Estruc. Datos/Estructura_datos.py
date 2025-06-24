# manejo de diccionario de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precio frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# actualizo precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# lista de frutas
solo_frutas = list(precios_frutas.keys())
print("Frutas disponibles:", solo_frutas)

# agenda telef.
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre que desea consultar: ")
if consulta in agenda:
    print("Número:", agenda[consulta])
else:
    print("Contacto no encontrado.")

#  set y conteo de palabras
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", conteo_palabras)

# promedio
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese nota {j+1} para {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

# set de estudiantes
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# control de stock
stock = {"pan": 10, "leche": 5}
producto = input("Ingrese el nombre del producto: ")
if producto in stock:
    unidades = int(input("Cuántas unidades agregar?: "))
    stock[producto] += unidades
else:
    nuevo_stock = int(input("Producto nuevo. ¿Cuántas unidades tiene?: "))
    stock[producto] = nuevo_stock
print("Stock actualizado:", stock)

# agenda con tupla (día, hora)
agenda_eventos = {("lunes", "10:00"): "Clase", ("martes", "14:00"): "Reunión"}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
evento = agenda_eventos.get((dia, hora), "No hay actividad registrada.")
print("Actividad:", evento)

# invertir diccionario de paises y capitales
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago"
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:", capitales_paises)
