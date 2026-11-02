import sqlite3
from base_datos import BaseDatos
from modelo import Videojuego

class VideojuegoDAO:
    def insertar(self, videojuego):
        conexion = BaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO videojuegos (nombre, precio, cantidad) VALUES (?, ?, ?)",
                (videojuego.nombre, videojuego.precio, videojuego.cantidad)
            )
            videojuego.id = cursor.lastrowid 
            conexion.commit()
            return True
        except sqlite3.IntegrityError: 
            return False
        finally:
            conexion.close() 

    def listar_todos(self):
        conexion = BaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, cantidad FROM videojuegos")
        registros = cursor.fetchall()
        conexion.close()
        return [Videojuego(*reg) for reg in registros]

    def buscar_por_id(self, id):
        conexion = BaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, cantidad FROM videojuegos WHERE id = ?", (id,))
        registro = cursor.fetchone()
        conexion.close()
        return Videojuego(*registro) if registro else None

    def actualizar(self, videojuego):
        conexion = BaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE videojuegos SET nombre=?, precio=?, cantidad=? WHERE id=?",
            (videojuego.nombre, videojuego.precio, videojuego.cantidad, videojuego.id)
        )
        filas = cursor.rowcount
        conexion.commit()
        conexion.close()
        return filas > 0

    def eliminar(self, id):
        conexion = BaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM videojuegos WHERE id = ?", (id,))
        filas = cursor.rowcount
        conexion.commit()
        conexion.close()
        return filas > 0