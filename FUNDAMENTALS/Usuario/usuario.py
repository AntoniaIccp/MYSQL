class Usuario:
    def __init__(self):
        self.balance = 0

    def hacer_depósito(self, amount):
        self.balance += amount
        return self

    def hacer_retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"Balance actual: {self.balance}")
        return self


guido = Usuario()
guido.hacer_depósito(100).hacer_depósito(200).hacer_depósito(300).hacer_retiro(50).mostrar_balance_usuario()