class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def imprimirnombre(self):
        print(self.nombre,self.apellido)

x = Persona("Daniel","Lorenzo")
x.imprimirnombre()

class Estudiante(Persona):
    def __init__(self,nombre,apellido,anio):
        super().__init__(nombre,apellido) # hereda los metodos y propiedades de su padre
        self.aniograduacion = anio # Se agrega una nueva propiedad.

    def bienvenido(self):
        print("Welcome",self.nombre,self.apellido, "de la clase de ",self.aniograduacion)

y = Estudiante("Kevin","Mcain",2021)
#print(y.aniograduacion)
y.bienvenido()
