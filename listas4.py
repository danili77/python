# ordenar listas

comida = ["patata","huevo","jamon","queso"]

comida.sort() # Ordena alfanumericamente

print(comida)



numeros = [100,50,65,82,23]

numeros.sort()
numeros.sort(reverse= True) # ordenar de forma descendente

print(numeros)



frutas = ["naranja","mango","kiwi","piña","platano"]

frutas.sort(reverse= True) # ordenar de forma descendente

print(frutas)


# ordena la lista segun lo cerca que este el numero de 50

def mifuncion(n):
    return abs(n-50)

numeros.sort(key = mifuncion)
print(numeros)


# invertir el orden de una listas

frutas.reverse()
print(frutas)


# copiar una lista

nueva = frutas.copy()
print(nueva)

nueva2 = list(frutas) # Otra forma de copiar una lista
print(nueva2)
