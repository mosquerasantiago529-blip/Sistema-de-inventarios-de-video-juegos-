# 🎮 Sistema de Inventario de Videojuegos

Sistema de consola desarrollado en **Python y SQLite** para administrar un inventario de videojuegos mediante operaciones CRUD y control de ventas, aplicando el patrón de diseño DAO.

## 🎯 Propósito

Permitir el registro, consulta, modificación y eliminación de videojuegos, así como el control de ventas y stock, conservando los datos entre diferentes ejecuciones del programa.

## 📁 Estructura del proyecto

| Archivo | Responsabilidad |
|---|---|
| `modelo.py` | Contiene la clase Videojuego y sus atributos. |
| `base_datos.py` | Administra la conexión a SQLite y crea las tablas. |
| `producto_dao.py` | Contiene las operaciones SQL del CRUD. |
| `producto_servicio.py` | Implementa las reglas del negocio y validaciones. |
| `main.py` | Contiene el menú interactivo de consola. |
| `inventario.db` | Base de datos SQLite creada automáticamente. |

## ⚙️ Funcionalidades implementadas

- Registrar videojuegos con nombre, precio y cantidad.
- Mostrar el inventario completo.
- Buscar videojuegos mediante su ID.
- Actualizar nombre, precio y stock.
- Eliminar videojuegos del inventario.
- Vender unidades y descontarlas del stock disponible.
- Conservar los datos mediante SQLite.

## ✅ Validaciones

- No permite nombres vacíos.
- El precio debe ser mayor que cero.
- No permite cantidades negativas.
- No permite ventas con cantidades menores o iguales a cero.
- No permite vender más unidades de las disponibles.
- Informa cuando un ID no existe.
- Controla entradas incorrectas para evitar cierres inesperados.

## 🚀 Cómo ejecutar el proyecto

**Requisitos:** Python 3 instalado.

1. Descargar o clonar el repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

La base de datos `inventario.db` y sus tablas se crean automáticamente al iniciar el programa.

## 🧪 Pruebas realizadas

| Prueba | Resultado |
|---|---|
| Registrar Resident Evil 4, precio 180000 y stock 10 | Exitoso |
| Mostrar inventario | Exitoso |
| Buscar un ID existente | Exitoso |
| Actualizar un videojuego | Exitoso |
| Vender 3 unidades | Stock actualizado de 10 a 7 |
| Intentar vender 20 unidades | Operación rechazada |
| Buscar un ID inexistente | Mensaje de aviso |
| Eliminar un videojuego | Exitoso |

## 📸 Evidencias de funcionamiento

Las siguientes evidencias muestran las pruebas realizadas en la aplicación:

> Agregar aquí las capturas de pantalla de:
>
> 1. Menú principal.
> 2. Registro de un videojuego.
> 3. Inventario completo.
> 4. Búsqueda por ID.
> 5. Actualización de un videojuego.
> 6. Venta exitosa de unidades.
> 7. Venta rechazada por falta de stock.
> 8. Búsqueda de un ID inexistente.
> 9. Eliminación de un videojuego.

## 📝 Notas importantes

- Se eliminó el registro automático del videojuego de ejemplo.
- Los datos permanecen guardados entre ejecuciones.
- Las consultas SQL se encuentran en el DAO y no en el programa principal.
- Se mantiene la separación de responsabilidades entre las diferentes capas de la aplicación.

## 👨‍💻 Autor

**Estudiante:** Santiago Mosquera  
**Curso:** Programación Orientada a Objetos  
**Fecha:** Noviembre de 2026
2