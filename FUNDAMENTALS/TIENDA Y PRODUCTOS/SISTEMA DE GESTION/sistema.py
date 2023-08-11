class Usuario:
    def __init__ (self, titulo,autor,ISBN,estado):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.estado = estado

class prestar_libro:
    def __init__(self, nombre, libro, tiempo):
        self.nombre = nombre
        self.libro = libro
        self.tiempo = tiempo
    for registro in self.registros:
            nombre = registro.usuario.nombre
            tiempo = registro.tiempo
            tipo = registro.tipo
            print(f"Usuario: {nombre} - Tipo: {tipo} - Tiempo: {tiempo}")

class devolver_libro:
    def __init__(self,estado):
        self.estado = estado

class usuario:
    def __init__(self,nombre,id,libro):
        self.nombre=nombre
        self.id=id
        self.libro=libro


class biblioteca:
        def __init__(self,lista_de_libros,lista_de_usuarios):
            self.lisra_de_libros = lista_de_libros
            self.lista_de_usuarios = lista_de_usuarios

def main ():
    def prestar_libro = prestar_libro()

    while True:
            print("\n--  BIBLIOTECA--")
            print("1. Agregar un nuevo libro a la biblioteca")
            print("2. Eliminar un libro de la biblioteca    ")
            print("3. Prestar un libro de la biblioteca     ")
            print("4. Devolver un libro a la biblioteca:    ")
            print("5. Agregar un nuevo usuario              ")
            print("6. Eliminar un usuario                   ")
            print("7. Ver todos los libros en la biblioteca ")
            print("8. Ver todos los usuarios                ")
            print("0 Salida                                 ")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                nombre = input("Agregar libro: ")
            prestar_libro.prestar_libro(nombre)

            elif opcion == "2":
            nombre = input("Eliminar libro: ")
            prestar_libro.registrar_entrada(nombre)

            elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            prestar_libro.registrar_salida(nombre)

            elif opcion == "4":
            nombre = input("Ingrese el nombre del usuario: ")
            prestar_libro.registrar_salida(nombre)

            elif opcion == "5":
            nombre = input("Ingrese el nombre del usuario: ")
            prestar_libro.registrar_salida(nombre)

            elif opcion == "6":
            prestar_libro.listar_registros()

            elif opcion == "0":
            break
    else:
            print("Opción inválida. Intente nuevamente.")



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
        print("\n--  BIBLIOTECA--")
        print("1. Agregar usu")
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