import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import time
import consulta
import insertar

def pulir_precio(precio_old):
    total_cadena = len(precio_old)
    p_sin = precio_old[2:total_cadena]
    precio_p = p_sin.replace('.','')
    return precio_p
    pass

def pulir_nombre(nombre):
    posicion = nombre.find(' ')
    total = len(nombre)
    if nombre[posicion-1] == '*':
        return nombre[posicion:total]
    return nombre
    pass

for cate in range(1,8):
    if cate == 1:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate=1'
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')
        tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
        id_Reg = consulta.get_id_reg("valparaiso")
        subc = consulta.get_id_sub_nombre("servicios")
        Unidad = 'unidad'

        Cantidad = 1
        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link

            insertar.in_datos_productos(precio, fuente, fecha_obtencion_dato, fecha_actualizacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], nombre, Unidad, Cantidad)
            print("1")
    elif cate== 2:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate=2'
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')
        tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
        id_Reg = consulta.get_id_reg("valparaiso")
        subc = consulta.get_id_sub_nombre("servicios")

        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link
            print("2")
            insertar.in_datos_productos(precio, fuente, fecha_obtencion_dato, fecha_actualizacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], nombre, Unidad, Cantidad)
    elif cate == 3:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate=3'
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')
        tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
        id_Reg = consulta.get_id_reg("valparaiso")
        subc = consulta.get_id_sub_nombre("servicios")

        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link
            insertar.in_datos_productos(precio, fuente, fecha_obtencion_dato, fecha_actualizacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], nombre, Unidad, Cantidad)
            print("3")

    elif cate == 4:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate=4'
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')
        tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
        id_Reg = consulta.get_id_reg("valparaiso")
        subc = consulta.get_id_sub_nombre("servicios")

        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link
            insertar.in_datos_productos(precio, fuente, fecha_obtencion_dato, fecha_actualizacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], nombre, Unidad, Cantidad)
            print("4")

    elif cate == 6:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate=6'
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')
        tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
        id_Reg = consulta.get_id_reg("valparaiso")
        subc = consulta.get_id_sub_nombre("insumos")

        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link
            insertar.in_datos_productos(precio, fuente, fecha_obtencion_dato, fecha_actualizacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], nombre, Unidad, Cantidad)
            print("6")
    elif cate == 7:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate=7'
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')
        tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
        id_Reg = consulta.get_id_reg("valparaiso")
        subc = consulta.get_id_sub_nombre("insumos")

        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link
            insertar.in_datos_productos(precio, fuente, fecha_obtencion_dato, fecha_actualizacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], nombre.lower(), Unidad, Cantidad)
            print("7")

    time.sleep(5)