class Persona:
    def __init__(self, nombre, edad): # para crear un nuevo objeto
        self.nombre = nombre
        self.edad  = edad

    def  mifunc(self):
        print("Hola mi nombre es "+self.nombre)

p1 = Persona("Dani",32)
p1.mifunc()

print(p1.nombre)
print(p1.edad)

p1.edad = 40 # Modificar propiedades
print(p1.edad)

del p1.edad # Elimina la propiedad edad del objeto p1

del p1  # Elimina el objeto p1
