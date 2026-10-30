# INTEGRANTE 2 - DAVID MÉRIDA
# MODULO DE GESTIÓN Y VALIDACIÓN

#REGISTRAR NUEVO PRODUCTO PIDIENDO LOS DATOS AL USUARIO 
def registrar_producto():
    print ("REGISTRAR NUEVO PRODUCTO")

    codigo = input("Ingrese el código del producto: ")
    if not codigo:
        print("El código no puede estar vacío.")
        return 
    if codigo in codigo_p:
        print("El código ya existe. No se puede registrar el producto.")
        return
    nombre = input("Ingrese el nombre del producto: ")
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    #VALIDACIÓN DE PRECIO CON TRY-EXCEPT (TRY: INTENTAR Y COMPROBAR SI ES CORRECTO  .....   EXCEPT:SI OCURRE EL ERROR PASA x)
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Precio inválido. Por favor, ingrese un número válido.")

    #VALIDACION DE CANTIDAD CON TRY-EXCEPT
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Cantidad inválida. Por favor, ingrese un número entero válido.")

    #REGISTRAR EL PRODUCTO USANDO .APPEND
    codigo_p.append(codigo)
    nombre_p.append(nombre)
    precio_p.append(precio)
    cantidad_p.append(cantidad)
    print("Producto registrado con éxito.")

#LOCALIZAR UN PRODUCTO EN ESPECÍFICO POR SU COIGO O NOMBRE 
def buscar_P():
    print("BUSCAR PRODUCTO")
     
     if not codigo_p:
        print("No hay productos registrados.")
        return
    criterio = input("Ingrese el código o nombre del producto a buscar: ")

    encontrado = False
    for i in range(len(codigo_p)):
        #BUSQUEDA DE PRODUCTO POR CODIGO O NOMBRE (SE USA LOWER PARA IGNORAR MAYUSCULAS Y MINUSCULAS)
        if codigo_p[i] == criterio or nombre_p[i].lower() == criterio.lower():
            print(f"Producto encontrado: Código: {codigo_p[i]}, Nombre: {nombre_p[i]}, Precio: {precio_p[i]}, Cantidad: {cantidad_p[i]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.")

#BORRAR UN REGISTRO DE LAS LISTAS
def eliminar_P():
    print("ELIMINAR PRODUCTO")
    if not codigo_p:
        print("No hay productos registrados.")
        return
    
    codigo_a_eliminar = input("Ingrese el código del producto a eliminar: ")
    if codigo_a_eliminar in codigo_p:
        idx = codigo_p.index(codigo_a_eliminar)
        confirmacion = input(f"¿Está seguro de que desea eliminar el producto? (s/n): ")
        if confirmacion == s or confirmacion == S or confirmacion == si or confirmacion == SI:
            codigo_p.pop(idx)
            nombre_p.pop(idx)
            precio_p.pop(idx)
            cantidad_p.pop(idx)
            print("Producto eliminado con éxito.")
        else: 
            print("Eliminación cancelada.")