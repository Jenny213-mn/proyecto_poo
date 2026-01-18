# Proyecto POO en Python

Este proyecto demuestra el uso de Programación Orientada a Objetos en Python.
# Autora: Jenny Manzano

## Conceptos aplicados
- Clases y objetos
- Herencia
- Encapsulación
- Polimorfismo
- Organización por carpetas

## 🧠 Descripción de las clases

### 🔹 Persona
Clase base que representa a una persona.
- Usa **atributos privados** (encapsulación)
- Incluye métodos getters
- Tiene un método `presentarse()`

### 🔹 Estudiante
Clase que hereda de `Persona`.
- Agrega el atributo `carrera`
- Sobrescribe el método `presentarse()` (polimorfismo)

### 🔹 GestorPersonas
Clase encargada de:
- Almacenar una lista de personas
- Mostrar la presentación de cada objeto

---

## ▶️ Ejecución del programa

Desde la carpeta raíz del proyecto, ejecutar:
```bash
python main.py
