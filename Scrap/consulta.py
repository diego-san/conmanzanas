import sqlite3
import os

dir = str(os.path.dirname(os.path.abspath(__file__)))

def buscar_dato_pais(pais):
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idpais from basedatos_pais WHERE nombrep=?", (str(pais),))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows


def lista_pais_nombre():
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT nombrep from basedatos_pais")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def lista_pais_id():
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idpais from basedatos_pais")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_region(id):
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idpais_id from basedatos_region WHERE idpais_id=?", (id,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_region_pais(idpais):
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idreg from basedatos_region WHERE idpais_id=?", (str(idpais),))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
    pass

def get_id_tipocambio_nombre(nombre):
        conn = sqlite3.connect(dir+'/../db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT id_cambio from basedatos_tipocambio WHERE nombrecamp=?", (str(nombre).strip(),))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows
        pass

def get_id_sub_nombre(nombre):
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idsubc from basedatos_subcategoria WHERE nomsc=?", (str(nombre).strip(),))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
    pass

def get_id_reg(nombre):
    conn = sqlite3.connect(dir+'/../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idreg from basedatos_region WHERE nombreg=?", (str(nombre).strip(),))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
    pass
