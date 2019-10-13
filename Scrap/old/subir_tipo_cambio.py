
import json
import sqlite3
def ac(name):
    name = name.replace('á','a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)

with open('Json/tipo_cambio.json') as file:
    moneda= json.load(file)


for m in moneda['paises']:
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()

    nombre = c.execute("SELECT * FROM basedatos_tipocambio WHERE nombrecamp=?", (ac(str(m['tipo cambio'])),)).fetchall()

    if len(nombre) == 0:
        c.execute('''INSERT INTO  basedatos_tipocambio VALUES(?,?)''', (None, ac(str(m['tipo cambio']))))


    conn.commit()
    conn.close()
    pass




