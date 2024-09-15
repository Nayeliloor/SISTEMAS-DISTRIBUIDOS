# Función de Búsqueda Binaria
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Encuentra el punto medio

        # Verifica si el elemento objetivo está en el medio
        if arr[mid] == target:
            return mid
        # Si el objetivo es menor, ignora la mitad derecha
        elif arr[mid] > target:
            right = mid - 1
        # Si el objetivo es mayor, ignora la mitad izquierda
        else:
            left = mid + 1

    return -1  # Devuelve -1 si no se encuentra el valor

# Ejemplo de uso
arr_sorted = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr_sorted, target)

print("\nBúsqueda Binaria:")
if result != -1:
    print(f"Elemento {target} encontrado en el índice {result}")
else:
    print(f"Elemento {target} no encontrado")
