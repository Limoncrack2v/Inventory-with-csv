import csv
import os



def archivo_inv():
   #Poner ruta al archivo
    file = open('C:\\Users\\hugo9\\Documents\\Programación\\Python\\Inventory_Project\\Inventario-Inventario.csv', 'r', newline='', encoding='utf-8')

    archivo = csv.reader(file)

    inventario = []

    for fila in archivo:
        inventario.append(fila)
    
    for c in range (0, len(inventario[0])):
        for f in range (1, len(inventario)):
           
          
           if c == 2 or c == 0:
              inventario[f][c] = int(inventario[f][c])

    file.close()
              
    return inventario

inventario = archivo_inv()

def archivo_ven():
   #Poner ruta al archivo
    file = open('C:\\Users\\hugo9\\Documents\\Programación\\Python\\Inventory_Project\\Inventario-Ventas.csv', 'r', newline='', encoding='utf-8')

    archivo = csv.reader(file)

    ventas = []

    for fila in archivo:
        ventas.append(fila)
    
    for c in range (1, len(ventas[0])):
        for f in range (len(ventas)):
    
            ventas[f][c] = int(ventas[f][c])

    file.close()

    return ventas
    

ventas = archivo_ven()
fila = len(inventario)
columna = len(inventario[0])

filac = len(ventas)
columnac = len(ventas[0])
ventas_totales = 0





def registrar_venta(vendedor, modelo, unidades):
    ventas_totales = 0
  
    for f in range(filac):       
        if ventas[f][0] == vendedor:
            print('Acceso correcto')
            break
        
        if f +1 == filac:
            print('Intente de nuevo con un vendedor válido.')


  
  
    for f in range(1, fila):

        if inventario[f][0] == modelo:
            print('Modelo encontrado')
        
        
            if inventario[f][2] >= unidades:
                print('Cantidad disponible')
                inventario[f][2] -= unidades
                ventas_totales += unidades
                sumar_venta(ventas_totales, modelo, vendedor)
                print('Venta realizada')
            else:
                print('No hay suficientes artículos disponibles.')
                
            return

        
    print('No existe el modelo')


def sumar_venta(ventas_totales, modelo, vendedor):
    idx = 0
    for f in range(fila):
        if inventario[f][0] == modelo:
            idx = f

    idv = 0
    for f in range(filac):
        if ventas[f][0] == vendedor:
            idv = f

    ventas[idv][idx] += ventas_totales

  

def registrar_llegada(modelo, cantidad):
  
  
    for f in range(1, fila):
        if inventario[f][0] == modelo:
            print('Modelo encontrado.')
            inventario[f][2] += cantidad
            print('Cantidad agregada exitosamente.')
            return
        
    print(f'No existe el modelo {modelo}')


def mostrar_inventario():
  for i in inventario:
    print('\n'.join(map(str, inventario)))
    break


def mayor_ventas():
    temp = []
    idx = 0
    for c in range(1, columnac):
        suma = 0
        for f in range(filac):
            suma+= ventas[f][c]

        temp.append(suma)

    m = max(temp)
    
    for i in temp:
        if i == m:
            idx = temp.index(i)

    print(f'El modelo más vendido es el {inventario[idx+1][1]} con {m} ventas')


def mx_vendedor():
    temp = []
    for f in range(0, filac):
        suma = 0
        for c in range(1, columnac):
            suma += ventas[f][c]
        
        temp.append(suma)

    m = max(temp)

    for i in temp:
        if i == m:
            idx = temp.index(i)

    
    print(f'El vendedor con registro de mayor ventas es: {ventas[idx][0]} con {m} ventas')




def reporte_vendedor(nombre):
    idv = 0

    if nombre in ventas:
        for f in range(filac):
            if ventas[f][0] == nombre:
                idv = f

        #if f+1 == filac:
            #print("No se encontró a ese vendedor")

        #Colocar ruta del archivo con \\ doble
        name_file = f'C:\\Users\\hugo9\\Documents\\Programación\\Python\\Inventory_Project\\Reporte_ventas_{nombre}.csv'
        file2 = open(name_file, 'w',newline = '')
        escribir = csv.writer(file2)
        texto = nombre + "\n"

        for f in range(1, fila):
            texto += f"{inventario[f][0]},{inventario[f][1]},{ventas[idv][f]}\n"

        lineas = texto.split("\n")
        lista_datos = [linea.split(',') for linea in lineas if linea]
        escribir.writerows(lista_datos)

        print(f'Archivo {os.path.basename(name_file)} generado')
    
    else:
        print(f'El vendedor {nombre} no existe')

def ventas_totales():
    temp = []
    for c in range(1, columnac):
        suma = 0
        for f in range(filac):
            suma += ventas[f][c]
        temp.append(suma)
    total = sum(temp)
    print(f'La venta total es de: {total} artículos')



        
    





