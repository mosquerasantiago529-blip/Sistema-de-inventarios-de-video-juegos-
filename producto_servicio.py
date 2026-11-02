from modelo import Videojuego
from producto_dao import VideojuegoDAO

class VideojuegoServicio:
    def __init__(self):
        self.dao = VideojuegoDAO()

    def registrar(self, nombre, precio, cantidad):
        # Validaciones
        if not nombre.strip():
            return False, " El nombre no puede estar vacío."
        if precio <= 0:
            return False, " El precio debe ser mayor a cero."
        if cantidad < 0:
            return False, " La cantidad no puede ser negativa."
        
        juego = Videojuego(nombre=nombre.strip(), precio=precio, cantidad=cantidad)
        exito = self.dao.insertar(juego)
        if exito:
            return True, " Videojuego registrado correctamente."
        return False, "No se pudo registrar el videojuego."

    def listar_inventario(self):
        return self.dao.listar_todos()

    def buscar(self, id):
        if id <= 0:
            return None, " El ID debe ser positivo."
        juego = self.dao.buscar_por_id(id)
        if not juego:
            return None, f" No existe un videojuego con ID {id}."
        return juego, " Encontrado:"

    def modificar(self, id, nuevo_nombre, nuevo_precio, nueva_cantidad):
        juego = self.dao.buscar_por_id(id)
        if not juego:
            return False, f" No existe el videojuego con ID {id}."
        
        if not nuevo_nombre.strip():
            return False, " El nombre no puede estar vacío."
        if nuevo_precio <= 0:
            return False, " El precio debe ser mayor a cero."
        if nueva_cantidad < 0:
            return False, " La cantidad no puede ser negativa."
        
        juego.nombre = nuevo_nombre.strip()
        juego.precio = nuevo_precio
        juego.cantidad = nueva_cantidad
        
        self.dao.actualizar(juego)
        return True, " Videojuego actualizado correctamente."

    def eliminar_juego(self, id):
        if not self.dao.buscar_por_id(id):
            return False, f"No existe el videojuego con ID {id}."
        self.dao.eliminar(id)
        return True, " Videojuego eliminado correctamente."

    def vender(self, id, cantidad_vender):
        if cantidad_vender <= 0:
            return False, " La cantidad a vender debe ser mayor a cero."
        
        juego = self.dao.buscar_por_id(id)
        if not juego:
            return False, f"No existe el videojuego con ID {id}."
        
        if cantidad_vender > juego.cantidad:
            return False, f" Stock insuficiente. Disponibles: {juego.cantidad}, solicitados: {cantidad_vender}"
        
        juego.cantidad -= cantidad_vender
        self.dao.actualizar(juego)
        return True, f" Venta realizada. Stock restante: {juego.cantidad}"