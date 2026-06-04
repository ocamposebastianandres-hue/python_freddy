# Código para ilustrar la relación de COMPOSICIÓN entre clases.
# .venv activate
# .venv deactivate
class Aula:
    
    def __init__(self, codigo, capacidad):
        self.codigo = codigo
        self.capacidad = capacidad
        print(f"Aula {self.codigo} creada.")
        
    def mostrar_info(self):
        print(f"Aula: {self.codigo} - Capacidad: {self.capacidad}")
        
    def __del__(self):
        print(f"Aula {self.codigo} eliminada.")


class Escuela:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
        # La escuela crea sus propias aulas
        self.aulas = [
            Aula("A101", 30),
            Aula("A102", 25),
            Aula("LAB01", 20)
        ]

        print(f"Escuela {self.nombre} creada.")
    def mostrar_aulas(self):