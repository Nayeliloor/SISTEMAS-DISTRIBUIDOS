# Nodo inicial vacío
head = None

# Función para agregar un nodo al final de la lista
def append(head, data):
    new_node = {'data': data, 'next': None}
    if head is None:
        return new_node
    else:
        current = head
        while current['next'] is not None:
            current = current['next']
        current['next'] = new_node
    return head

# Función para agregar un nodo al inicio de la lista
def prepend(head, data):
    new_node = {'data': data, 'next': head}
    return new_node

# Función para eliminar un nodo con un valor específico
def delete(head, key):
    if head is None:
        print("La lista está vacía")
        return head
    
    # Si el nodo a eliminar es el primero
    if head['data'] == key:
        return head['next']
    
    current = head
    prev = None
    while current is not None and current['data'] != key:
        prev = current
        current = current['next']
    
    # Si no se encuentra el nodo
    if current is None:
        print("Nodo no encontrado")
        return head

    # Eliminar el nodo
    prev['next'] = current['next']
    return head

# Función para mostrar los elementos de la lista
def display(head):
    elements = []
    current = head
    while current is not None:
        elements.append(current['data'])
        current = current['next']
    print(elements)

# Ejemplo de uso
head = append(head, 10)
head = append(head, 20)
head = prepend(head, 5)
display(head)    # Muestra: [5, 10, 20]
head = delete(head, 10)
display(head)    # Muestra: [5, 20]
