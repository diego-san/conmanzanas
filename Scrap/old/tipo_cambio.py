import requests
from bs4 import BeautifulSoup
import json
import os.path

with open('Json/paises.json') as file:
    paises = json.load(file)

lista_pais_peso = {'chile': 'Peso Chileno', 'argentina': 'Peso Argentino', 'uruguay': 'Peso Uruguayo', 'mexico': 'Peso Mexicano'}
validador = 0

data = {}
data['paises'] = []

#funcion que obtiene el tipo de moneda
def tipo_moneda(tipo_precio):
    total_cadena = len(tipo_precio)
    direc = total_cadena - 1
    while tipo_precio[direc] != ' ':
        direc = direc - 1
        tipo_valor_filtrado = tipo_precio[0:direc]
        pass
    return tipo_valor_filtrado
    pass

for pais in paises:

    for pais_lista in lista_pais_peso:
        if pais['pais'] == pais_lista:
            #cambia a 1 cuando es un tipo de pais con moneda tipo peso
            validador = 1
            tipo_cambio = lista_pais_peso[pais_lista]

            pass
        pass

    if validador == 0:
        pais_new = str(pais['pais'].replace(' ', '-'))
        url = 'https://preciosmundi.com/' + pais_new + '/precios-supermercado'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        thead = soup.find('thead')
        tipo_cambio = tipo_moneda(thead.find_all('th')[1].get_text().strip())






        pass
    validador = 0
    print(pais['pais'])
    data['paises'].append({
        'nombre': str(pais['pais']),
        'tipo cambio': str(tipo_cambio.lower().strip()),
    })
    pass

dir = os.path.dirname(os.path.abspath(__file__)) + '/json'

file_name ='tipo_cambio.json'

with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)