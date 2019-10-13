
import json
import sqlite3


with open('Json/paises.json') as file:
    paises= json.load(file)


for pais in paises:
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute('''INSERT INTO  basedatos_pais VALUES(?,?)''', (None,str(pais['pais'])))
    conn.commit()
    conn.close()
    pass





