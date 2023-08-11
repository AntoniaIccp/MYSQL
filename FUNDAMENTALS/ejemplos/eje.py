
class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido


#DECLARACION DE UNA CLASE ALUMNO
class Alumno:
    def __init__(self,nombre,apellido,correo,curso,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo 
        self.curso=curso
        self.edad=edad
        self.balance_cuenta = 0


    def hacer_deposito(self,monto):
        self.balance_cuenta += monto
    
    def hacer_giro(self,monto):
        self.balance_cuenta -= monto




#DECLARACION DE UNA INSTANCIA ALUMNO
Anto = Alumno("Antito","Gomez","antito@gmail.com","4ªC",17)
Deivid = Alumno("David","Ponce","david@gmail","4ªC" ,25)

#MENSAJES DEL OBJETO.

# print(f"hola me llamo: {Anto.nombre} y mi curso es  {Anto.curso} y mi edad es {Anto.edad}")
# print(f"hola mi nobre es {Deivid.nombre} y mi edad es {Deivid.edad}")

Anto.hacer_deposito(1000)
Anto.hacer_giro(500)


print(f"Mi saldo en la cuenta es: ${Anto.balance_cuenta}")





