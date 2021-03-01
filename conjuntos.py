conjunto = {"manzana","platano","cereza"}
# un conjunto es una coleccion desordenada y no indexada de elementos
# No permite duplicados
print(conjunto)

print(len(conjunto)) # cantidad de elementos de un conjunto

print(type(conjunto)) # para saber el tipo

# hacer un conjunto con set

conjunto2 = set(("pera","piña","sandia"))
print(conjunto2)


# recorrer un conjunto
for x in conjunto:
    print(x)

print("platano" in conjunto) # Comprobar si un elemento esta en el conjunto2

conjunto.add("naranja") # añade un elemento al conjunto2


# Agregar un conjunto a otro
conjunto.update(conjunto2)
print(conjunto)

# Unir dos conjuntos
conjunto3 = conjunto.union(conjunto2)
print(conjunto3)


#Agregar una lista al conjunto
milista = ["kiwi","papaya"]

conjunto.update(milista)

print(conjunto)

# Eliminar un elemento del conjunto(si un elemento no existe se genera un error)

conjunto.remove("platano")

print(conjunto)


# otra forma de quitar un elemento

conjunto.discard("manzana")
print(conjunto)

# Eliminar el ultimo elemento
conjunto.pop()
print(conjunto)

#vacia el conjunto2
conjunto.clear()
print(conjunto)

#elimina el conjunto entero
del conjunto
#print(conjunto)


# conservar solo los elementos duplicados
conjunto4 = {"manzana","platano","cereza"}
conjunto5 = set(("pera","piña","manzana"))
conjunto4.intersection_update(conjunto5) #intersection() --> hace lo mismo

print(conjunto4)

# conservar los elementos no duplicados

conjunto4.symmetric_difference_update(conjunto5)
print(conjunto4)
