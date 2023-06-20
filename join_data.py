import pandas as pd
import json

# Leer el archivo CSV
def read_csv(filename):
    data = pd.read_csv(filename)
    json_data = data.to_dict(orient='records')
    return json_data

# Leer el archivo JSON
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


# Archivos de entrada
csv_filename = 'datos_farmacias_total.csv'
json_filename = 'comunas.json'

# Archivo de salida
output_filename = 'farmacias_con_comunas.csv'

# Leer los datos del archivo CSV
csv_data = read_csv(csv_filename)

# Leer los datos del archivo JSON
json_data = read_json(json_filename)

for c in csv_data:
    cm_value = c['CM']
    if pd.notna(cm_value):
        cm_value = int(cm_value)
        matching_comuna = next((j for j in json_data if j['comuna_id'] == cm_value), None)
        if matching_comuna:
            c['comuna'] = matching_comuna['nombre']
        else:
            c['comuna'] = ""
    else:
        c['comuna'] = ""

# Crear un DataFrame con los datos combinados
combined_data = pd.DataFrame(csv_data)

# Escribir los datos combinados en un nuevo archivo CSV
combined_data.to_csv(output_filename, index=False)

print(f"Archivo CSV combinado creado exitosamente: {output_filename}")
