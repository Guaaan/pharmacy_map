import requests
import json
from get_data import locaciones as regiones

def get_comunas(region):
    url = "https://seremienlinea.minsal.cl/asdigital/mfarmacias/mapa.php"

    payload = "func=comunas&region=13"
    headers = {
    'authority': 'seremienlinea.minsal.cl',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-AR,es-419;q=0.9,es;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'edf2b787d71200dafd83c3d361162bdf1c672cd1=b9rbs0br0t3qhmk0ebuuus5gt4; _hjSessionUser_1899797=eyJpZCI6ImMyMDJhNmVlLTg5NjctNTBkNi05MmU2LWU2NzliNzVkNmVkYiIsImNyZWF0ZWQiOjE2ODY3NTA2NzQxNzIsImV4aXN0aW5nIjp0cnVlfQ==; visid_incap_2940246=4E6QAs9jRjWdCZnLqk1r9NJKj2QAAAAAQUIPAAAAAAAKPO3BATkIWGQsTv6rwu+Y; incap_ses_1269_2940246=YGKCEqw14BEQP6QMiGWcEdJKj2QAAAAAE7CkkuAdVmqzT/YKGm7KDg==; incap_ses_1272_2940246=brtyQ9pxEXTOKD37Aw6nEcrMkWQAAAAAxpfsPj/WiYPJrmbJzwxUAA==; _gid=GA1.2.367111530.1687276747; _hjSession_1899797=eyJpZCI6IjMwMTVlN2NmLTZhZjYtNDIyMy04MjA0LWU1MzAxYjJlNTUzYSIsImNyZWF0ZWQiOjE2ODcyNzY3NDc2MTEsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _ga_K0XLHJL8YF=GS1.1.1687276747.2.1.1687276760.0.0.0; _ga=GA1.1.142835544.1686750135; _ga_S5W7DTQL54=GS1.1.1687276761.5.1.1687277034.0.0.0',
    'origin': 'https://seremienlinea.minsal.cl',
    'referer': 'https://seremienlinea.minsal.cl/asdigital/index.php?mfarmacias',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    arr_respuesta = response.json()
    print(arr_respuesta['respuesta'])
    return arr_respuesta['respuesta']

arr_comunas = []

for r in regiones:
    comunas = get_comunas(r['rg'])
    arr_comunas.append({"region": r['rg'], "comunas": comunas})

print(arr_comunas)

# Escribir arr_comunas en un archivo JSON
with open('comunas.json', 'w') as file:
    json.dump(arr_comunas, file)

print("Archivo JSON creado exitosamente.")