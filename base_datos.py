import sqlite3

class BaseDatos:
    @staticmethod
    def obtener_conexion():
        return sqlite3.connect('inventario.db')

    @staticmethod
    def crear_tabla():
        conexion = BaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videojuegos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()