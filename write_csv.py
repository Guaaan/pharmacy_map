import logging
import pandas as pd
from time import sleep
import requests
import json


def get_pharmacy_data(pharmacy_im, lt, lg, tp):

    url = "https://seremienlinea.minsal.cl/asdigital/mfarmacias/mapa.php"

    payload = f"im={pharmacy_im}&lt=-{lt}&lg=-{lg}&tp={tp}&func=local&fecha=0"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-AR,es-419;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'edf2b787d71200dafd83c3d361162bdf1c672cd1=b9rbs0br0t3qhmk0ebuuus5gt4; _gid=GA1.2.197336248.1686750674; _hjSessionUser_1899797=eyJpZCI6ImMyMDJhNmVlLTg5NjctNTBkNi05MmU2LWU2NzliNzVkNmVkYiIsImNyZWF0ZWQiOjE2ODY3NTA2NzQxNzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.142835544.1686750135; _ga_K0XLHJL8YF=GS1.1.1686750674.1.1.1686750979.0.0.0; _ga_S5W7DTQL54=GS1.1.1686750134.1.1.1686751898.0.0.0',
        'Origin': 'https://seremienlinea.minsal.cl',
        'Referer': 'https://seremienlinea.minsal.cl/asdigital/index.php?mfarmacias',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()  # Verificar si la respuesta tiene un estado de error
        print(response.status_code)
        if response.ok and response.text is not None:
            json_data = response.json()
            if json_data is not None and 'respuesta' in json_data and 'local' in json_data['respuesta']:
                return json_data
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
    except requests.exceptions.Timeout:
        print("Tiempo de espera agotado. Intenta nuevamente más tarde.")
    
    return None


# Lista de farmacias
# get_pharmacies()
locales = []
# Leer el archivo JSON y almacenar su contenido en la variable farmacias
with open("farmacias.json", "r") as file:
    farmacias = json.load(file)
    for f in farmacias:
        locales.append(f)
file.close()

# Nombre del archivo CSV de salida
archivo_csv = "datos_farmacias_total.csv"
archivo_json = "datos_farmacias_total.json"

# Realizar el bucle for y escribir los resultados en el archivo CSV

# Configurar el log
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Crear una lista para almacenar los datos de cada farmacia
datos_farmacias = []

# Contador de errores
error_count = 0
total_locales = len(locales)
# for frm in farmacias["respuesta"]["locales"]:
for i, frm in enumerate(locales):
    try:
        im = frm["im"]
        lt = frm["lt"]
        lg = frm["lg"]
        tp = frm["tp"]
        porcentaje = (i + 1) / total_locales * 100

        # Mostrar el porcentaje
        print("Porcentaje completado: {:.2f}%".format(porcentaje))
        # Obtener los datos de la farmacia
        if im is not None and lt is not None and lg is not None and tp is not None:
            pharmacy_data = get_pharmacy_data(im, lt, lg, tp)
            current = pharmacy_data
        else:
            pass
        if current is not None and 'respuesta' in current and 'local' in current['respuesta']:
            respuesta = current['respuesta']['local']

            # Extraer los datos relevantes
            im = respuesta['im']
            nm = respuesta['nm']
            dr = respuesta['dr']
            rg = respuesta['rg']
            cm = respuesta['cm']
            tl = respuesta['tl']
            at = respuesta['at']
            horario = {}
            if current['respuesta']['horario']:
                horario = current['respuesta']['horario']
            else:
                horario={}
            
            # print([im, nm, dr, rg, cm, tl, at, horario])
            # Agregar los datos a la lista
            try:
                datos_farmacias.append([im, nm, dr, rg, cm, tl, at, horario])
            except KeyError as e:
                error_count += 1
                logging.error(
                    "Error en farmacia con IM {}: {}".format(im, str(e)))
        else:
            pass

    except KeyError as e:
        error_count += 1
        logging.error("Error en farmacia con IM {}: {}".format(im, str(e)))

# Crear un DataFrame a partir de la lista de datos
data = pd.DataFrame(
    datos_farmacias, columns=["IM", "NM", "DR", "RG", "CM", "TL", "AT", "Horario"])

# Escribir el DataFrame en un archivo CSV
data.to_csv(archivo_csv, index=False)
with open(archivo_json, "w") as file:
    json.dump(datos_farmacias, file)

# Registrar el número de errores
logging.info("Número total de errores: {}".format(error_count))
print(error_count)
