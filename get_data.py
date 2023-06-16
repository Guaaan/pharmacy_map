import requests
import json
from urllib.parse import urlencode


def obtener_coordenadas(lat, lng, factor, rg):
    lat_diff = abs(lat - lat * factor)
    lng_diff = abs(lng - lng * factor)

    lat_max = lat + lat_diff
    lat_min = lat - lat_diff
    lng_max = lng + lng_diff
    lng_min = lng - lng_diff

    return {"rg": rg, "lat": lat, "lng": lng, "lat_min": lat_min, "lat_max": lat_max,
            "lng_min": lng_min, "lng_max": lng_max}


data = [
    {
        "numero": "15",
        "region": "XV",
        "nombre": "Arica y Parinacota",
        "id": "15",
        "lat": "-18.479707",
        "lng": "-70.310482"
    },
    {
        "numero": "01",
        "region": "I",
        "nombre": "Tarapaca",
        "id": "1",
        "lat": "-20.232689",
        "lng": "-70.136042"
    },
    {
        "numero": "02",
        "region": "II",
        "nombre": "Antofagasta",
        "id": "2",
        "lat": "-23.655776",
        "lng": "-70.397944"
    },
    {
        "numero": "03",
        "region": "III",
        "nombre": "Atacama",
        "id": "3",
        "lat": "-27.368584",
        "lng": "-70.332383"
    },
    {
        "numero": "04",
        "region": "IV",
        "nombre": "Coquimbo",
        "id": "4",
        "lat": "-29.904899",
        "lng": "-71.251766"
    },
    {
        "numero": "05",
        "region": "V",
        "nombre": "Valparaíso",
        "id": "5",
        "lat": "-33.04864",
        "lng": "-71.613353"
    },
    {
        "numero": "13",
        "region": "XIII",
        "nombre": "Metropolitana",
        "id": "13",
        "lat": "-33.479361",
        "lng": "-70.633042"
    },
    {
        "numero": "06",
        "region": "VI",
        "nombre": "Libertador General Bernardo O'Higgins",
        "id": "6",
        "lat": "-34.5755374",
        "lng": "-71.00223110"
    },
    {
        "numero": "07",
        "region": "VII",
        "nombre": "Maule",
        "id": "7",
        "lat": "-35.425676",
        "lng": "-71.648958"
    },
    {
        "numero": "16",
        "region": "XVI",
        "nombre": "Ñuble",
        "id": "16",
        "lat": "-36.610027",
        "lng": "-72.102127"
    },
    {
        "numero": "08",
        "region": "VIII",
        "nombre": "Bio-Bio",
        "id": "8",
        "lat": "-36.82396",
        "lng": "-73.044973"
    },
    {
        "numero": "09",
        "region": "IX",
        "nombre": "La Araucanía",
        "id": "9",
        "lat": "-38.738163",
        "lng": "-72.591269"
    },
    {
        "numero": "14",
        "region": "XIV",
        "nombre": "Los Rios",
        "id": "14",
        "lat": "-39.832774",
        "lng": "-73.228373"
    },
    {
        "numero": "10",
        "region": "X",
        "nombre": "Los Lagos",
        "id": "10",
        "lat": "-41.470482",
        "lng": "-72.941322"
    },
    {
        "numero": "11",
        "region": "XI",
        "nombre": "Aysén del General Carlos Ibáñez del Campo",
        "id": "11",
        "lat": "-45.572074",
        "lng": "-72.068376"
    },
    {
        "numero": "12",
        "region": "XII",
        "nombre": "Magallanes y de la Antártica Chilena",
        "id": "12",
        "lat": "-53.166717",
        "lng": "-70.916665"
    }
]


def get_pharmacies():
    url = "https://seremienlinea.minsal.cl/asdigital/mfarmacias/mapa.php"

    results = []

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-AR,es-419;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'edf2b787d71200dafd83c3d361162bdf1c672cd1=b9rbs0br0t3qhmk0ebuuus5gt4; _gid=GA1.2.197336248.1686750674; _hjFirstSeen=1; _hjSession_1899797=eyJpZCI6ImNkNDg1ZGMwLTZiOTQtNGJiMi04NmJjLWI1YmQ0OGMxOWU1NyIsImNyZWF0ZWQiOjE2ODY3NTA2NzQ0NzksImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _hjSessionUser_1899797=eyJpZCI6ImMyMDJhNmVlLTg5NjctNTBkNi05MmU2LWU2NzliNzVkNmVkYiIsImNyZWF0ZWQiOjE2ODY3NTA2NzQxNzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.142835544.1686750135; _ga_K0XLHJL8YF=GS1.1.1686750674.1.1.1686750979.0.0.0; _ga_S5W7DTQL54=GS1.1.1686750134.1.1.1686751898.0.0.0',
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
    locaciones = [{"rg": 15, "lat": -18.479707, "lng": -70.310482, "lat_min": -27.7195605, "lat_max": -9.2398535, "lng_min": -105.465723, "lng_max": -35.155241}, {"rg": 1, "lat": -20.232689, "lng": -70.136042, "lat_min": -30.3490335, "lat_max": -10.1163445, "lng_min": -105.204063, "lng_max": -35.068021}, {"rg": 2, "lat": -23.655776, "lng": -70.397944, "lat_min": -35.483664, "lat_max": -11.827888, "lng_min": -105.596916, "lng_max": -35.198972}, {"rg": 3, "lat": -27.368584, "lng": -70.332383, "lat_min": -41.052876, "lat_max": -13.684292, "lng_min": -105.49857449999999, "lng_max": -35.1661915}, {"rg": 4, "lat": -29.904899, "lng": -71.251766, "lat_min": -44.8573485, "lat_max": -14.9524495, "lng_min": -106.877649, "lng_max": -35.625883}, {"rg": 5, "lat": -33.04864, "lng": -71.613353, "lat_min": -49.572959999999995, "lat_max": -16.52432, "lng_min": -107.4200295, "lng_max": -35.8066765}, {"rg": 13, "lat": -33.479361, "lng": -70.633042, "lat_min": -50.219041499999996, "lat_max": -16.7396805, "lng_min": -105.94956300000001, "lng_max": -35.316521}, {"rg": 6, "lat": -34.5755374, "lng": -71.0022311, "lat_min": -51.8633061, "lat_max": -17.2877687, "lng_min": -106.50334665, "lng_max": -35.50111555}, {"rg": 7, "lat": -35.425676, "lng": -71.648958, "lat_min": -53.138514, "lat_max": -17.712838, "lng_min": -107.47343699999999, "lng_max": -35.824479}, {"rg": 16, "lat": -36.610027, "lng": -72.102127, "lat_min": -54.9150405, "lat_max": -18.3050135, "lng_min": -108.1531905, "lng_max": -36.0510635}, {"rg": 8, "lat": -36.82396, "lng": -73.044973, "lat_min": -55.23594, "lat_max": -18.41198, "lng_min": -109.5674595, "lng_max": -36.5224865}, {"rg": 9, "lat": -38.738163, "lng": -72.591269, "lat_min": -58.1072445, "lat_max": -19.3690815, "lng_min": -108.88690349999999, "lng_max": -36.2956345}, {"rg": 14, "lat": -39.832774, "lng": -73.228373, "lat_min": -59.749161, "lat_max": -19.916387, "lng_min": -109.84255950000001, "lng_max": -36.6141865}, {"rg": 10, "lat": -41.470482, "lng": -72.941322, "lat_min": -62.20572299999999, "lat_max": -20.735241, "lng_min": -109.41198299999999, "lng_max": -36.470661}, {"rg": 11, "lat": -45.572074, "lng": -72.068376, "lat_min": -68.35811100000001, "lat_max": -22.786037, "lng_min": -108.102564, "lng_max": -36.034188}, {"rg": 12, "lat": -53.166717, "lng": -70.916665, "lat_min": -79.7500755, "lat_max": -26.5833585, "lng_min": -106.37499749999999, "lng_max": -35.4583325}]
    
    for item in locaciones:
        payload = {
            "func": "sector",
            "filtro": "todos",
            "fecha": "0",
            "region": item['rg'],
            "lat": item["lat"],
            "lng": item["lng"],
            "latMin": item["lat_min"],
            "latMax": item["lat_max"],
            "lngMin": item["lng_min"],
            "lngMax": item["lng_max"],
            "hora": "10:16:37"
        }

        encoded_payload = urlencode(payload)
        response = requests.post(url, headers=headers, data=encoded_payload)
        arr_farmacias = response.json()["respuesta"]["locales"]
        for r in arr_farmacias:
            results.append(r)
        print(response.text)
        print(response.status_code)
    print(results)
    with open("farmacias.json", "w") as file:
        json.dump(results, file)

# get_pharmacies()
# coordenadas = []
# for item in data:
#     coordenadas.append(obtener_coordenadas(
#         float(item['lat']), float(item['lng']), 0.5, int(item['numero'])))
# print(json.dumps(coordenadas))