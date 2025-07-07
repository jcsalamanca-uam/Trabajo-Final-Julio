from Modulos.Generador_Datos import generar_usuarios
from Modulos.Buscador import buscar_sospechosos

def menu():
    while True:
        print("\n===============================")
        print("DETECTOR DE USUARIOS SOSPECHOSOS")
        print("===============================")
        print("1. Generar nuevos usuarios")
        print("2. Buscar usuarios sospechosos")
        print("3. Salir")
        print("===============================")

        opcion = input("Elige una opción (1-3): ")

        if opcion == '1':
            try:
                cantidad = int(input("¿Cuántos usuarios deseas generar?: "))
                generar_usuarios(cantidad)
                print(f"Se generaron {cantidad} usuarios y se guardaron en 'usuarios.csv'")
            except ValueError:
                print("Por favor ingresa un número válido.")

        elif opcion == '2':
            print("Buscando usuarios sospechosos...\n")
            sospechosos = buscar_sospechosos()
            
            exportar = input("\n¿Deseas guardar los sospechosos en 'sospechosos.csv'? (s/n): ").lower()
            if exportar == 's':
                guardar_sospechosos(sospechosos)
                print("Archivo 'sospechosos.csv' guardado correctamente.")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta otra vez.")

def guardar_sospechosos(sospechosos):
    
    import csv
    with open('sospechosos.csv', 'w', newline='', encoding='utf-8') as file:
        campos = ['ID', 'Nombre', 'Email', 'Publicaciones_dia', 'Comentario_reciente']
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        for usuario in sospechosos:
            writer.writerow(usuario)

# Ejecutar el programa
if __name__ == '__main__':
    menu()
