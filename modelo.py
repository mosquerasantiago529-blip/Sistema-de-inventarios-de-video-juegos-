class Videojuego:
    def __init__(self, id=None, nombre="", precio=0.0, cantidad=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad  # stock disponible

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Precio: ${self.precio:,.2f} | Stock: {self.cantidad}"