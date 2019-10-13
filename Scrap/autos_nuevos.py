import requests
from bs4 import BeautifulSoup
import consulta
import insertar
from datetime import datetime
def ac(name):
    name = name.replace('á', 'a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)
product = ['alfa-romeo', 'audi', 'baic', 'bmw', 'brilliance', 'changan', 'chery', 'chevrolet', 'chrysler', 'citroen','toyota','volkswagen','volvo','seat','skoda','ssangyong','subaru','suzuki','ram','renault','peugeot','porsche','proton','mahindra','maxus','mazda','mercedes-benz','mg','mini','mitsubishi','nissan','opel','lada','land-rover','lexus','lifan','kia','jac-motors','jaguar','jeep','jmc','honda','iveco','hyundai','ford','fiat','dodge']
#product = ['audi']
for marcas in product:
    url ='https://www.autocosmos.cl/catalogo/vigente/'+marcas
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tbody_total = soup.find_all(class_='model-card__content')
    for tbody in tbody_total:
        tr_tabla = tbody.find(class_='model-card__price').get_text().strip()
        if tr_tabla == 'Precio no disponible':
            pass
        else:
            termino_cadena = len(tr_tabla)
            nombre = tbody.find(class_='model-card__brand').get_text().strip()
            precio = tr_tabla[29:termino_cadena].replace('.','')
            tipo_cambio_id = consulta.get_id_tipocambio_nombre('peso chileno')
            id_region = consulta.get_id_reg('santiago')
            id_sub = consulta.get_id_sub_nombre('medios de transporte')
            ahora = datetime.now()
            img = insertar.iconos(6)
            fecha_obtencion = ahora.strftime('%d/%m/%Y')
            unidad = 'unidad'
            cant = 1
            print(str(tr_tabla) + "| |" + str(ac(nombre).lower())+"| |"+str(url))
            insertar.in_datos_productos(precio, url, fecha_obtencion, fecha_obtencion,tipo_cambio_id[0][0],id_region[0][0], id_sub[1][0], str(ac(nombre).lower()), unidad, cant,img)

