class Humano:
    def __init__(self):
        print("Soy un nuevo objeto")

    def hablar(self, mensaje):
        print (mensaje)

pedro = Humano()
raul = Humano()

pedro.hablar("Hola!!")
raul.hablar("Hola Pedro!")
