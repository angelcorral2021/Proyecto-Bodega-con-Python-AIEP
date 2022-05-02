# Programa de Bodega con sistema de recaudación.

clientes = {}
opcion = 0
recaudacion = []
articulos_retirados = []
promocion = int(3)
aux_promocion = promocion-1
valor_retiro = 1000
contrasenia = '123456'
contc = 0

print('Bienvenido a la tienda de la sombra\nSeleccione una opción para continuar: \n1. Agregar Cliente(s)\n2. Ver Clientes\n3. Buscar Cliente\n4. Agregar Artículo(s)\n5. Retirar Artículo(s)\n6. Recaudación Total\n7. Opciones de Administrador \n8. Salir')
is_run = True
while is_run:
    
    opcion = input("MENÚ PRINCIPAL\nIngrese una opción: ")
    print('Menú Principal\n1. Agregar Cliente(s)\n2. Ver Clientes\n3. Buscar Cliente\n4. Agregar Artículo(s)\n5. Retirar Artículo(s)\n6. Recaudación Total\n7. Opciones de Administrador \n8. Salir')
    if opcion == '1':
        print('Menú 1. Agregar Cliente(s)\nIngrese el o los usuarios que desee, cuando termine ingrese [ok]:  ')
        play2 = True
        while play2:
            rut = input("Ingrese el rut del cliente: ")
            if rut == str('ok') or rut == str('OK'):
                play2 = False
            elif rut in clientes:
                    print("El cliente ya existe\nIntente de nuevo ...")
            else:
                    nombre = input("Ingrese el nombre del cliente: ")
                    clientes[rut] = {'nombre': nombre, 'articulos': []} # Aqui creamos la lista, con cada ingreso se crea una nueva lista o diccionario con clave del rut por eso no pueden ser 2 iguales

    elif opcion == '2':
        print('Menú 2. Ver Clientes:')
        for rut in clientes:
            print(f"Rut: {rut}")
            print(f"Nombre: {clientes[rut]['nombre']}")
            print('__________________________________________')
        for rut in clientes:
            contc = (len(clientes))
        print(f'Tenemos {contc} cliente(s) en los registros.')

    elif opcion == '3':
        rut = input('Menú 3. Buscar Cliente\nIngrese el rut del cliente: ')
        if rut in clientes:
            print(f"Rut: {rut}")
            print(f"Nombre: {clientes[rut]['nombre']}")
            print(f"Articulos: {clientes[rut]['articulos']}")
            contt = (len(clientes[rut]['articulos']))
            print(f'El cliente tiene {contt} artículos en nuestras existencias.')
            print('__________________________________________')
        else:
            print("Cliente no registrado")

    elif opcion == '4':
        rut = input('Menú 4. Agregar Artículo(s)\nIngrese el rut del cliente: ')
        if rut in clientes:
            play = True
            while(play):
                articulo = input("Escriba el(los) artículo(s) en cada linea y ENTER, cuando termine escriba [ok] y ENTER: ")
                articulo = articulo.lower()
                clientes[rut]['articulos'].append(articulo)
                if articulo == str('ok' or 'OK' or 'oK' or 'Ok'): # Lo siento profe le fallamos jajajaja no funciono el lower
                    clientes[rut]['articulos'].remove(articulo)
                    play = False
        else: 
            print("Cliente no registrado")

    elif opcion == '5':
        print(f'Menú 5. Retirar Artículo(s)\nExiste una promoción, ¡retire {promocion} y pague {aux_promocion} !')
        corte = int(input('Cuantos artículos desea retirar: '))
        contador = corte
        recaudacion.append(((int(corte/promocion)*-1) + corte) * valor_retiro)
        rut = input('Ingrese su rut: ')
        if rut in clientes:
            while contador > 0 :
                print(clientes[rut]['articulos'])
                articulolw = input("Ingrese el artículo que desea quitar en cada linea y ENTER: ")
                clientes[rut]['articulos'].remove(articulolw.lower())
                contador -= 1
            print('El total a pagar es de $', ((int(corte/promocion)*-1) + corte) * valor_retiro)
        else:
            recaudacion.remove(((int(corte / promocion) * -1) + corte) * valor_retiro)
            print("Cliente no registrado")
    elif opcion == '6':

        print(f'Menú 6. Recaudación\nTotal Recaudado $ {sum(recaudacion)}.- CLP')

    elif opcion == '7':
        
        confirm = input('Ingrese contraseña de administrador: ')
        
        if contrasenia != confirm:
            print("Contraseña invalida")
            is_run2 = False
        elif contrasenia == confirm:
            print(f'Menú 7. Administrativo')
            print('1. Cambiar de precio de retiro\n2. Cambiar promoción\n3. Cambiar contraseña\n4. Salir a Menú Principal')
            opcion_adm = input("MENÚ ADMINISTRADOR\nIngrese opcion: ")
            
            if opcion_adm == '1':
                print(f'El precio actual del retiro es de: $ {valor_retiro}')
                valor_retiro = input('Ingrese el nuevo precio: ')
            elif opcion_adm == '2':
                print(f"La promoción actual es de llevar {promocion} y pagar {aux_promocion} ")
                promocion = input("Ingrese por cuantos artículos los clientes dejarán de pagar uno gratis : ")
            elif opcion_adm == '3':
                contrasenia = input("Ingrese nueva contraseña: ")

            elif opcion_adm == str():
                print('1. Cambiar de precio de retiro\n2. Cambiar promoción\n3. Cambiar contraseña\n4. Salir a Menú Principal')
                opcion_adm = input("MENÚ ADMINISTRADOR\nIngrese opcion: ")

            elif opcion_adm == '4':
                print('Bienvenido a la tienda de la sombra\nSeleccione una opción para continuar: \n1. Agregar Cliente(s)\n2. Ver Clientes\n3. Buscar Cliente\n4. Agregar Artículo(s)\n5. Retirar Artículo(s)\n6. Recaudación Total\n7. Opciones de Administrador \n8. Salir')

    elif opcion == '8':
        print("Gracias por su visita\n¡Hasta Luego!")
        is_run = False
        break
    else:
        print("Opción invalida - Revise el menú para ver opciones disponibles ...")
        print('1. Agregar Cliente(s)\n2. Ver Clientes\n3. Buscar Cliente\n4. Agregar Artículo(s)\n5. Retirar Artículo(s)\n6. Recaudación Total\n7. Opciones de Administrador \n8. Salir')
        opcion = input("MENÚ PRINCIPAL\nIngrese una opción: ")