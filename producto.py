class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        
        
# metodo aumentar el stock en una cantidad especifica
    def actualizar_stock(self, cantidad):
        self._stock += cantidad

# Intenta restar stock. Si hay suficiente, lo descuenta y retorna True; si no, muestra un mensaje y retorna False.
    def descontar_stock(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock de {self._nombre}.")
            return False

#Métodos para acceder a los atributos privados de forma controlada.
    def get_precio(self):
        return self._precio

    def get_nombre(self):
        return self._nombre

# print(producto), muestre una cadena nombre, precio y stock.
    def __str__(self):
        return f"{self._nombre} - ${self._precio} ({self._stock} disponibles)"
