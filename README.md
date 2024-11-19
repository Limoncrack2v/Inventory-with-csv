Descripción
Este proyecto es un Sistema de Gestión de Inventario y Ventas desarrollado en Python. Permite gestionar el inventario de productos, registrar ventas, monitorear el rendimiento de los vendedores, y generar reportes detallados. Está diseñado para funcionar en una interfaz de terminal interactiva con menús navegables.

Características principales
Registrar ventas: Agrega registros de ventas asociadas a un vendedor y un producto.
Actualizar inventario: Registra la llegada de nuevos productos y actualiza el inventario.
Consultar inventario: Muestra el estado actual del inventario.
Modelo más vendido: Identifica el producto con mayor número de ventas.
Vendedor con más ventas: Muestra el vendedor con el mejor rendimiento.
Ventas totales: Calcula el total de artículos vendidos.
Generar reporte de ventas: Crea un archivo CSV con el desempeño de un vendedor específico.
Interfaz de menú: Navegación intuitiva en consola usando las flechas del teclado.
Estructura de archivos
El proyecto depende de los siguientes archivos de datos:

Inventario-Inventario.csv: Archivo con los detalles del inventario (modelo, cantidad, etc.).
Inventario-Ventas.csv: Archivo con los registros de ventas por vendedor y modelo.
Requisitos previos
Python 3.6 o superior.
Dependencias: El módulo curses y soporte para archivos CSV.
Instalación
Clona o descarga este repositorio.

Asegúrate de que las rutas de los archivos CSV (Inventario-Inventario.csv y Inventario-Ventas.csv) en el código estén configuradas correctamente.

Uso
Al iniciar el programa, un menú interactivo aparece en la terminal con las siguientes opciones:

Registrar venta: Ingresa el nombre del vendedor, el modelo del producto, y las unidades vendidas.
Registrar llegada: Actualiza el inventario con nuevos productos.
Mostrar inventario: Consulta el estado actual del inventario.
Modelo más vendido: Obtén información sobre el producto más popular.
Vendedor con más ventas: Identifica al vendedor más exitoso.
Ventas totales: Muestra el total de unidades vendidas.
Generar reporte: Crea un reporte en formato CSV para un vendedor específico.
Salir: Finaliza el programa.
Notas importantes
Rutas de los archivos CSV: Cambia las rutas en las funciones archivo_inv y archivo_ven según la ubicación en tu sistema.
Formato de los archivos CSV:
Inventario-Inventario.csv: Debe incluir columnas como ID del modelo, nombre, y cantidad.
Inventario-Ventas.csv: Debe incluir el nombre del vendedor y columnas para las ventas por modelo.
Ejemplo de uso
Selecciona la opción deseada usando las teclas arriba/abajo.
Presiona Enter para confirmar tu selección.
Sigue las instrucciones en pantalla.
