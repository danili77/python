tuplanueva = ("manzana","platano","cereza","manzana")

for x in tuplanueva:
    print(x)


# recorrer una tupla consultando su numero de indice
for i in range(len(tuplanueva)):
    print(tuplanueva[i])


while i < len(tuplanueva):
    print(tuplanueva[i])
    i = i + 1

# Unir dos tuplas

tupla1 = ("a","b","c")
tupla2 = (1,2,3)

tupla3 = tupla1 + tupla2

print(tupla3)

# Multiplicar tuplas(multiplica el contenido de las tuplas)

mitupla = tupla1 * 2
print(mitupla)

# metodos de tuplas

tupla4 = (1,2,3,4,5,9,1,2)
x = tupla4.count(1)            # Devuelve el numero de veces que aparece un valor en la tupla

print(x)

y = tupla4.index(9)            # Busca la primera aparicion de un valor especificado, sino encuentra el valor se genera unna excepcion
print(y)
