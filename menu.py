from tienda import Tienda

def menu():
    tienda = Tienda()

    while True:
        print("1: Mostrar inventario\n2: Agregar al carrito\n3: Guardar compra\n4: Salir")
        opc = input("Ingrese una opción: ")

        if opc == "1":
            tienda.mostrar_inventario()
        elif opc == "2":
            tienda.mostrar_inventario()
            try:
                nro = int(input("Ingrese el número del producto que desea agregar a su carrito: "))
                tienda.seleccionar_producto(nro)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opc == "3":
            tienda.guardar_compra()
            break
        elif opc == "4":
            print("Finalizado")
            break
        else:
            print("Opción no valida")

menu()