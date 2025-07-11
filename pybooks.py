#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
}
#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

# Stock marca
def stock_marca(marca):
    stockMarca = 0
    for codigo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            if codigo in stock:
                stockMarca += stock[codigo][1]
    print(f"Total stock unidades de {marca}: {stockMarca}")

#busqueda precios
def busqueda_precio(p_min, p_max):
    listaProductos = []
    for codigo, datos in stock.items():
        precio = datos[0]
        if precio >= p_min and precio <= p_max and datos[1] > 0:
            
            for modelo, datos in productos.items():
                if codigo == modelo:
                    listaProductos.append(datos[0] + "--" + codigo)                 
    if listaProductos:
        listaProductos.sort()
        print(f"Productos:", listaProductos)
    else:
        print("No hay productos en ese rango de precio")


#Listado productos
def ordenar_productos():
    listadoProductos = []
    i = 0
    for codigo, datos in productos.items():
        orden = datos [0] + " - " + codigo + " - " + datos[2] + " - " + datos[4]
        listadoProductos.append(orden)
    print("------- Listado de Notebooks Ordenados --------")
    for a in listadoProductos:
        print(f"{listadoProductos[i]}")
        i += 1                                                                                                          




def main():
    opcion = 0
    while opcion != 4:
        print("** MENU PRINCIPAL **")
        print("1. Stock marca.")
        print("2. Busqueda de precio.")
        print("3. Listado de productos.")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                marca = input("Ingrese una marca: ")
                stock_marca(marca)
            elif opcion == 2:
                condicional = True
                while condicional:
                    try:
                        p_min = int(input("Ingrese el precio minimo: "))
                        p_max = int(input("Ingrese el precio máximo: "))
                        if p_min < p_max:
                            busqueda_precio(p_min, p_max)
                            condicional = False
                        else:
                            raise TypeError
                    except ValueError as e:
                        print("El valor ingresado debe ser en numeros enteros.")
                    except TypeError as e:
                        print("El precio minimo tiene que ser menor al maximo")
            elif opcion == 3:
                ordenar_productos()
            elif opcion == 4:
                print("Programa finalizado.")
            else:
                print("Debe ingresar una opcion valida.")
        except:
            print("Ingrese una opcion válida.")
        print("")

main()

