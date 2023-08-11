# declarar una clase y darle nombre al usuario
class Usuario :
    def __init__(self) :
        self.name = "Michael"
        self.email = "michael@codingdojo.como"
        self.balance_cuenta = 0


Usuario()
guido = Usuario()
monty = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name    #salida: Michael
print(monty.name)   #salida: Michael