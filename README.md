----- Estructura del Proyecto -----

producto.py: Define la clase Producto, la cual actúa como clase base para todos los productos.

ropa.py: Contiene la clase Ropa, que hereda de Producto e incluye clases específicas como Camisa, Pantalon y Zapato que heredan de Ropa.

inventario.py: Define la clase Inventario para gestionar la lista de productos en stock.

tienda.py: Contiene la clase Tienda, que permite mostrar el inventario, seleccionar productos y guardar la compra en el carrito.

carrito.py: Contiene la clase Carrito, que gestiona los productos seleccionados y el cálculo del monto total.

menu.py: Archivo principal que permite la interacción con el usuario a través de un menú de opciones.

----- Principios de POO Implementados -----

Encapsulamiento: Los atributos de cada clase están encapsulados, y algunos son privados, para controlar el acceso y la modificación, se utiliza get y set.

Herencia: Ropa hereda de Producto, mientras que Camisa, Pantalon, y Zapato heredan de Ropa.

Polimorfismo: Se implementa el método mostrar_info en cada clase hija para proporcionar una salida personalizada de información del producto.

Abstracción: La lógica de compra está encapsulada en la clase Tienda, ocultando los detalles internos del carrito y el inventario.

----- Interacción con el Usuario -----

Al ejecutar el programa desde menu.py, el usuario verá un menú con las siguientes opciones:

Mostrar inventario: Muestra los productos disponibles en la tienda.

Agregar al carrito: Permite seleccionar un producto para agregarlo al carrito.

Guardar compra: Muestra un resumen de los productos en el carrito y el total a pagar.

Salir: Finaliza el programa.
