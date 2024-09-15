# Nodo inicial del árbol (vacío)
root = None

# Función para crear un nuevo nodo
def create_node(data):
    return {'data': data, 'left': None, 'right': None}

# Función para insertar un nodo en el árbol binario
def insert(root, data):
    if root is None:
        return create_node(data)
    
    if data < root['data']:
        root['left'] = insert(root['left'], data)
    else:
        root['right'] = insert(root['right'], data)
    
    return root

# Función para mostrar los elementos del árbol en orden (in-order traversal)
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root['left'])
        print(root['data'], end=' ')
        in_order_traversal(root['right'])

# Ejemplo de uso
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

print("Elementos del árbol en orden:")
in_order_traversal(root)  # Muestra: 20 30 40 50 60 70 80
