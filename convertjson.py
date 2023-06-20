import json
import csv

def convertir_json_a_csv(archivo_json, archivo_csv):
    # Abrir el archivo JSON y cargar los datos
    with open(archivo_json, 'r') as json_file:
        datos_json = json.load(json_file)
    
    # Obtener la lista de claves para las columnas del CSV
    claves = list(datos_json[0].keys())
    
    # Abrir el archivo CSV en modo escritura
    with open(archivo_csv, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=claves)
        
        # Escribir la primera fila con los nombres de las columnas
        writer.writeheader()
        
        # Escribir los datos en filas sucesivas
        for fila in datos_json:
            writer.writerow(fila)

    print("La conversión de JSON a CSV se ha completado con éxito.")

# Ruta del archivo JSON de entrada
archivo_json = 'comunas.json'

# Ruta del archivo CSV de salida
archivo_csv = 'comunassss.csv'

# Llamar a la función para convertir el archivo JSON a CSV
convertir_json_a_csv(archivo_json, archivo_csv)
