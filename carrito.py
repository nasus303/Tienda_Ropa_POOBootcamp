class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)
        print(f"{producto.mostrar_info()} añadido al carrito")

    def mostrar_carrito(self):
        if not self._productos:
            print("El carrito está vacío.")
        for producto in self._productos:
            print(producto.mostrar_info())

    def total(self):
        return sum(producto.get_precio() for producto in self._productos)