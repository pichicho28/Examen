stock_marca = 0
actualizar_precio = 0

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], #HP
    '2175HD': [327990,4],  #lenovo
    'JjfFHD': [424990,1], #Asus
    'fgdxFHD': [664990,21], #HP
    '123FHD': [290890,32], #lenovo
    '342FHD': [444990,7], #lenovo
    'GF75HD': [749990,2], #Asus
    'UWU131HD': [349990,1], #Dell
    'FS1230HD': [249990,0], 
}


while True:
    print("--------MENU PRINCIPAL--------");
    print("1) Stock marca.");
    print("2) Busqueda por precio.");
    print("3) Actualizar precio.");
    print("4) Salir.");


    opcion = input("Elige las opciones: ")

    if opcion =="1":
        stock_marca = input("Ingrese la marca: ")
        if stock_marca == "HP" or stock_marca == "lenovo" and stock_marca == "Asus" and stock_marca == "Dell":
                
                if stock == "HP":
                    print(f"el stock es: {stock['8475HD']}");
                    print(f"el stock es: {stock['fgdxFHD']}\n");
                elif stock == "lenovo":
                    print(f"el stock es: {stock['2175HD']}");
                    print(f"el stock es: {stock['123FHD']}");
                    print(f"el stock es: {stock['342FHD']}\n");
                elif stock == "Asus":
                    print(f"el stock es: {stock['JjfFHD']}");
                    print(f"el stock es: {stock['GF75HD']}\n");
                elif stock == "Dell":
                    print(f"el stock es: {stock['UWU131HD']}\n");
                else:
                    print(f"el stock es: {stock['FS1230HD']}\n");



    elif opcion =="2":
        try: 
            precioMinimo = int(input("Ingrese el precio minimo: "));
            precioMaximo= int(input("Ingrese el precio maximo: "));
        except ValueError:
            print("debe de ingresar un entero");
        
        for i in range(1,9):
            stock = i



            print(f"Los notebooks entre los precios consultas son: {stock}");
            #print(f"Los notebooks entre los precios consultas son: {stock['fgdxFHD']}")
            #print(f"Los notebooks entre los precios consultas son: {stock['2175HD']}")
            #print(f"Los notebooks entre los precios consultas son: {stock['123FHD']}")
            #print(f"Los notebooks entre los precios consultas son: {stock['342FHD']}")
            #print(f"Los notebooks entre los precios consultas son: {stock['JjfFHD']}")
            #print(f"Los notebooks entre los precios consultas son: {stock['GF75HD']}")
            #print(f"Los notebooks entre los precios consultas son: {stock['UWU131HD']}")





#actualizar_precio
    elif opcion =="3":
        if actualizar_precio == stock:
            actualizar_precio = int(input("Ingrese el modelo a actualizar: "))
            false = actualizar_precio
            nuevoPrecio = int("ingrese un nuevo precio: ")
        elif actualizar_precio == True:
            print("Desea actualizar otro precio (s/n)?: ")
        else:
            print("el modelo no existe.")
            
           


    
    elif opcion =="4":
        print("Programa finalizado")
        break

    else:
        print("¡Ingrese una de las opciones!")