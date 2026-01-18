# Archivo principal del programa
from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import GestorPersonas

# Crear objetos
persona1 = Persona("Carlos", 40)
estudiante1 = Estudiante("Ana", 20, "Ingeniería en Sistemas")

# Crear gestor
gestor = GestorPersonas()

# Agregar objetos al gestor
gestor.agregar_persona(persona1)
gestor.agregar_persona(estudiante1)

# Demostrar funcionamiento
gestor.mostrar_presentaciones()
