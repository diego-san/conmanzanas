import requests
from bs4 import BeautifulSoup
from datetime import date
import consulta
import insertar
import filtro
import time
product = ['precios-supermercado', 'precio-restaurantes', 'precio-ropa-calzado', 'precio-transporte-servicios', 'precio-vivienda-salarios', 'precio-ocio-deportes']
lista_sub_categoria = ['precios en supermercados', 'precio restaurant', 'ropa y calazado', 'transporte y servicio' ,'vivienda y salario', 'ocio y deportes ']
paises= consulta.lista_pais_nombre()

lista_pais_peso = {'chile': 'peso chileno', 'argentina': 'peso argentino', 'uruguay': 'peso uruguayo', 'mexico': 'peso mexicano'}
validador = 0

#remueve los acentos de los string
def ac(name):
    name = name.replace('á', 'a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)
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

def busca_mes(mes):
    diccionario = {'enero': '01', 'febrero':'02','marzo':'03','abril':'04','mayo':'05','junio':'06','julio':'07','agosto':'08','septiembre':'09','obtubre':'10','noviembre':'11','diciembre':'12'}
    for mes_list in diccionario:
        if mes == mes_list:
            return diccionario[mes_list]
        pass
    return '01'
    pass

#funcion que genera fecha de actualizacion
def fecha_actializacion(fecha):
    total_cadena = len(fecha)
    direc = 0
    fecha= fecha[16:total_cadena-1]

    while fecha[direc] != ' ':
        direc = direc + 1
        mes = fecha[0:direc]
        ano = fecha[direc+4:]
    fecha_final = ano+'-'+busca_mes(mes)+'-01'
    return fecha_final
    pass

def pulir_precio(precio):
    precio_new = precio.replace(',', '.')
    r = 'False'
    v = 0
    while str(r) == 'False':
        v = v + 1
        longitud = len(precio_new)
        r = precio_new[longitud-1].isdigit()
        precio_new = precio_new[0:len(precio_new)-1]

    return precio_new

contador_pais = 1

for pais in paises:

    pais_new = pais[0].replace(' ', '-')
    url = 'https://preciosmundi.com/' + pais_new
    id_region = consulta.get_region_pais(consulta.buscar_dato_pais(pais[0])[0][0])[0][0]

    for pais_lista in lista_pais_peso:
        if pais[0] == pais_lista:
            #cambia a 1 cuando es un tipo de pais con moneda tipo peso
            validador = 1
            tipo_cambio = lista_pais_peso[pais_lista].lower().strip()

            pass
        pass


    sub_categoria = 0
    for i in product:
        id_subcategoria = consulta.get_id_sub_nombre(lista_sub_categoria[sub_categoria])[0][0]

        ur = url + '/' + i
        r = requests.get(ur)
        soup = BeautifulSoup(r.content, "html.parser")
        fecha_actualizacion_final = fecha_actializacion(soup.find('p').get_text().strip())
        tbody_total = soup.find_all('tbody')

        if validador == 0:
            thead = soup.find('thead')
            tipo_cambio = ac(tipo_moneda(thead.find_all('th')[1].get_text().strip().lower()))

            pass

        tipo_cambio_id = consulta.get_id_tipocambio_nombre(tipo_cambio)[0][0]


        for tbody in tbody_total:
            tr_tabla = tbody.find_all('tr')

            for tr_dato in tr_tabla:

                nombre = tr_dato.find('td', class_='product-name').get_text().strip()
                precio = pulir_precio(tr_dato.find_all('td', class_='price')[0].get_text().strip())
                fecha_obtencion_dato = date.today()
                fuente = ur
                name = filtro.palabra(nombre)
                img = insertar.iconos(id_subcategoria)

                if name == 0:
                    print("name")
                else:
                    cantidad = float(name[1].replace(',', '.'))
                    if nombre != 'hipoteca: tasa de interes anual (%)':
                        insertar.in_datos_productos(str(precio), fuente, fecha_obtencion_dato, fecha_actualizacion_final, tipo_cambio_id, id_region, id_subcategoria, ac(name[0].lower()), ac(name[2].lower()), cantidad, img)
                        print(precio)

        sub_categoria = sub_categoria + 1

        print(str(contador_pais) + ' de 126 paises')
    time.sleep(1)
    validador = 0
    contador_pais = contador_pais +1
    pass






