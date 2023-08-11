class Alumnos:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def  nombre(self):
        return self.nombre + self.apellido
    
    


def menu():
    while menu!=3:
        print( "Libro de Alumnos 4°C" )
        print("Ingrese su apellido")
        print("-------------------")
        print("1. Ingresa nombre del estudiante")
        print("2. Ingresa apellido del estudiante")
        print("3. Salir")
        seleccion = int(input("Elige una opcion:"))
        if seleccion == 1:
            registrar( )

        if seleccion == 2:
            registrar()
"""
class Registro:
    def __init__(self,fecha, presencia):
        self.fecha = fecha
        self.presencia = presencia
"""


