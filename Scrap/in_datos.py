#ingresa los datos a las tablas de pais,region,tipocambio,categoria y sub-categoria
import json
import sqlite3

#remueve los acentos de los string
def ac(name):
    name = name.replace('á','a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)


# funcio que sube los paises a la base de datos
def in_pais():
    with open('Json/paises.json') as file:
        paises = json.load(file)

    for pais in paises:
        conn = sqlite3.connect('../db.sqlite3')
        c = conn.cursor()
        c.execute('''INSERT INTO  basedatos_pais VALUES(?,?)''', (None, str(pais['pais'])))
        conn.commit()
        conn.close()
        pass
    pass

#funcion que sube la regiones ||solo capitale de paises que no son chile
def in_region():

    con = sqlite3.connect('../db.sqlite3')
    cursor = con.cursor()
    sql = "SELECT nombrep FROM basedatos_pais"
    sq = cursor.execute(sql)
    s = sq.fetchall()

    dir = 'Json/file.json'
    paises = json.load(open(dir))
    for pais in paises:
        p = ac(str(pais['Pais'].lower()))
        region_t = ac(str(pais['Continente'].lower()))

        for pais_bd in s:
            if p == str(pais_bd[0]):
                cons = ("SELECT idpais FROM basedatos_pais WHERE nombrep=?")
                v = cursor.execute(cons, (p,))
                m = v.fetchall()
                insert_reg = "insert into basedatos_region values(?, ?, ?);"
                cursor.execute(insert_reg, (None, region_t, str(m[0][0])))
    con.commit()
    con.close()
    pass

#funcion que ingresa los tipo de moneda al a BD
def in_tipocambio():
    with open('Json/tipo_cambio.json') as file:
        moneda = json.load(file)

    for m in moneda['paises']:
        conn = sqlite3.connect('../db.sqlite3')
        c = conn.cursor()

        nombre = c.execute("SELECT * FROM basedatos_tipocambio WHERE nombrecamp=?",
                           (ac(str(m['tipo cambio'])),)).fetchall()

        if len(nombre) == 0:
            c.execute('''INSERT INTO  basedatos_tipocambio VALUES(?,?)''', (None, ac(str(m['tipo cambio']))))

        conn.commit()
        conn.close()
        pass
    pass
def iconos(id):
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
    elif id == 'investigacion':
        return 'investigacion.png'
    elif id == 'innovacion':
        return 'innovacion.png'
    elif id == 'emprendimiento':
        return 'emprendimiento.png'
    elif id == 'formacion personal':
        return 'formacion_personal.png'
    elif id == 'puentes y caminos':
        return 'puentes_y_caminos.png'
    elif id == 'hospitales y consultorios':
        return 'hospitales_y_consultorios.png'
    elif id == 'transporte y telecomunicaciones':
        return 'transporte_y_telecomunicaciones.png'

def in_categoria():
    lista_categoria=dict()
    lista_categoria = {'salud':['medicamento', 'infraestructura salud','servicios','insumos'],'supermercado':['precios en supermercados'],'educacion':['infraestructura educacion','costo educacion'],'vivienda':['vivienda y salario','articulos para el hogar','gastos de vivienda'],'otros':['ropa y calazado','ocio y deportes','recreacion y cultura'],'transporte':['transporte y servicio','medios de transporte'],'restaurant y hoteles':['precio restaurant','precio hoteles'],'ciencia y tecnologia':['investigacion','innovacion','emprendimiento','formacion personal'],'obras publicas':['puentes y caminos','hospitales y consultorios','transporte y telecomunicaciones']}
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()


    for categorias in lista_categoria:
        c.execute('''INSERT INTO  basedatos_categoria VALUES(?,?)''', (None, categorias))
        id= c.lastrowid

        subcategoria=lista_categoria[categorias]
        for sub in subcategoria:
            c.execute('''INSERT INTO  basedatos_subcategoria VALUES(?,?,?,?)''', (None,sub, id, iconos(sub)))



    conn.commit()
    conn.close()

def in_Reg_Chile():
    List_Reg_Chile = dict()
    List_Reg_Chile = {'arica y parinacota', 'tarapaca', 'antofagasta', 'atacama', 'coquimbo', 'valparaiso',
                      'libertador general bernardo ohiggins', 'maule', 'ñuble', 'biobio', 'la araucania', 'los rios',
                      'los lagos', 'aisen', 'magallanes'}
    con = sqlite3.connect('../db.sqlite3')
    cursor = con.cursor()
    sql = "SELECT idpais FROM basedatos_pais WHERE nombrep='chile' "
    sq = cursor.execute(sql)
    s = sq.fetchall()
    for chile in s:
        pass

    for regiones in List_Reg_Chile:
        insert_Reg_Chile = "INSERT INTO basedatos_region VALUES(?,?,?);"
        cursor.execute(insert_Reg_Chile, (None,regiones, chile[0],))
        pass
    con.commit()
    con.close()
    pass
in_pais()
in_region()
in_Reg_Chile()
in_tipocambio()
in_categoria()
