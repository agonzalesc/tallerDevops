import csv
def cargar_estudiantes (ruta_archivo):
    estudiantes=[] #Lista donde se almacena los estudiantes validos 
    with open(estudiantes, mode='r') as archivo: #Abrir el archivo csv en modo lectura
        lector=csv.Dictreader(archivo) #Usar DictReader para leer el archivo csv como diccionario
        for fila in lector:
            try: 
                nombre=fila['nombre'] #Obtenemos el nombre del estudiante
                nota=float(fila['nota']) #Obtenemos la nota del estudiante
                if 0.0 <= nota <= 5.0: #Validamos que la nota este entre 0 y 5
                    estudiantes.append({'nombre': nombre, 'nota': nota}) #Agregamos el estudiante a la lista
            except ValueError: #Si la nota no es un numero
                continue #Ignoramos el estudiante
    return estudiantes #Retornamos la lista de estudiantes validos

