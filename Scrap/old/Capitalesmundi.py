import requests
from bs4 import BeautifulSoup
import json
import os.path

def ac(name):
    name = name.replace('á','a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)
data = {}
data['paises'] = []
continentes= ['europa', 'america', 'asia', 'africa', 'oceania']
for continente in continentes:
    url= "https://preciosmundi.com/"+continente
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tablas = soup.find_all('div', class_=('col-lg-3 col-md-3 col-sm-6'))
    table = soup.find_all('ul', class_=('list-unstyled countries'))
    for pais in table:
        s= pais.find_all('li')
        for li in s:

            data['paises'].append({
                'pais': ac(li.get_text().lower()),
                                    })
            dir = os.path.dirname(os.path.abspath(__file__))

            file_name = 'paisesPM.json'
dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'paises.json'

with open(os.path.join(dir, file_name), 'w') as file:


    json.dump(data, file, indent=4, ensure_ascii=False)
