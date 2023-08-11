from padre import padre

class hijo(padre):
    def __init__(self , huerfano):
        self.huerfano = huerfano

    def imprimir(self):
        return f"{self.huerfano}"
    