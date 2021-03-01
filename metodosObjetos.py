class Persona:
    def __init__(self, nombre, edad): # para crear un nuevo objeto
        self.nombre = nombre
        self.edad  = edad

    def mifuncion(self):
        print("Hola mi nombre es "+self.nombre)

p1 = Persona("Dani",32)

p1.mifuncion()

p1.age = 40  # modificar una propiedad

del p1 # elimina p1
