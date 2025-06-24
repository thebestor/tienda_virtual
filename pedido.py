class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._items = []  # lista vacía _items donde se almacenarán los productos del pedido junto con sus cantidades.

# Método para agregar un producto al pedido.
#Antes de agregar el producto, intenta descontar stock con producto.descontar_stock(cantidad).
#Si hay stock suficiente, lo descuenta y agrega el ítem a la lista.
#Si no hay stock, muestra un mensaje y no lo agrega
    def agregar_item(self, producto, cantidad):
        if producto.descontar_stock(cantidad):
            self._items.append((producto, cantidad))
        else:
            print(f"No se pudo agregar {producto.get_nombre()} al pedido.")

# Recorre cada producto en el pedido y suma el total de la compra (precio * cantidad).
    def calcular_total(self):
        total = sum(producto.get_precio() * cantidad for producto, cantidad in self._items)
        if hasattr(self._cliente, "get_descuento"):
            descuento = self._cliente.get_descuento()
            total *= (1 - descuento / 100)
        return round(total, 2)



#Este método genera un texto descriptivo del pedido:
    def __str__(self):
        detalle = f"Pedido de {self._cliente.get_nombre()}:\n"
        for producto, cantidad in self._items:
            detalle += f" - {producto.get_nombre()} x{cantidad}\n"
        detalle += f"Total: ${self.calcular_total()}"
        return detalle
