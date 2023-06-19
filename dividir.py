import json

def divide_json_file(json_file, num_files):
    with open(json_file, 'r') as file:
        data = json.load(file)

    total_results = len(data)
    results_per_file = total_results // num_files

    for i in range(num_files):
        start_index = i * results_per_file
        end_index = (i + 1) * results_per_file if i < num_files - 1 else total_results

        output_data = data[start_index:end_index]

        output_file = f"output_{i}.json"
        with open(output_file, 'w') as outfile:
            json.dump(output_data, outfile)

        print(f"Archivo {output_file} creado con éxito.")

# Ejemplo de uso
json_file = "farmacias.json"
num_files = 32

divide_json_file(json_file, num_files)