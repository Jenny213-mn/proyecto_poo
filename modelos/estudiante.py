# Clase derivada Estudiante
# Aplica HERENCIA y POLIMORFISMO

from modelos.persona import Persona

# Clase derivada que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: sobrescribe el método presentarse
    def presentarse(self):
        return f"Hola, soy {self.get_nombre()}, estudio {self.carrera} y tengo {self.get_edad()} años."
