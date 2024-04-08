costalmacr = 7.00
costalmacs = 8.00
costalmacd = 6.00
precventr = 29.00
precvents = 30.00
precventd = 26.50
maxtanque = 80
tanquer = 40
tanques = 40
tanqued = 40
trabajadorjd = 1
trabajarorjv = 1
trabajadorjn = 1
while True: 
    print("Bienvenido a la gasolinera")
    print("1. Gestionar inventario")
    print("2. Venta de combustible")
    print("3. Gestión de turnos")
    print("4. Reporte de rentabilidad")
    print("5. Salir")
    opcion = int(input("Ingrese la opcion que desea realizar: "))
    if opcion == 1:
        print("Gestionar inventario")
        print ("El deposito de gasolina regular tiene ", tanquer, " galones")
        print ("El deposito de gasolina super tiene ", tanques, " galones")
        print ("El deposito de gasolina diesel tiene ", tanqued, " galones")
        elec = input("¿deseea agregar combustible a un deposito? (s/n): ")
        if elec == "s":
            cantr = int(input("Ingrese la cantidad de gasolina regular que desea agregar: "))
            if tanquer + cantr > maxtanque:
                print("No se puede agregar esa cantidad de gasolina regular porque sobrepasa el limite del tanque")
            else:
                tanquer = tanquer + cantr
            cants = int(input("Ingrese la cantidad de gasolina super que desea agregar: "))
            if tanques + cants > maxtanque:
                print("No se puede agregar esa cantidad de gasolina super porque sobrepasa el limite del tanque")
            else:
                tanques = tanques + cants
            cantd = int(input("Ingrese la cantidad de gasolina diesel que desea agregar: "))
            if tanqued + cantd > maxtanque:
                print("No se puede agregar esa cantidad de gasolina diesel porque sobrepasa el limite del tanque")
            else:
                tanqued = tanqued + cantd

    elif opcion == 2:
        print ("El deposito de gasolina regular tiene ", tanquer, " galones y cuesta ", tanquer * precventr, "Quetzales" )
        print ("El deposito de gasolina super tiene ", tanques, " galones y cuesta ", tanques * precvents, "Quetzales" )
        print ("El deposito de gasolina diesel tiene ", tanqued, " galones y cuesta ", tanqued * precventd, "Quetzales" )
        tipc = input("Ingrese el tipo de combustible que desea comprar (r/s/d): ")
        cantc = int(input("Ingrese la cantidad de combustible que desea comprar: "))
        if tipc=="r" and tanquer <= 5:
            print("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
        elif tipc== "r":
            if tanquer - cantc < 0:
                print("No se puede vender esa cantidad de gasolina regular porque sobrepasa el limite del tanque")
            else:
                tanquer = tanquer - cantc
                print("El total a pagar es: ", cantc * precventr)

        if tipc=="s" and tanques <= 5:
            print("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
        elif tipc== "s":
            if tanques - cantc < 0:
                print("No se puede vender esa cantidad de gasolina super porque sobrepasa el limite del tanque")
            else:
                tanques = tanques - cantc
                print("El total a pagar es: ", cantc * precvents)
        
        if tipc=="d" and tanqued <= 5:
            print("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
        elif tipc== "d":
            if tanqued - cantc < 0:
                print("No se puede vender esa cantidad de gasolina diesel porque sobrepasa el limite del tanque")
            else:
                tanqued = tanqued - cantc
                print("El total a pagar es: ", cantc * precventd)

        
        
       