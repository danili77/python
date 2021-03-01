milista = ["raton","teclado","monitor"]

# Para recorrer una lista distintas formas
for x in milista:
    print(x)

# Recorrer una lista por su indice
for i in range(len(milista)):
    print(milista[i])

# con un while
i = 0
while i < len(milista):
    print(milista[i])
    i = i + 1


# usando compresion de listas
[print(x) for x in milista]
