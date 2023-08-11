from datetime import datetime

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Registro:
    def __init__(self, usuario, tiempo, tipo):
        self.usuario = usuario
        self.tiempo = tiempo
        self.tipo = tipo

class SistemaAsistencia:
    def __init__(self):
        self.usuarios = []
        self.registros = []

    def agregar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        print(f"Se ha agregado al usuario {nombre}.")

    def registrar_entrada(self, nombre):
        usuario = self.buscar_usuario(nombre)
        if usuario:
            tiempo = datetime.now()
            registro = Registro(usuario, tiempo, "entrada")
            self.registros.append(registro)
            print(f"Registro de entrada para {nombre} registrado a las {tiempo}.")
        else:
            print(f"No se encontró al usuario {nombre}.")

    def registrar_salida(self, nombre):
        usuario = self.buscar_usuario(nombre)
        if usuario:
            tiempo = datetime.now()
            registro = Registro(usuario, tiempo, "salida")
            self.registros.append(registro)
            print(f"Registro de salida para {nombre} registrado a las {tiempo}.")
        else:
            print(f"No se encontró al usuario {nombre}.")

    def listar_registros(self):
        for registro in self.registros:
            nombre = registro.usuario.nombre
            tiempo = registro.tiempo
            tipo = registro.tipo
            print(f"Usuario: {nombre} - Tipo: {tipo} - Tiempo: {tiempo}")

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None

def main():
    sistema_asistencia = SistemaAsistencia()

    while True:
        print("\n-- Sistema de Asistencia --")
        print("1. Agregar usuario")
        print("2. Registrar entrada")
        print("3. Registrar salida")
        print("4. Listar registros")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.agregar_usuario(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.registrar_entrada(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.registrar_salida(nombre)
        elif opcion == "4":
            sistema_asistencia.listar_registros()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()