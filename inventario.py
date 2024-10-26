class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
        print("Prenda agregada con exito")

    def mostrar_inventario(self):
        for prenda in self.prendas:
            print(prenda.mostrar_info())