# Función de Búsqueda Lineal
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Devuelve el índice si se encuentra el valor
    return -1  # Devuelve -1 si no se encuentra el valor

# Ejemplo de uso
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)

print("Búsqueda Lineal:")
if result != -1:
    print(f"Elemento {target} encontrado en el índice {result}")
else:
    print(f"Elemento {target} no encontrado")
