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
trabajadorjv = 1
trabajadorjn = 1
salariojd = 14
salariojv = 14.50
salariojn = 15.50
ingresostotales = 0

while True: 
    totaltrabajadores = trabajadorjd + trabajadorjv + trabajadorjn
    print("Bienvenido a la gasolinera Jaguar")
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
                if cantr < 0:
                 print (" No se puede agregar una cantidad negativa de gasolina regular")
                else:
                    tanquer = tanquer + cantr
            cants = int(input("Ingrese la cantidad de gasolina super que desea agregar: "))
            if tanques + cants > maxtanque:
                print("No se puede agregar esa cantidad de gasolina super porque sobrepasa el limite del tanque")
            else:
                if cants < 0:
                    print (" No se puede agregar una cantidad negativa de gasolina super")
                else:
                    tanques = tanques + cants
            cantd = int(input("Ingrese la cantidad de gasolina diesel que desea agregar: "))
            if tanqued + cantd > maxtanque:
                print("No se puede agregar esa cantidad de gasolina diesel porque sobrepasa el limite del tanque")
            else:
                if cantd < 0:
                    print (" No se puede agregar una cantidad negativa de gasolina diesel")
                else:
                    tanqued = tanqued + cantd

    elif opcion == 2:
        venta = False
        totalpago = 0
        print ("El deposito de gasolina regular tiene ", tanquer, " galones y cuesta ", tanquer * precventr, "Quetzales" )
        print ("El deposito de gasolina super tiene ", tanques, " galones y cuesta ", tanques * precvents, "Quetzales" )
        print ("El deposito de gasolina diesel tiene ", tanqued, " galones y cuesta ", tanqued * precventd, "Quetzales" )
        dineroogalones = input ("Seleccione si pagar por equivalente en efectivo o por cantidad de galones (d/g): ")
        dineroogalones.lower()
        if dineroogalones == "g":
            tipc = input("Ingrese el tipo de combustible que desea comprar (r/s/d): ")
            tipc.lower()
            cantc = int(input("Ingrese la cantidad de combustible que desea comprar: "))
            if tipc=="r" and tanquer <= 5:
                print("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
            elif tipc== "r":
                if tanquer - cantc < 0:
                    print("No se puede vender esa cantidad de gasolina regular porque sobrepasa el limite del tanque")
                else:
                    tanquer = tanquer - cantc
                    totalpago=cantc * precventr
                    print("El total a pagar es: ", totalpago)
                    venta=True
                    ingresostotales += totalpago
            if tipc=="s" and tanques <= 5:
                print("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
            elif tipc == "s":
                if tanques - cantc < 0:
                    print("No se puede vender esa cantidad de gasolina super porque sobrepasa el limite del tanque")
                else:
                    tanques = tanques - cantc
                    totalpago=cantc * precvents
                    print("El total a pagar es: ", totalpago)
                    venta=True
                    ingresostotales += totalpago                      
            if tipc=="d" and tanqued <= 5:
                print("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
            elif tipc== "d":
                if tanqued - cantc < 0:
                    print("No se puede vender esa cantidad de gasolina diesel porque sobrepasa el limite del tanque")
                else:
                    tanqued = tanqued - cantc
                    totalpago=cantc * precventd
                    print("El total a pagar es: ", totalpago)
                    venta=True
                    ingresostotales += totalpago
        elif dineroogalones == "d":
            tipc = input("Ingrese el tipo de combustible que desea comprar (r/s/d): ")
            tipc.lower()
            if tipc == "r":
                comprdr = float(input("Ingrese la cantidad de dinero que desea comprar de gasolina regular: "))
                galonsvntr = comprdr / precventr
                if galonsvntr <= 5:
                    print ("Se desea comprar ", galonsvntr, "galones de gasolina regular y" )
                    print ("No se puede realizar la compra porque el deposito es igual o menor a 5 galones")
                if tanquer - galonsvntr < 0:
                    print("No se puede vender esa cantidad de gasolina regular porque sobrepasa el limite del tanque")
                else:
                    totalpago = comprdr
                    cantc = galonsvntr
                    tanquer -= galonsvntr                    
                    print ("Usted puede comprar ", galonsvntr, " galones de gasolina regular")
                    venta=True
                    ingresostotales += comprdr                    
            elif tipc == "s":
                comprds = float (input("Ingrese la cantidad de dinero que desea comprar de gasolina super: "))
                galonsvnts = comprds / precvents
                if galonsvnts <= 5:
                    print ("Se desea comprar ", galonsvnts, "galones de gasolina super y" )
                    print ("No se puede comprar menos de 5 galones de gasolina super")
                if tanques - galonsvnts < 0:
                    print ("No se puede vender esa cantidad de gasolina super porque sobrepasa el limite del tanque")
                else:
                    totalpago = comprds
                    cantc = galonsvnts
                    tanques -= galonsvnts
                    print ("Usted puede comprar ", galonsvnts, " galones de gasolina super")
                    venta=True
                    ingresostotales += comprds
            elif tipc == "d":
                comprdd = float (input("Ingrese la cantidad de galones que desea comprar de gasolina diesel: "))
                galonsvntd = comprdd / precventd
                if galonsvntd <= 5:
                    print ("Se desea comprar ", galonsvntd, "galones de gasolina diesel y" )
                    print ("No se puede comprar menos de 5 galones de gasolina diesel")
                if tanqued - galonsvntd < 0: 
                    print ("No se puede vender esa cantidad de gasolina diesel porque sobrepasa el limite del tanque")
                else:
                    totalpago = comprdd
                    cantc = galonsvntd
                    tanqued -= galonsvntd
                    print ("Usted puede comprar ", galonsvntd, " galones de gasolina diesel")
                    venta=True
                    ingresostotales += comprdd
            else:
             print("Opcion no valida")
        else: 
            print("Opcion no valida")

        if venta==True:
            nombre = input("Ingrese el nombre del cliente: ")
            nit = input("Ingrese el NIT del cliente: ")
            while True:
                bomba = int (input("Ingrese la bomba utilizada, 1, 2, 3 o 4: "))
                if bomba > 4:
                    print ("Por favor ingrese una bomba valida")
                else:
                 print("------------Datos de la venta-----------")
                 print("Nombre del cliente: ", nombre)
                 print("NIT del cliente: ", nit)
                 print("Bomba utilizada: ", bomba)
                 print("Cantidad de combustible: ", cantc)
                 print("Total a pagar: ", totalpago)
                 print ("")
                 print ("")
                 break
    elif opcion == 3:
        print("Gestión de turnos")
        print ("El total de trabajadores es de: ", totaltrabajadores)
        print("El numero de trabajadores de la jornada diurna es de: ", trabajadorjd)
        print("El numero de trabajadores de la jornada verspertina es de: ", trabajadorjv)
        print("El numero de trabajadores de la jornada nocturna es de: ", trabajadorjn)
        elecmodjornada =input ("¿Desea modificar la cantidad de trabajadores en las diferentes jornadas? (s/n) ")
        elecmodjornada.lower()
        if elecmodjornada =="s":
            agregaroquitar = input ("¿Desea agregar o quitar trabajadores? (a/q) ")
            agregaroquitar.lower()
            if agregaroquitar == "a":
                Jornada =input("¿A que jornada desea agregar trabajadores? (d/v/n) ")
                Jornada.lower()
                if Jornada == "d":
                    sumtrabajadores = int(input("¿Cuantos trabajadores desea agregar a la jornada diurna? "))
                    trabajadorjd += sumtrabajadores
                elif Jornada == "v":
                    sumtrabajadores = int(input("¿Cuantos trabajadores desea agregar a la jornada vespertina? "))
                    trabajadorjv += sumtrabajadores
                elif Jornada == "n":
                    sumtrabajadores = int(input("¿Cuantos trabajadores desea agregar a la jornada nocturna? "))
                    trabajadorjn += sumtrabajadores
                else:
                   print("Opcion no valida")
            elif agregaroquitar == "q":
                Jornada =input("¿A que jornada desea quitar trabajadores? (d/v/n) ")
                Jornada.lower()    
                if Jornada == "d":  
                    restatrabajadores = int(input("¿Cuantos trabajadores desea quitar a la jornada diurna? "))
                    if trabajadorjd - restatrabajadores < 0:
                        print("No se puede quitar esa cantidad de trabajadores a la jornada diurna")
                    elif trabajadorjd - restatrabajadores >= 0: 
                        trabajadorjd -= restatrabajadores
                elif Jornada == "v":
                    restatrabajadores = int(input("¿Cuantos trabajadores desea quitar a la jornada vespertina? "))
                    if trabajadorjv - restatrabajadores < 0:
                        print ("No se puede quitar esta cantidad de trabajadores a la jornada vespertina")
                    elif trabajadorjv - restatrabajadores >= 0:
                        trabajadorjv -= restatrabajadores
                elif Jornada == "n":
                    restatrabajadores = int(input("¿Cuantos trabajadores desea quitar a la jornada nocturna? "))
                    if trabajadorjn - restatrabajadores < 0:
                        print ("No se puede quitar esta cantidad de trabajadores a la jornada nocturna")
                    elif trabajadorjn - restatrabajadores >= 0:
                        trabajadorjn -= restatrabajadores
                else:
                   print("Opcion no valida")
    elif opcion == 4:
        materiaprima = (tanquer*costalmacr) + (tanques*costalmacs) + (tanqued*costalmacd)
        manodeobra = (trabajadorjd * salariojd) + (trabajadorjv * salariojv) + (trabajadorjn * salariojn)
        print ("Ingresos totales:         Q",ingresostotales)
        print ("Materia prima: ")
        print ("Costo combustible regular:         Q", tanquer * costalmacr)
        print ("Costo combustible super:         Q",tanques * costalmacs)
        print ("Costo combustible diesel:         Q",tanqued * costalmacd)
        print ("Mano de obra: ")
        print ("Salario de jornada diurna:         Q", trabajadorjd * salariojd)
        print ("Salario de jornada vespertina:         Q", trabajadorjv * salariojv)
        print ("Salario de jornada nocturna:         Q", trabajadorjn * salariojn)
        print ("Costos fijos:          Q10")
        print ( "Utilidad bruta:         Q", ingresostotales - materiaprima - manodeobra - 10)
    elif opcion == 5:
        print("Gracias por utilizar el sistema")
        break
    
    elif opcion < 1 or opcion > 5:
        print("Opcion no valida")
        print("Por favor ingrese una opcion valida")