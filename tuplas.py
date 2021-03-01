# Una tupla es una colección ordenada y no puede cambiar.Se escribe entre parentesis.Permiten valores duplicados.
# Y elementos de distinto tipo.

tupla = ("manzana","platano","cereza","manzana")

print(tupla)

print(len(tupla)) # longitud de una tupla


tupla2 = ("manzana",) # crear una tupla de un solo elemento
print(tupla2)


# Crear una tupla usando el contructor

tupla3 = tuple(("manzana","platano","cereza"))
print(tupla3)


# Acceder a elementos de una tupla

print(tupla3[1])
print(tupla3[-1])
print(tupla3[1:3])
print(tupla3[:2])
print(tupla3[1:])

# comprueba si "manzana esta presente en una tupla"

if "manzana" in tupla3:
    print("Si 'manzana' esta en la tupla de frutas")


# Cambiar valores de una tupla

x = ("manzana","platano","cereza","manzana")

y = list(x)
y[1] ="kiwi"
x = tuple(y)

print(x)

# agregar elementos.Hay que convertir la tupla en lista.

z = list(x)
z.append("naranja")
x = tuple(z)
print(x)


# Eliminar una tupla
b = list(x)
b.remove("manzana")
x = tuple(b)
print(x)

#del x  # Elimina la tupla completa


# desempaquetando una tupla

tuplanueva = ("manzana","platano","cereza","manzana")

(red,purple,green,yellow) = tuplanueva

print(red)
print(purple)
print(green)
print(yellow)

(red,purple,*green) = tuplanueva # Asigna el resto de valores de la tupla a una lista llamada green
print(red)
print(purple)
