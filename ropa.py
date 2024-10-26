from producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def mostrar_info(self):
        return f"{self._nombre}/ Talla: {self._talla}/ Precio: {self._precio}"

class Camisa(Ropa):
    def mostrar_info(self):
        return f"Camisa: {super().mostrar_info()}"

class Pantalon(Ropa):
    def mostrar_info(self):
        return f"Pantalon: {super().mostrar_info()}"


class Zapato(Ropa):
    def mostrar_info(self):
        return f"Zapato: {super().mostrar_info()}"
    