
from base_datos import BaseDatos
from producto_servicio import VideojuegoServicio


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debes ingresar un numero entero.")


def leer_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debes ingresar un precio valido.")


def mostrar_menu():
    print("\n" + "=" * 45)
    print("     SISTEMA DE INVENTARIO DE VIDEOJUEGOS")
    print("=" * 45)
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")
    print("=" * 45)


def menu():
    BaseDatos.crear_tabla()
    servicio = VideojuegoServicio()

    while True:
        mostrar_menu()
        opcion = leer_entero("Selecciona una opcion: ")

        if opcion == 1:
            nombre = input("Nombre: ")
            precio = leer_flotante("Precio: ")
            cantidad = leer_entero("Stock: ")

            ok, mensaje = servicio.registrar(nombre, precio, cantidad)
            print(mensaje)

        elif opcion == 2:
            videojuegos = servicio.listar_inventario()

            if not videojuegos:
                print("El inventario esta vacio.")
            else:
                for juego in videojuegos:
                    print(juego)

        elif opcion == 3:
            id_juego = leer_entero("ID del videojuego: ")
            juego, mensaje = servicio.buscar(id_juego)
            print(mensaje)

            if juego:
                print(juego)

        elif opcion == 4:
            id_juego = leer_entero("ID a actualizar: ")
            juego, mensaje = servicio.buscar(id_juego)

            if not juego:
                print(mensaje)
                continue

            print("Datos actuales:", juego)

            nombre = input("Nuevo nombre: ")
            precio = leer_flotante("Nuevo precio: ")
            cantidad = leer_entero("Nuevo stock: ")

            ok, mensaje = servicio.modificar(
                id_juego, nombre, precio, cantidad
            )
            print(mensaje)

        elif opcion == 5:
            id_juego = leer_entero("ID a eliminar: ")
            ok, mensaje = servicio.eliminar_juego(id_juego)
            print(mensaje)

        elif opcion == 6:
            id_juego = leer_entero("ID del videojuego: ")
            cantidad = leer_entero("Unidades a vender: ")

            ok, mensaje = servicio.vender(id_juego, cantidad)
            print(mensaje)

        elif opcion == 7:
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion no valida.")

        input("\nPresiona ENTER para continuar...")


if __name__ == "__main__":
    menu()
