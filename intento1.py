
# INTEGRANTE 3: Cálculos, Burbuja y Reporte


# Tus datos base independientes
codigo_p = ["P001", "P002", "P003", "P004"]
nombre_P = ["Monitor", "Teclado", "Mouse", "Impresora"]
precio_P = [300.0, 70.0, 40.0, 800.0]
cantidad_P = [5, 15, 15, 5]



# 1. MOSTRAR INVENTARIO 

def listar_inventario():
    print(f"{'CÓDIGO':<10} | {'PRODUCTO':<15} | {'PRECIO ($)':<12} | {'CANTIDAD':<10}")
    print("-" * 55)
    for i in range(len(codigo_p)):
        print(f"{codigo_p[i]:<10} | {nombre_P[i]:<15} | ${precio_P[i]:<11.2f} | {cantidad_P[i]:<10}")
    print("-" * 55)



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
        
    print("\n--- ORDENAR PRODUCTOS (MÉTODO BURBUJA) ---")
    print("1. Ordenar por Precio (Menor a Mayor)")
    print("2. Ordenar por Precio (Mayor a Menor)")
    print("3. Ordenar alfabéticamente por Nombre (A - Z)")
    
    opcion = input("Seleccione una opción de ordenamiento (1-3): ")
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


# PRUEBA AL EJECUTAT

if __name__ == "__main__":
    print(">>> 1. MOSTRAR INVENTARIO ORIGINAL <<<")
    listar_inventario()
    
    print("\n>>> 2. PROBANDO CÁLCULOS ESTADÍSTICOS <<<")
    calculos_E()
    
    print("\n>>> 3. PROBANDO ORDENAMIENTO BURBUJA <<<")
    ordenar_P()