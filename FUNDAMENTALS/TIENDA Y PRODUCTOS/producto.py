class Producto:
    def __init__(self,nombre,precio,categoria):
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria

    def actualizar_precio(self,cambio_porcentaje,esta_elevado):
        self.cambio=cambio_porcentaje
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100

        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def imprimir(self):
        print(f"El nombre del producto es: {self.nombre} y la categoria es: {self.categoria}")

Producto1 = Producto("confort",3000,"higiene")
Producto1.imprimir()