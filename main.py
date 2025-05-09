from estudiantes.registro import cargar_estudiantes, mostrar_estudiantes, calcular_promedio

def main():
    estudiantes = cargar_estudiantes('estudiantes.csv')  # Cargar estudiantes desde el archivo CSV
    mostrar_estudiantes(estudiantes)  # Mostrar la lista de estudiantes
    promedio = calcular_promedio(estudiantes)  # Calcular el promedio de notas
    print(f"Promedio de notas: {promedio:.2f}")  # Mostrar el promedio de notas

    if __name__ == "__main__":
        main()
 