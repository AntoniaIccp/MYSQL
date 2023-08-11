class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1=numero1
        self.numero2=numero2

    def sumar(self):
        return self.numero1 + self.numero2
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def division(self):
        return self.numero1 / self.numero2
    
    def multiplicar(self):
        return self.numero1 * self.numero2

def mostrar_menu():
    print("*------ Calculadora ------*")
    print("|| opcion 1: sumar       ||")
    print("|| opcion 2: restar      ||")
    print("|| opcion 3: division    ||")
    print("|| opcion 4: multiplicar ||")
    print("|| opcion : Salir   ||")
    print("*--------------------------*")
    
calculadora = Calculadora(0,0)

while True:
    mostrar_menu()
    opcion = input("Ingresa el: ")

    if opcion == "1":
            numero1 = (input("Ingrese el primer numero: "))
            numero2 = (input("Ingresa el segundo numero "))
            resultado = calculadora.sumar(numero1,numero2)
            print(f"Ingresa el:{numero1}+{numero2} es: {resultado}\n")

    elif opcion == "2":
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingresa el segundo numero "))
            resultado = calculadora.resta(numero1,numero2)
            print(f"Ingresa el:{numero1}-{numero2} es: {resultado}\n")

    elif opcion == "3":
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingresa el segundo numero "))
            resultado = calculadora.division(numero1,numero2)
            print(f"Ingresa el:{numero1}/{numero2} es: {resultado}\n")

    elif opcion == "4":
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingresa el segundo numero "))
            resultado = calculadora.multiplicacion(numero1,numero2)
            print(f"Ingresa el:{numero1}*{numero2} es: {resultado}\n")
        
    elif opcion == "0":
                print("¡Hasta luego!")
                break
    
    else:
        print("Opcion invalida. Intente nuevamente.\n")
               