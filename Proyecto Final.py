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
    print("=" * 55)
# 3. ALGORITNO DE BURBUJA 

def ordenar_P():
    if not codigo_p:
        print("El inventario está vacío.")
        return
    print("=" * 55)    
    print("\n--- ORDENAR PRODUCTOS (MÉTODO BURBUJA) ---")
    print("=" * 55)
    print("1. Ordenar por Precio (Menor a Mayor)")
    print("2. Ordenar por Precio (Mayor a Menor)")
    print("3. Ordenar alfabéticamente por Nombre (A - Z)")
    print("")
    opcion = input("Seleccione una opción de ordenamiento (1-3): ")
    print("=" * 55)

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
            print("=======================================")
            print("            Menú de Opciones")
            print("=======================================")
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
                    print("Presione la tecla espacio para regresar al menú principal")
                
                elif opcion == 2:
                    print("\nSeleccionó la opción de Agregar Producto.")
                    agregar_P()

                    pass
                    input("Presione la tecla espacio para regresar al menú principal")
                elif opcion == 3:
                     print("\nSeleccionó la opción de Buscar Producto.")
                     buscar_P()

                     pass
                     input("Presione la tecla espacio para regresar al menú principal")

                elif opcion == 4:
                    print("\nSeleccionó la opción de Eliminar Producto.")
                    eliminar_P()    
                    pass
                    input("Presione la tecla enter para regresar al menú principal")

                elif opcion == 5:
                    print("\nSeleccionó la opción de Cálculos Estadísticos.")

                    calculos_E()

                    pass
                    input("Presione la tecla enter para regresar al menú principal")

                elif opcion == 6:
                    print("\nSeleccionó la opción de Ordenar Productos.")            
                    ordenar_P()

                    pass
                    input("Presione la tecla enter para regresar al menú principal")
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
