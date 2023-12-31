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

comunas = json_data


for c in csv_data:
    for j in json_data:
        try: 
            if pd.isna(c['CM']) is not True:
                id_json = int(j['comuna_id'])
                id_csv = int(c['CM'])
                if id_json == id_csv:
                    c['comuna'] = j['nombre']
            else: 
                c['comuna'] = 0
        except ValueError as e:
            print(j['comuna_id'])
            print(c['CM'])
            print(e)
# print(csv_data)
combined_data = pd.DataFrame(csv_data)

# Escribir los datos combinados en un nuevo archivo CSV
combined_data.to_csv(output_filename, index=False)

print(f"Archivo CSV combinado creado exitosamente: {output_filename}")
