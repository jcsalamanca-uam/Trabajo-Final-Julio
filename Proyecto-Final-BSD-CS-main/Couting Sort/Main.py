from Modulos.Generar_Datos import generar_datos, guardar_en_csv
from Modulos.Ordenamiento import counting_sort_por_edad, cargar_desde_csv
import time

def comparar_algoritmos(personas):
    print("Ordenando con Counting Sort...")
    inicio = time.time()
    resultado_counting = counting_sort_por_edad(personas)
    tiempo_counting = time.time() - inicio
    print(f"Counting Sort: {tiempo_counting:.4f} segundos")

    print("⚙ Ordenando con sorted() (TimSort)...")
    inicio = time.time()
    resultado_sorted = sorted(personas, key=lambda x: x[1])
    tiempo_sorted = time.time() - inicio
    print(f"sorted(): {tiempo_sorted:.4f} segundos")

    diferencia = abs(tiempo_sorted - tiempo_counting)
    print(f"\nDiferencia de tiempo: {diferencia:.4f} segundos")
  
# ---------- 5. Main con medición de tiempo ----------
def main():
    while True:
        print("\n" + "="*40)
        print("      MENÚ - ORDENAMIENTO POR EDAD")
        print("="*40)
        print("1. Generar datos y guardarlos en CSV")
        print("2. Cargar datos, ordenarlos y guardar resultado")
        print("3. Comparar counting sort vs Sorted")
        print("4. Salir")
        print("="*40)
        opcion = input("Seleccione una opción (1/2/3/4/): ")

        if opcion == "1":
            cantidad = int(input("¿Cuántos registros deseas generar? (ej. 100000): "))
            print(" Generando datos...")
            inicio = time.time()
            personas = generar_datos(cantidad)
            guardar_en_csv(personas)
            fin = time.time()
            print(f"Datos generados y guardados en 'personas.csv' ({fin - inicio:.2f} s)")
        
        elif opcion == "2":
            print("Cargando datos desde 'personas.csv'...")
            personas = cargar_desde_csv()
            if not personas:
                continue
            print("Ordenando por edad...")
            inicio = time.time()
            personas_ordenadas = counting_sort_por_edad(personas)
            fin = time.time()
            guardar_en_csv(personas_ordenadas, nombre_archivo="personas_ordenadas.csv")
            print(f"Ordenamiento completo en {fin - inicio:.2f} s. Guardado en 'personas_ordenadas.csv'.")

        elif opcion == "3":
            print("Cargando datos desde 'personas.csv'...")
            personas = cargar_desde_csv()
            if not personas:
                continue
            comparar_algoritmos(personas)
            
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
