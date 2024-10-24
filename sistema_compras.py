class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre de la prenda: {self.nombre}, Precio: {self.precio}, Stock: {self.cantidad}")
        
class Ropa_Hombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

class Ropa_Mujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self,prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()
    
    def guardar_inventario(self):
        with open('productos.txt', 'w') as archivo:
            for prenda in self.prendas:
                archivo.write(f"{prenda.__class__.__name__},{prenda.nombre},{prenda.precio},{prenda.cantidad},{prenda.talla}\n")

    def cargar_inventario(self):
        self.prendas = []
        try:
            with open('productos.txt', 'r') as archivo:
                for i in archivo:
                    clase, nombre, precio, cantidad, talla = i.strip().split(',')
                    if clase == 'Ropa_Hombre':
                        prenda = Ropa_Hombre(nombre, float(precio), int(cantidad), talla)
                    elif clase == 'Ropa_Mujer':
                        prenda = Ropa_Mujer(nombre, float(precio), int(cantidad), talla)
                    self.prendas.append(prenda)
        except FileNotFoundError:
            print("Error no se encontró el archivo")

    def comprar_prenda(self, nombre, cantidad):
        for prenda in self.prendas:
            if prenda.nombre.lower() == nombre.lower():
                if prenda.cantidad >= cantidad and cantidad > 0:
                    prenda.cantidad -= cantidad
                    print(f"Compra realizada con exito")
                    self.guardar_inventario()
                else:
                    print("No hay cantidad suficiente en stock")
                return
        print("Prenda no encontrada")

def menu():
    while True:
        print("1: Mostrar prendas\n2: Comprar prenda\n3: Salir")
        opc = input("Seleccione una opción: ")
        if opc == '1':
            inventario.mostrar_inventario()
        elif opc == '2':
            nombre_prenda = input("¿Qué prenda deseas comprar?\n")
            try:
                cantidad = int(input("¿Qué cantidad?\n"))
                if cantidad <= 0:
                    print("Cantidad incorrecta")
                    continue
                inventario.comprar_prenda(nombre_prenda, cantidad)
            except ValueError:
                print("Ingresa un número válido")
        elif opc == '3':
            print("Finalizado")
            break
        else:
            print("Opción no valida")
        

inventario = Inventario()
inventario.cargar_inventario()

menu()
