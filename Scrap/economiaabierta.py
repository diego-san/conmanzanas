import requests
import json
import chardet
from datetime import date
import consulta
import insertar
def ac(name):
    return (name)
def modifica_fecha_publicacion(fecha_old):
    dia = fecha_old[0:2]
    mes = fecha_old[3:5]
    ano = fecha_old[6:10]
    fecha_new = ano+'-'+mes+'-'+dia
    return fecha_new

resp = requests.get('https://api.datos.sernac.cl/api/v2/dashboards/PRECI-MEDIC.json/?auth_key=edbb95d24d7caeeb9dc6a0da35bc5a3c1fed957d')

#list_precio_medicamento = json.loads(resp.content)

list_precio_medicamento =  json.loads(resp.content.decode(chardet.detect(resp.content)['encoding']))


page = 0
validador = 0

ultimo = list_precio_medicamento['resources'][0]
guid = ultimo['guid'].strip()

contador = 0

while validador == 0:
    link = "https://api.datos.sernac.cl/api/v2/datastreams/" + guid + "/data.pjson/?auth_key=edbb95d24d7caeeb9dc6a0da35bc5a3c1fed957d&limit=50&page=" + str(
        page)

    lista_producto = requests.get(link)
    lista_producto_json = json.loads(lista_producto.content.decode(chardet.detect(lista_producto.content)['encoding']))
    if len(lista_producto_json['result']) == 1:
        validador = 1
        pass
    page = page + 1
    for c in range(0, 49):
        Unidad = 'unidad'
        Cantidad = 1
        lista_medicamento = lista_producto_json['result'][c]
        nombre = lista_medicamento['Glosa_Producto-Principio-Activo']
        region = lista_medicamento['Region']
        precio = str(lista_medicamento['Precio']).replace(".","").replace("$","")

        fecha_publicacion = modifica_fecha_publicacion(lista_medicamento['Fecha'])

        fecha_hoy = date.today()
        fuente = 'https://datos.sernac.cl/dashboards/20611/precios-medicamentos/'

        if ac(region.lower()) == "metropolitana de santiago":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("santiago")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                    id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)

        elif ac(region.lower()) == "aysen del gral. carlos ibanez del campo":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("aisen")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "valparaiso":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("valparaiso")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "tarapaca":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("tarapaca")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "del libertador general bernardo ohiggins":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("libertador general bernardo ohiggins")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "de los rios":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("los rios")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "de la araucania":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("la araucania")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "del maule":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("maule")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "ñuble":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("ñunle")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "coquimbo":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("coquimbo")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "del bio bio":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("biobio")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "de magallanes y de la antartica chilena":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("magallanes")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "atacama":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("atacama")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "antofagasta":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("antofagasta")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "arica y parinacota":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("arica y parinacota")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        elif ac(region.lower()) == "de los lagos":
            tipo_cambio = consulta.get_id_tipocambio_nombre("peso chileno")
            id_Reg = consulta.get_id_reg("los lagos")
            subc = consulta.get_id_sub_nombre("medicamento")

            insertar.in_datos_productos(precio, fuente, fecha_hoy, fecha_publicacion, tipo_cambio[0][0],
                                        id_Reg[0][0], subc[0][0], ac(nombre.lower()), Unidad, Cantidad)
        contador = contador + 1
        print(str(contador)+') '+nombre+'| pagina: '+str(page))

    pass


