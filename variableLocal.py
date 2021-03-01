# La variable creada dentro de la funcion es local solo se puede usar dentro de la funcion.

x = "asombroso"

def myfunc():
    x = "fantastico"
    print("Python es "+x)

myfunc()

print("Python es "+x)
