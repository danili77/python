# crear un diccionario.No permite duplicados. Pares de atributos clave-valor.

dicc = {
 "marca":"Ford",
 "modelo":"Mustang",
 "año":1964
}

print(dicc)

print(dicc["marca"]) # Acceder a un elemento

dicc.get("marca") # Obtener el valor de la clave marca

print(len(dicc)) # longitud o numero de elementos en el diccionario

print(type(dicc)) # tipo de datos de dicc

x = dicc.keys() # obtiene la lista de las claves

y = dicc.values() # obtiene la lista de los valores

z = dicc.items() # Obtiene la lista de los pares clave:valor

print(x)

print(y)

print(z)

dicc["color"] = "blanco" # Agrega un nuevo elemento

dicc["año"] = 2021 # Cambia el valor

dicc.update({"año":1988}) # Cambia el valor con update

print(dicc)

# comprueba si el modelo esta presente en el diccionario

if "modelo" in dicc:
    print("Si modelo es una de las claves en este diccionario")

# Eliminar elementos
dicc.pop("modelo")
print(dicc)

dicc.popitem() #Elimina el ultimo elemento insertado
print(dicc)

# Otra forma de eliminar
del dicc["marca"]
print(dicc)

dicc.clear() # Metodo que vacia el diccionario
print(dicc)


dicc1 = {
 "marca":"Ford",
 "modelo":"Mustang",
 "año":1964
}

# Recorrer un diccionario sacando los los nombres clave
for x in dicc1:
    print(x)

# Otra forma de devolver las claves

for x in dicc1.keys():
    print(x)

# Saca los valores
for x in dicc1:
    print(dicc1[x])

# Otra forma de devolver los valores
for x in dicc1.values():
    print(x)


# Recorra tanto las claves como los valores
for x,y in dicc1.items():
    print(x,y)
