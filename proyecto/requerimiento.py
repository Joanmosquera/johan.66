# Mi primer programa de inventario
# Autor: Principiante

# Guardamos productos en una lista
productos = []

# Función para agregar un producto
def agregar_producto():
    print("AGREGAR PRODUCTO")
    print("--------------")
    nombre = input("Escribe el nombre del producto: ")
    
    # Intentamos convertir a números
    try:
        precio = float(input("Escribe el precio: "))
        cantidad = int(input("Escribe cuántos hay: "))
    except:
        print("Error! Debes escribir números")
        return
    
    # Guardamos el producto como un diccionario
    producto = {}
    producto["nombre"] = nombre
    producto["precio"] = precio
    producto["cantidad"] = cantidad
    
    # Lo agregamos a la lista
    productos.append(producto)
    print("Producto agregado!")
    
    # Guardamos en archivo
    guardar_productos()

# Función para mostrar productos
def mostrar_productos():
    print("LISTA DE PRODUCTOS")
    print("--------------")
    
    if len(productos) == 0:
        print("No hay productos todavía")
        return
    
    for p in productos:
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        print("--------------")

# Guardar en archivo
def guardar_productos():
    import json
    archivo = open("productos.txt", "w")
    json.dump(productos, archivo)
    archivo.close()
    print("Datos guardados!")

# Cargar del archivo
def cargar_productos():
    import json
    import os
    
    # Verificar si existe el archivo
    if os.path.exists("productos.txt"):
        try:
            archivo = open("productos.txt", "r")
            datos = json.load(archivo)
            archivo.close()
            
            # Actualizar la lista de productos
            global productos
            productos = datos
            print(f"Se cargaron {len(productos)} productos")
        except:
            print("Error al leer el archivo")

# Programa principal
print("SISTEMA DE INVENTARIO v1.0")
print("=========================")

# Cargar datos al inicio
cargar_productos()

# Menú principal
while True:
    print("\nMENU:")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")
    
    opcion = input("\nElige una opción (1-3): ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida, intenta de nuevo")