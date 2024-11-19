import curses
import functions as fn
import sys

inventario = fn.inventario
ventas = fn.ventas
txt = 'Presiona Enter para regresar al menú principal'

def opcion1():
    while True:
        try:
            vendedor = input('Ingrese el nombre del vendedor: ')
            modelo = int(input('Ingrese el número de modelo del artículo: '))
            unidades = int(input('Ingrese la cantidad de artículos vendidos: '))
            break
        
        except ValueError:
            print('Por favor introduzca datos válidos. Recuerde que debe teclear el código númerico del producto, no su nombre.\n')

    fn.registrar_venta(vendedor, modelo, unidades)
    print('')
    print(txt, '\n')

def opcion2():
    while True:
        try:
            modelo = int(input('Ingrese el numero de modelo del artículo: '))
            cantidad = int(input('Introduzca la cantidad de unidades a agregar: '))
            break
        except ValueError:
            print('Por favor introduzca datos válidos. Recuerde que debe teclear el código númerico del producto, no su nombre.\n')
    fn.registrar_llegada(modelo, cantidad)
    print('')
    print(txt, '\n')

def opcion3():
  
    fn.mostrar_inventario()
    print('')
    print(txt, '\n')
  

def opcion4():
    
    fn.mayor_ventas()
    print('')
    print(txt, '\n')

def opcion5():

    fn.mx_vendedor()
    print('')
    print(txt, '\n')



def opcion6():

    fn.ventas_totales()
    print('')
    print(txt, '\n')


def opcion7():
    
    nombre = input('Indica el nombre del vendedor: ')
    fn.reporte_vendedor(nombre)
    print('')
    print(txt, '\n')

def opcion8():
    
    sys.exit()

def main(stdscr):
  curses.curs_set(0)  # Oculta el cursor

  while True:#Bucle que engloba todo el menú
      # Configuración inicial
      opcion_actual = 0
      opciones = ["- Registrar venta", "- Registrar llegada", "- Mostrar inventario", "- Modelo más vendido", "- Vendedor con mas ventas", "- Ventas totales", "- Generar Reporte de Ventas", "- Salir"]
      funciones = {0: opcion1, 1: opcion2, 2: opcion3, 3: opcion4, 4: opcion5, 5: opcion6, 6: opcion7, 7:opcion8}
      stdscr.clear()

      while True:
          stdscr.clear()

          # Imprime las opciones
          for i, opcion in enumerate(opciones):
              if i == opcion_actual:
                  stdscr.addstr(i, 0, f"> {opcion}", curses.A_REVERSE)
              else:
                  stdscr.addstr(i, 0, f"  {opcion}")

          # Captura la entrada del teclado
          key = stdscr.getch()

          # Maneja la navegación
          if key == curses.KEY_UP:
              opcion_actual = (opcion_actual - 1) % len(opciones)
          elif key == curses.KEY_DOWN:
              opcion_actual = (opcion_actual + 1) % len(opciones)
          elif key == curses.KEY_ENTER or key in [10, 13]:
              curses.endwin()
              funciones[opcion_actual]()  # Llama a la función asociada a la opción seleccionada
              stdscr.getch()
              break


curses.wrapper(main)
