from mascota import mascota
class ninja():
    def __init__( self ,nombre, apellido, premios, comida_mascota, mascota):
        self.nombre =nombre
        self.apellido =apellido
        self.premios =premios
        self.comida_mascota =comida_mascota
        self.mascota =mascota
    def caminar(cls,self):
        self.mascota.jugar()
        return self
    def alimentar():
        pass
    def bañar():
        pass
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()

