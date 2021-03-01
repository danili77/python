milista = ["manzana","banana","cereza"]

print(milista)

print(len(milista)) # longitud de una lista

print(type(milista)) # tipos de datos de una lista. --> da un objeto de tipos de datos lista.

# Utilizando el constructor list() para hacer una milista

milista2  = list(("manzana","pero","uva"))

print(milista2)

print(milista2[1])  # nos muestra el segundo elemento de la milista

print(milista2[-1])  # Empieza por el final de la lista -1 ultimo elemento,-2 penultimo elemento

print(milista2[1:3]) # devuelve una nueva lista con los valores especificados en el rango, el ultimo valor no se incluye

print(milista2[:3]) # Al omitir el valor inicial comenzara desde el primer elementos

print(milista2[1:]) # Al omitir el valor final el rango continuara hasta el final de la milista

print(milista2[-3:-1]) # Se empieza por detras y el segundo parametro no se incluye

# comprobar si un elemento esta en una lista
if "manzana" in milista2:
    print("Si 'manzana' esta en la lista de frutas")

milista2[1] = "sandia"  # Cambia el valor de la posicion 2 de la lista

print(milista2)

milista2[1:3] = ["mango","pera"] # Cambia un rango de valores

print(milista2)

# insertar un valor en una lista con el metodo insert(indice,elemento a insertar)

milista2.insert(2,"sandia")
print(milista2)
