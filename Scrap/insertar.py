import sqlite3
import os

dir = str(os.path.dirname(os.path.abspath(__file__)))


def in_datos_productos(precio, fuente, fechas, fechapub, id_cambio_id, id_reg_id, id_sub, nombre, unidad, cant, img):

    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute('''INSERT INTO  basedatos_bienesyservicios VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (None, str(nombre), float(precio), img, unidad,float(cant),fuente, fechas,fechapub,id_cambio_id,id_reg_id,id_sub, True))
    conn.commit()
    conn.close()



def iconos(ids):
    id = nombre_subc(ids)[0][0]


    if id == 'medicamento':
        return 'medicamento.png'
    elif id == 'infraestructura salud':
        return 'infraestructura.png'
    elif id == 'servicios':
        return 'servicio.png'
    elif id == 'insumos':
        return 'insumo.png'
    elif id == 'precios en supermercados':
        return 'supermercado.png'
    elif id == 'infraestructura educacion':
        return 'infraestructura_educacion.png'
    elif id == 'costo educacion':
        return 'costoeducacion.png'
    elif id == 'vivienda y salario':
        return 'vivienda_y_salario.png'
    elif id == 'articulos para el hogar':
        return 'articulos_para_el_hogar.png'
    elif id == 'gastos de vivienda':
        return 'gasto_de_vivienda.png'
    elif id == 'ropa y calazado':
        return 'ropa_y_calzado.png'
    elif id == 'ocio y deportes':
        return 'ocio_y_deporte.png'
    elif id == 'recreacion y cultura':
        return 'recreacion_y_cultura.png'
    elif id == 'transporte y servicio':
        return 'transporte_y_servicio.png'
    elif id == 'medios de transporte':
        return 'medio_de_trasnporte.png'
    elif id == 'precio restaurant':
        return 'precio_restaurant.png'
    elif id == 'precio hoteles':
        return 'preciohoteles.png'

def nombre_subc(id):
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT nomsc from basedatos_subcategoria WHERE idsubc=?", [str(id)],)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows