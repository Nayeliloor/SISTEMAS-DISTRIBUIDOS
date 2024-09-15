container = []

container.Pila.append(1)
container.Pila.append(2)
container.Pila.append(3)

for elem in containerPila:
    print(elem)

aux1=containerPila.pop()

print(f'The last element to be showed {aux1}')

print ("Actualización del contenedor despues de pop")
for elem in containerPila:
    print(elem)

# aux2=containerPila[-1]
# print(f'The las element {aux1}')
