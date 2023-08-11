from tienda import Tienda
from producto import Producto

def mostrar_menu():
    print("*--------- Tienda ---------*")
    print("|| Opcion 1: Registrar nuevo producto       ||")
    print("|| Opcion 2: Registrar una ventana          ||")
    print("|| Opcion 3: Listar productos               ||")
    print("|| Opcion 4: Actualizar productos           ||")
    print("|| OPCIÓN 0: Salir                          ||")
    print("*--------------------------------------------*")

def main():
    Tienda1 = Tienda("baul de antonia")
    while True:
        mostrar_menu()
        option= input("Escoga una opcion:")

        if option == "1":
            print("+-----------------------------------+")
            print("|--------- Ingresar nombre ---------|")
            print("+-----------------------------------+")
            Nombre= input("Ingrese el nombre del producto:")
            Precio= input("Ingrese el precio:")
            Categoria= input("Ingrese la categoria:")
            nuevo_producto = Producto(Nombre, Precio, Categoria)
            Tienda1.agregar_producto(nuevo_producto)
            print("+-----------------------------------+")
            print("|--------- Producto Creado ---------|")
            print("+-----------------------------------+")

        if option == "2":
            pass
            
        if option == "3":
            Tienda1.listar_productos()

        if option == "4":
            print("+-----------------------------------+")
            print("|--------- Ingresar nombre ---------|")
            print("+-----------------------------------+")
            Nombre= input("Ingrese el nombre del producto:")
            Precio= input("Ingrese el precio:")
            Categoria= input("Ingrese la categoria:")
            nuevo_producto = Producto(Nombre, Precio, Categoria)
            Tienda1.modificar_producto(nuevo_producto)
            print("+-----------------------------------+")
            print("|--------- Producto Modificado ---------|")
            print("+-----------------------------------+")

        if option == "0":
            print("¡Hasta Luego!")
            break

        else:
            print("option invalida, intente nuevamente. \n")

if __name__ == "__main__":
    main()