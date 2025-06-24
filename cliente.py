class Cliente:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email       

    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def __str__(self):
        return f"{self._nombre} ({self._email})"

class ClienteVIP(Cliente):
    def __init__(self, nombre, email, descuento):
        super().__init__(nombre, email)
        self._descuento = descuento  # porcentaje de descuento (ej. 10 para 10%)

    def get_descuento(self):
        return self._descuento

    def __str__(self):
        return f"{self._nombre} ({self._email}) - Cliente VIP ({self._descuento}% off)"
    
