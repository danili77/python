a = ",me gustan las manzanas,manzana es mi fruta favorita."
b = "\u0030" # esto en unicode es 0
c = "220"
d = "miCasa"
e = "      "
f = "   Me Gustan Las Naranjas"

fila = ("John","Nieve","Mola")

print(a.upper()) # Devuelve la cadena en mayusculas

print(a.isupper()) # Comprueba si todos los caracteres de la cadena estan en mayusculas.

print(a.lower()) # Devuelve la cadena en minusculas

print(a.islower()) # Comprueba si todos los caracteres del String son minusculas.

print(a.strip()) # Elimina cualquier espacio en blanco antes o despues del texto

print(a.replace("h","j")) # Reemplaza una cadena por otra

print(a.split(",")) # Devuelve una lista de elementos,lo que se especifica entre comillas es el elemento separador

print(a.capitalize()) # Convierte el primer caracter en mayusculas

print(a.casefold()) # Convierte la cadena a minusculas

print(a.center(20,"o")) # Devuelve una cadena centrado, se le pasa por parametro los espacios que va a ocupar y el caracter de relleno

print(a.count("manzana",0,22)) # Parametros-->valor a contar,posicion de inicio y posicion de fin.

print(a.encode()) # Devuelve una version codificada del string

print(a.startswith(",")) # Devuelve true si la cadena comienza con el valor especificado por parametro.

print(a.endswith(".")) # Devuelve true si la cadena termina con el valor especificado por parametro.

print(a.expandtabs(2)) # Establece el tamaño del tabulador especificado por parametro.

print(a.find("es")) # Busca la cadena especificada por parametro y devuelve la posicion donde se encontro.

print(a.index("mi")) #Busca la cadena especificada por parametro y retorna la posición donde se encontro

print(a.isalpha()) # Comprueba si todos los caracteres de la cadena son letras

# el metodo format(precio = 49) sirve para formtear una cadena.Vease https://www.w3schools.com/python/ref_string_format.asp

print(b.isdecimal()) #Comprueba que todos los caracteres unicode son decimales.

print(c.isdigit()) #Devuelve True si todos los caracteres son digitos.

print(d.isidentifier()) # Devuelve true si la cadena es un identificador valido

"""
Una cadena se considera un identificador válido si solo contiene letras alfanuméricas (az) y (0-9), o guiones bajos (_).
Un identificador válido no puede comenzar con un número ni contener espacios.
"""

print(c.isnumeric()) # Devuelve true si todos los caracteres de la cadena son numeros

print(d.isprintable()) # Devuelve true si todos los caracteres de la cadena son imprimibles.No imprimibles(\r,\n)

print(e.isspace()) # Devuelve true si todos los caracteres de la cadena son espacios en blanco

print(f.istitle()) # Devuelve True si todas las palabras de la cadena comienzan por mayusculas

print("#".join(fila)) # Une todos los elementos de una fila en una cadena y los separa con un caracter especificado al principio

x= f.ljust(20)
print(x,"y las mandarinas") # Devuelve la version justificada de la cadena f, a la izquierda 20 caracteres

print(f.lstrip()) # quita los espacios en blanco a la izquierda de la cadena

txt = "Podria comer pizza todo el dia"

y = txt.partition("pizza") # busca la cadena especificada y la divide en una fila con 3 elementos

print(y)

print(a.rfind("manzana")) # Devuelve la posicion de la ultima aparicion de la palabra especificada por parametro,-1 si no encuentra nada.

print(a.rindex("manzana")) # Devuelve la posicion de la ultima aparicion de la palabra especificada por parametro,si no encuentra nada genera excepcion.

print(a.zfill(100)) # Rellena la cadena con 0 hasta que tenga 40 caracteres
