containerFila=[]
containerFila.append(12)
containerFila.append(13)
containerFila.append(14)

for i in containerFila:
    print(i)

print("after pop")

containerFila.pop(0)
for i in containerFila:
    print(i)