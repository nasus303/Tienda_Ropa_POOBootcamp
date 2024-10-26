from ropa import Camisa
from ropa import Pantalon
from ropa import Zapato
from carrito import Carrito

class Tienda:
    def __init__(self):
        self._inventario = [
            Camisa("Camisa Azul", 50.0, "XL"),
            Pantalon("Pantalón de vestir", 100.0, "M"),
            Zapato("Zapatos de vestir", 50.0, "39")
        ]
        self._carrito = Carrito()

    def mostrar_inventario(self):
        print("Inventario:")
        for i, producto in enumerate(self._inventario, 1):
            print(f"{i}. {producto.mostrar_info()}")

    def seleccionar_producto(self, opcion):
        if 1 <= opcion <= len(self._inventario):
            producto = self._inventario[opcion - 1]
            self._carrito.agregar_producto(producto)
        else:
            print("Opción no válida.")

    def guardar_compra(self):
        self._carrito.mostrar_carrito()
        total = self._carrito.total()
        print(f"Monto total: {total}")