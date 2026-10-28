codigo_p = ["P001", "P002", "P004"]
nombre_P = ["Monitor", "Teclado", "Mouse", "Impresora"]
precio_P = [300, 70, 40, 800]
cantidad_P = [5, 15, 15, 5]

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

            try:
                opcion=int(input("¿Qué operación desea realizar? (1-7)"))
                
                
                if opcion == 1:
                    print("Seleccionó la opción de Inventario")
                    print("El inventario actual es: ")
                    listar_productos()
                
                elif opcion == 2:
                    print("Seleccionó la opción de Agregar Producto.")
                elif opcion == 3:
                     print("Seleccionó la opción de Buscar Producto.")

                elif opcion == 4:
                    print("Seleccionó la opción de Eliminar Producto.")

                elif opcion == 5:
                    print("Seleccionó la opción de Cálculos Estadísticos.")

                elif opcion == 6:
                    print("Seleccionó la opción de Ordenar Productos.")            

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
        if control2 <= control:
            control2 += 1
            print ("Credenciales incorrectas")
            print ("Intentos: ",control2," de: ", control, " Intente de nuevo: ")
if control2 >= control:
    print ("Intentos: ", control2," de: ",control, " Acceso denegado")
    inicio = False
