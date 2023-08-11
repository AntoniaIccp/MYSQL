class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):	# agregó esta línea, toma un valor

        def add_to_front(self, val):
            new_node = SLNode(val)	# crea una nueva instancia de nuestra clase Node usando el valor dado

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head	# guarda el encabezado actual en una variable

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head	# ESTABLECE el nuevo nodo JUNTO AL encabezado actual de la lista

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node	# FIJA el encabezado de la lista AL nodo que creamos en el último paso
        return self	# return self para permitir el encadenamiento
