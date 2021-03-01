milista = ["raton","teclado","monitor"]
milista.append("torre") # Para agregar un elemento a una lista
print(milista)


milista.insert(1,"tarjeta wifi") # inserta un elemnento en el indice indicado (se comienza en el indice 0)
print(milista)


milista2 = ["fuente de alimentacion","memoria ram","procesador"]
milista.extend(milista2) # agrega todos los elementos de una lista  a otra.(no tiene que ser una lista, puede ser una tupla,conjunto,diccionario)
print(milista)


milista.remove("tarjeta wifi") # Elimina el elemento especificado
print(milista)

milista.pop(1) # Elimina el elemento del indice especificado, sino se pone indice elimina el ultimo elemento.
print(milista)

del milista[0] # otra forma de eliminar un elemento de una lista con la palabra clave 'del'
print(milista)

#del milista
# elimina la lista completa

milista.clear() # vacia la lista
print(milista)
