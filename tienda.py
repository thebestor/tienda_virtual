from pedido import Pedido

class Tienda:
    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = [] # listas vacías todos los productos que la tienda tiene
        self._pedidos = [] # listas vacías todos los pedidos realizados

    def agregar_producto(self, producto):
        self._productos.append(producto)
    
    #Recorre la lista de productos y los imprime, usando el método __str__() de cada Producto.
    def mostrar_stock(self):
        print(f"Stock disponible en {self._nombre}:")
        for producto in self._productos:
            print(f" - {producto}")

    #Crea un nuevo pedido para el cliente recibido.
    def realizar_pedido(self, cliente, items):  # items = lista (producto, cantidad)
        pedido = Pedido(cliente)
        for producto, cantidad in items:
            pedido.agregar_item(producto, cantidad)
        self._pedidos.append(pedido)
        print("\nPedido registrado:")
        print(pedido)
    #Imprime todos los pedidos registrados, uno por uno.
    def mostrar_pedidos(self):
        print("\nPedidos realizados:")
        for pedido in self._pedidos:
            print(pedido)
            print("--------")
