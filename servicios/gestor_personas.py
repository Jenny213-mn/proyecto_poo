# Clase de servicio
# Maneja la lógica del sistema

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def mostrar_presentaciones(self):
        for persona in self.personas:
            # Polimorfismo: se llama al método correspondiente según el objeto
            print(persona.presentarse())
