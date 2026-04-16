# 1. Carga de Datos
# Creamos una lista con datos de prueba para poder hacer los cálculos.
ventas = [
    {"fecha": "2024-01-01", "producto": "Notebook", "cantidad": 2, "precio": 500.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-02", "producto": "Notebook", "cantidad": 1, "precio": 500.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0}
]

# 2. Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    # Si el producto ya está en el diccionario, le sumamos la cantidad
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += cantidad


# Identificamos cuál fue el más vendido
producto_mas_vendido = ""
max_cantidad = 0
for producto, cantidad in ventas_por_producto.items():
    if cantidad > max_cantidad:
        max_cantidad = cantidad
        producto_mas_vendido = producto

# 4. Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]
    
    if producto in precios_por_producto:
        # Recuperamos la tupla anterior y le sumamos los nuevos valores
        suma_ingresos, cant_total = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_ingresos + ingreso_venta, cant_total + cantidad)
    else:
        # Guardamos la tupla por primera vez: (ingresos_de_este_producto, cantidad)
        precios_por_producto[producto] = (ingreso_venta, cantidad)
precio_promedio_por_producto = {}
for producto, datos in precios_por_producto.items():
    suma_ingresos, cant_total = datos  
    precio_promedio_por_producto[producto] = suma_ingresos / cant_total

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso_venta
    else:
        ingresos_por_dia[fecha] = ingreso_venta

# 6. Representación de Datos
resumen_ventas = {}
for producto in ventas_por_producto.keys():
    # Buscamos el promedio en el diccionario que creamos en el paso 4
    # En lugar de usar la variable suelta 'precio_promedio', usamos el diccionario:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precio_promedio_por_producto[producto] # <--- Cambia esto
    }
# IMPRESIÓN DE RESULTADOS 
print("--- ANÁLISIS DE VENTAS ---")
print(f"1. Lista de ventas original:\n{ventas}\n")
print(f"2. Ingresos totales generados: ${ingresos_totales}\n")
print(f"3. Producto más vendido: '{producto_mas_vendido}' con {max_cantidad} unidades.\n")

print("4. Precio promedio de venta por producto:")
for producto, datos in resumen_ventas.items():
    print(f"   - {producto}: ${datos['precio_promedio']:.2f}")

print("\n5. Ingresos totales por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"   - {fecha}: ${ingreso:.2f}")

print(f"\n6. Resumen de ventas por producto:\n{resumen_ventas}")