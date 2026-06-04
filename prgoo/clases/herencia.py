# Código para ilustrar la relación de HERENCIA entre clases
# .venv activate
# .venv deactivate
class Persona:
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")


class Profesor(Persona):
    
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self.especialidad = especialidad
        
    def impartir_clase(self):
        print(f"El profesor {self.nombre} está impartiendo {self.especialidad}.")


class Alumno(Persona):
    
    def __init__(self, nombre, email, codigo):
        super().__init__(nombre, email)
        self.codigo = codigo
    
    def estudiar (self):
        print(f"el alumno {self.nombre} está estudiando.")
        