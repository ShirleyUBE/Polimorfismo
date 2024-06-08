class Animal:
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

def hacer_hablar(animal):
    print(animal.hablar())

# Crear instancias de las clases
perro = Perro()
gato = Gato()

# Llamar a la función hacer_hablar con diferentes objetos
hacer_hablar(perro)  # Salida: Guau
hacer_hablar(gato)   # Salida: Miau
