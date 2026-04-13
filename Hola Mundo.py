print ("Hola Mundo")
# 2. Imprime "Hola, Leandro" con el nombre en una variable
nombre = "Leandro"
print("Hola," , nombre) # con una coma
print( "Hola, " + nombre ) # con un +

# 3. Imprimir "Hola 11!" con el número en una variable
numero = 11
print("Hola", numero, "!") # con una coma
print("Hola" + str(numero) + "!" ) # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer milanesas y papas fritas" con las comidas en variables
comida1 = "milanesas"
comida2 = " papas fritas"
print( "me encanta comer {0} y {1}".format(comida1, comida2) ) # con .format()
print( f"me encanta comer {comida1} y {comida2}" ) # con una cadena f

# Lista de temperaturas diarias
temperaturas = [22.5, 21.0, 23.3, 25.2, 24.5]
media_temperatura = sum(temperaturas) / len(temperaturas)
print("Temperatura media:", media_temperatura)

# Coordenadas geográficas de una ubicación
coordenadas = (19.4326, -99.1332)  # Latitud y longitud de Ciudad de México

def calcular_distancia(coord1, coord2):
    # Implementación ficticia para calcular la distancia
    distancia = 10  # Solo un valor de ejemplo
    return distancia

distancia = calcular_distancia(coordenadas, (34.0522, -118.2437))
print("Distancia:", distancia)

# Diccionario con información sobre un conjunto de datos
dataset_info = {
    "nombre": "Datos de ventas",
    "columnas": ["fecha", "producto", "cantidad", "precio"],
    "filas": 1000,
    "fuente": "Sistema de ventas interno"
}

print("Nombre del conjunto de datos:", dataset_info["nombre"])
print("Columnas:", dataset_info["columnas"][2]) # Imprime la tercera columna
print("Número de filas:", dataset_info["filas"])