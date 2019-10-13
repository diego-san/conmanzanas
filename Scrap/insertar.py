import sqlite3
import os

dir = str(os.path.dirname(os.path.abspath(__file__)))


def in_datos_productos(precio, fuente, fechas, fechapub, id_cambio_id, id_reg_id, id_sub, nombre, unidad, cant, img):

    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute('''INSERT INTO  basedatos_bienesyservicios VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (None, str(nombre), float(precio), img, unidad,float(cant),fuente, fechas,fechapub,id_cambio_id,id_reg_id,id_sub))
    conn.commit()
    conn.close()


def iconos(id):

    if id == 1:
        return 'medicamento.png'
    elif id == 2:
        return 'infraestructura.png'
    elif id == 3:
        return 'servicio.png'
    elif id == 4:
        return 'insumo.png'
    elif id == 17:
        return 'supermercado.png'
    elif id == 7:
        return 'infraestructura_educacion.png'
    elif id == 8:
        return 'costoeducacion.png'
    elif id == 11:
        return 'vivienda_y_salario.png'
    elif id == 12:
        return 'articulos_para_el_hogar.png'
    elif id == 13:
        return 'gasto_de_vivienda.png'
    elif id == 14:
        return 'ropa_y_calzado.png'
    elif id == 15:
        return 'ocio_y_deporte.png'
    elif id == 16:
        return 'recreacion_y_cultura.png'
    elif id == 5:
        return 'transporte_y_servicio.png'
    elif id == 6:
        return 'medio_de_trasnporte.png'
    elif id == 9:
        return 'precio_restaurant.png'
    elif id == 10:
        return 'preciohoteles.png'
