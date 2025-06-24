from cliente import Cliente
from cliente import ClienteVIP
from producto import Producto
from tienda import Tienda
from pedido import Pedido

# Crea un producto con nombre, precio y stock inicia
p1 = Producto("Auriculares Bluetooth", 2500, 10)
p2 = Producto("Mouse",1500,6)

#Muestra el producto en consola, descuenta 3 unidades de stock, y lo vuelve a mostrar.
#print(p1)
#p1.descontar_stock(3)
#print(p1)

# Crea un cliente con nombre y correo, y lo muestra.
cliente1 = Cliente("María López", "maria@gmail.com")
cliente2 = ClienteVIP("Juan Pérez", "juan@gmail.com", 10)

print("\n--- Clientes ---")
print(cliente1)
print(cliente2)

# Crea una tienda, le carga el producto, y muestra su stock actual.
mi_tienda = Tienda("TechStore")
mi_tienda.agregar_producto(p1)
otra_tienda = Tienda("DELTA")
otra_tienda.agregar_producto(p2)

# Mostrar stock
print("\n---Stock en tienda---")
mi_tienda.mostrar_stock()
otra_tienda.mostrar_stock()

# Crea un pedido para ese cliente normal y agrega 2 unidades del producto.
#Internamente descuenta stock al agregar.
#Luego muestra el resumen del pedido.
print("\n--- Pedido Cliente Normal ---")
pedido1 = Pedido(cliente1)
pedido1.agregar_item(p1, 2)  # agrega 2 auriculares
print(pedido1)

# Pedido VIP
print("\n--- Pedido Cliente VIP ---")
pedido2 = Pedido(cliente2)
pedido2.agregar_item(p1, 2)
print(pedido2)
pedido3 = Pedido(cliente2)
pedido3.agregar_item(p2, 4)

# Agregar pedidos a la tienda
mi_tienda.realizar_pedido(cliente1, [(p1, 2)])
mi_tienda.realizar_pedido(cliente2, [(p1, 2)])
otra_tienda.realizar_pedido(cliente2,[(p2,4)])

# Mostrar stock actualizado
print("\n--- Stock Final ---")
mi_tienda.mostrar_stock()
otra_tienda.mostrar_stock()

# Mostrar todos los pedidos
print("\n--- Todos los Pedidos ---")
mi_tienda.mostrar_pedidos()
otra_tienda.mostrar_pedidos()
 

# Mostrar stock
#mi_tienda.mostrar_stock()

# Usa el método de la tienda para procesar un pedido: recibe el cliente y una lista de productos con cantidades.
#mi_tienda.realizar_pedido(cliente1, [(p1, 2)])  # 2 auriculares más

# Lista todos los pedidos registrados hasta ese momento.
#mi_tienda.mostrar_pedidos()
