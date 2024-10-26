
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_precio(self):
        return self._precio

    def mostrar_info(self):
        return f"{self._nombre} - Precio: {self._precio}"