# unir listas

lista1 = ["a","b","c"]
lista2 = [1,2,3]

lista3 = lista1+lista2

print(lista3)

# otra forma de unir es agregando todos los elementos de una lista a otra

for x in lista2:
    lista1.append(x)

print(lista1)

# Otra forma es con el metodo extend()

lista1.extend(lista2)
print(lista1)
