matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
matriz[0][1]=6 # Imprime el número 6
cantantes[0]["nombre"] = "Enrique Martin Morales" # Cambia el nombre del primer cantante a "Enrique Martin Morales"
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431 # Cambia la latitud a 9.9355431

def iterarDiccionario(lista):
    for diccionario in lista:
        # Extraemos los valores usando las llaves 'nombre' y 'pais'
        nombre = diccionario["nombre"]
        pais = diccionario["pais"]
        
        print(f"nombre - {nombre}, pais - {pais}")

# Definimos la lista de cantantes (la que tenés en la imagen)
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamamos a la función
iterarDiccionario(cantantes)

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        # Usamos la variable 'llave' para acceder al valor
        if llave in diccionario:
            print(diccionario[llave])

# La lista de cantantes para probar
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Pruebas según los ejemplos de la imagen
print("Valores para 'nombre':")
iterarDiccionario2("nombre", cantantes)

print("\nValores para 'pais':")
iterarDiccionario2("pais", cantantes)

def imprimirInformacion(diccionario):
    for llave in diccionario:
        lista_elementos = diccionario[llave]
        
        print(f"\n{len(lista_elementos)} {llave.upper()}")
        
        # Recorremos la lista para imprimir cada elemento
        for elemento in lista_elementos:
            print(elemento)

# Diccionario de prueba según la imagen
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# Llamada a la función
imprimirInformacion(costa_rica)