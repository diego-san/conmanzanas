import requests
import time
from bs4 import BeautifulSoup
import json
import os.path

data = {}
data['Productos'] = []
paises = {}
paises['pais'] = []




paises = ['afganistan']
product =['precios-supermercado']
paises_3 = ['afganistan','albania','chile', 'argentina']
for pais in paises:
        
    url = 'https://preciosmundi.com/'+pais
    for i in product:
        ur = url+'/'+i
        r = requests.get(ur)
       
        soup = BeautifulSoup(r.content, "html.parser")
        tbody_total = soup.find_all('tbody')

        for tbody in tbody_total:
            tr_tabla = tbody.find_all('tr')


            for tr_dato in tr_tabla:
                fecha_actualizacion = soup.find('p').get_text().strip()
                nombre = tr_dato.find('td', class_='product-name').get_text().strip()
                precio_peso = tr_dato.find_all('td', class_='price')[0].get_text().strip()
                cantidad = len(precio_peso)
                precio_peso = precio_peso[:cantidad-1]
                precio_dolar = tr_dato.find_all('td', class_='price')[1].get_text().strip()
                cantidad = len(precio_dolar)
                
                if pais in paises_3:
                        
                    precio_dolar= precio_dolar[:cantidad-1]
                    precio_euro = tr_dato.find_all('td', class_='price')[2].get_text().strip()
                    cantidad = len(precio_euro)
                    precio_euro = precio_euro[:cantidad-1]
                    
                data['Productos'].append({
                'nombre': nombre,
                'precio_peso': precio_peso,
                'precio_dolar': precio_dolar,
                'precio_euro': precio_euro,
                'url': ur,
                'Fecha de publicacion': fecha_actualizacion,
                'fechaScrapy': time.strftime("%d/%m/%Y"),
                'Categoria':i,
                'pais': pais,
                                    })

dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

file_name ='archivo__'+time.strftime("%d-%m-%Y-%H-%M-%S")+'.json'

with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)