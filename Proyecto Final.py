codigo_p = ["P001", "P002", "P003","P004"]
nombre_P = ["Monitor", "Teclado", "Mouse", "Impresora"]
precio_P = [300, 70, 40, 800]
cantidad_P = [5, 15, 15, 5]

def listar_inventario():
    print("=" * 55)
    print(f"{'CÓDIGO':<10} | {'PRODUCTO':<15} | {'PRECIO ($)':<12} | {'CANTIDAD':<10}")
    print("-" * 55)
    for i in range(len(codigo_p)):
        print(f"{codigo_p[i]:<10} | {nombre_P[i]:<15} | ${precio_P[i]:<11.2f} | {cantidad_P[i]:<10}")
    print("-" * 55)
    print("=" * 55)

# 2. CÁLCULOS ESTADÍSTICOS 
def calculos_E():
    if not codigo_p:
        print("El inventario está vacío.")
        return
        
    total_distintos = len(codigo_p)
    cantidad_total = sum(cantidad_P)
    
    # Valor total del inventario (Precio * Cantidad)
    valor_total = sum(precio_P[i] * cantidad_P[i] for i in range(total_distintos))
    
    # Precio promedio
    precio_promedio = sum(precio_P) / total_distintos
    
    # Identificar máximo y mínimo
    max_precio = max(precio_P)
    min_precio = min(precio_P)
    
    idx_max = precio_P.index(max_precio)
    idx_min = precio_P.index(min_precio)
    
    print("=" * 55)
    print(f"{'CÁLCULOS ESTADÍSTICOS DEL INVENTARIO':^55}")
    print("=" * 55)
    print(f"• Productos distintos en catálogo : {total_distintos}")
    print(f"• Total de unidades en stock    : {cantidad_total}")
    print(f"• Valor total del inventario    : ${valor_total:.2f}")
    print(f"• Precio promedio por producto  : ${precio_promedio:.2f}")
    print(f"• Producto más caro             : {nombre_P[idx_max]} (${max_precio:.2f})")
    print(f"• Producto más barato           : {nombre_P[idx_min]} (${min_precio:.2f})")
    print("=" * 40)
# 3. ALGORITNO DE BURBUJA 

def ordenar_P():
    if not codigo_p:
        print("El inventario está vacío.")
        return
    print("=" * 40)    
    print("\n---ORDENAR PRODUCTOS (MÉTODO BURBUJA)---")
    print("=" * 40)
    print("1. Ordenar por Precio (Menor a Mayor)")
    print("2. Ordenar por Precio (Mayor a Menor)")
    print("3. Ordenar alfabéticamente por Nombre (A - Z)")
    print("")
    opcion = input("Seleccione una opción de ordenamiento (1-3): ")
    print("=" * 40  )

    n = len(codigo_p)
    
    # Algoritmo de Burbuja manual
    for i in range(n):
        for j in range(0, n - i - 1):
            if opcion == '1':
                condicion = precio_P[j] > precio_P[j+1]
            elif opcion == '2':
                condicion = precio_P[j] < precio_P[j+1]
            elif opcion == '3':
                condicion = nombre_P[j] > nombre_P[j+1]
            else:
                print("Opción inválida.")
                return
                
            if condicion:
                # Intercambio simultáneo para mantener el orden de las listas
                precio_P[j], precio_P[j+1] = precio_P[j+1], precio_P[j]
                codigo_p[j], codigo_p[j+1] = codigo_p[j+1], codigo_p[j]
                nombre_P[j], nombre_P[j+1] = nombre_P[j+1], nombre_P[j]
                cantidad_P[j], cantidad_P[j+1] = cantidad_P[j+1], cantidad_P[j]
                
    print("\n¡Productos ordenados exitosamente con Burbuja!")
    listar_inventario()

def registrar_producto():
    print("=" * 40)
    print ("      REGISTRAR NUEVO PRODUCTO")
    print("=" * 40)
    codigo = input("\n Ingrese el código del producto: ")
    if not codigo:
        print("El código no puede estar vacío.")
        print("=" * 40)
        return 
    if codigo in codigo_p:
        print("El código ya existe. No se puede registrar el producto.")
        print("=" * 40)
        return
    nombre = input("Ingrese el nombre del producto: ")
    if not nombre:
        print("El nombre no puede estar vacío.")
        print("=" * 40)
        return

   
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Precio inválido. Por favor, ingrese un valor numérico válido.")

   
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Cantidad inválida. Por favor, ingrese un número entero válido.")

    #REGISTRAR EL PRODUCTO 
    codigo_p.append(codigo)
    nombre_P.append(nombre)
    precio_P.append(precio)
    cantidad_P.append(cantidad)
    print("Producto registrado con éxito.")
    print("=" * 40)

def buscar_P():
    print("=" * 40)
    print("         BUSCAR PRODUCTO")
    print("=" * 40)
     
    if not codigo_p:
        print("\n No hay productos registrados.")
        print("=" * 40)
        return
    criterio = input("Ingrese el código o nombre del producto a buscar: ")

    encontrado = False
    for i in range(len(codigo_p)):
        #BUSQUEDA DE PRODUCTO POR CODIGO O NOMBRE 
        if codigo_p[i] == criterio or nombre_P[i].lower() == criterio.lower():
            print(f"\nProducto encontrado: Código: {codigo_p[i]}, Nombre: {nombre_P[i]}, Precio: {precio_P[i]}, Cantidad: {cantidad_P[i]}")
            encontrado = True
            print("=" * 40)
            break
    
    if not encontrado:
        print("\nProducto no encontrado.")
        print("=" * 40)

#BORRAR UN REGISTRO DE LAS LISTAS
def eliminar_P():
    print("=" * 40)
    print("        ELIMINAR PRODUCTO")
    print("=" * 40)
    if not codigo_p:
        print("\n No hay productos registrados.")
        print("=" * 40)
        return
    
    codigo_a_eliminar = input("Ingrese el código del producto a eliminar: ")
    if codigo_a_eliminar in codigo_p:
        idx = codigo_p.index(codigo_a_eliminar)
        confirmacion = input(f"¿Está seguro de que desea eliminar el producto? (s/n): ")
        if confirmacion == "s" or confirmacion == "S" or confirmacion == "si" or confirmacion == "SI":
            codigo_p.pop(idx)
            nombre_P.pop(idx)
            precio_P.pop(idx)
            cantidad_P.pop(idx)
            print("\n Producto eliminado con éxito.")
            print("=" * 40)
        else: 
            print("\n Eliminación cancelada.")
            print("=" * 40)


usuario_est = "admin"
contraseña_est = "Acces2610"
control = 3
control2 = 0
        
print("==================================")
print("        Sistema de gestión")
print("        Acceso Restringido")
print("==================================")

inicio = True     
while inicio ==True and control2 < control:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == usuario_est and contraseña == contraseña_est:
        print("Credenciales válidas. Acceso concedido.")
    
        while True:
            print("========================================")
            print("            Menú de Opciones")
            print("========================================")
            print("Inventario__________________________(1)")
            print("Agregar Producto____________________(2)")
            print("Busca Producto______________________(3)")
            print("Eliminar Producto___________________(4)")
            print("Cálculos Estadísticos_______________(5)")
            print("Ordenar Productos___________________(6)")
            print("Salir del Sistema___________________(7)")
            print("")

            try:
                opcion=int(input("¿Qué operación desea realizar? (1-7):  "))
                print("=======================================")
                
                
                if opcion == 1:
                    print("\nSeleccionó la opción de Inventario ")
                    print("\nEl inventario actual es: \n")
                    listar_inventario()

                    pass
                    print("Presione la tecla Enter para regresar al menú principal")
                
                elif opcion == 2:
                    print("\nSeleccionó la opción de Agregar Producto.")
                    registrar_producto()

                    pass
                    input("Presione la tecla Enter para regresar al menú principal")
                elif opcion == 3:
                     print("\nSeleccionó la opción de Buscar Producto.")
                     buscar_P()

                     pass
                     input("Presione la tecla Enter para regresar al menú principal")

                elif opcion == 4:
                    print("\nSeleccionó la opción de Eliminar Producto.")
                    eliminar_P()    
                    pass
                    input("Presione la tecla Enter para regresar al menú principal")

                elif opcion == 5:
                    print("\nSeleccionó la opción de Cálculos Estadísticos.")

                    calculos_E()

                    pass
                    input("Presione la tecla Enter para regresar al menú principal")

                elif opcion == 6:
                    print("\nSeleccionó la opción de Ordenar Productos.")            
                    ordenar_P()

                    pass
                    input("Presione la tecla Enter para regresar al menú principal")
                elif opcion == 7:
                    print("Cerrando el sistema")
                    print("¡Hasta pronto!")
                    inicio = False
                    break
                    
                else:
                    print("Error, ingrese una opción válida entre 1 y 7")
            except ValueError:
                        print("Error, debe ingresar un valor numérico válido.")
                        print("Ingrese un valor entre 1 y 7")
                        continue
    else:
            control2 += 1
            print ("Credenciales incorrectas")
            print ("Intentos: ",control2," de: ", control, " Intente de nuevo: ")
if control2 >= control:
    print ("Intentos: ", control2," de: ",control, " Acceso denegado")
    inicio = False
