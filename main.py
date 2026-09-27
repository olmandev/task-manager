
print("Version en feature")
print("============================")
print("         TASK MANAGER       ")
print("============================")

nombre = "Olman"
edad = 22
lenguaje = "Python"

print(f"\nNombre: {nombre}")
print(f"Edad: {edad}")
print(f"Lenguaje: {lenguaje}")

mensaje = (
    "\nSelecciona una opción:"
    "\n1. Ver tareas"
    "\n2. Agregar tarea"
    "\n3. Eliminar tarea"
    "\n4. Salir\n\n"
)

tareas = []

while True:
    try:
        opcion = int(input(mensaje))
        if opcion == 1:
            if not tareas:
                print("\nNo hay tareas")
            else:
                for numero, tarea in enumerate(tareas, start=1):
                    print(numero,tarea)

        elif opcion == 2:
            tareas.append(input("\nEscribe la tarea: "))
            print("\nTarea agregada con éxito")

        elif opcion == 3:
            if not tareas:
                print("\nNo hay tareas para eliminar")
            else:
                for numero, tarea in enumerate(tareas, start=1):
                    print(numero, tarea)

                indice = int(input("\nEscribe el número de la tarea que quieres eliminar: "))

                if 1 <= indice <= len(tareas):
                    tarea_eliminada = tareas.pop(indice - 1)
                    print(f"\nTarea eliminada: {tarea_eliminada}")
                else:
                    print("\nLa tarea seleccionada no existe")
        elif opcion == 4:
            print("\nSaliendo...")
            break

        else:
            print("\nOpción inválida")

    except ValueError:
        print("\nDebes introducir un número entero")