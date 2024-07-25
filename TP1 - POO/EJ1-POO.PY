class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre.lower()
        self.apellido = apellido.lower()
        self.edad = edad
        self.curso = curso.lower()
        
    def programar(self):
        print(f"El alumno {self.nombre} {self.apellido} está programando")
        
alumno = Alumno(input("ingrese su nombre: "), 
                input("ingrese su apellido: "), 
                input("ingrese su edad: "), 
                input("ingrese su curso: "))
print(alumno)
alumno.programar()