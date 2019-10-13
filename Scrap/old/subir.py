import sqlite3
import json
import requests
def ac(name):
    name = name.replace('á','a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)

con = sqlite3.connect('../db.sqlite3')
cursor = con.cursor()
sql = "SELECT nombrep FROM basedatos_pais"
sq = cursor.execute(sql)
s= sq.fetchall()


dir = 'Json/file.json'
paises = json.load(open(dir))
for pais in paises:
    p=ac(str(pais['Pais'].lower()))
    region_t = ac(str(pais['Continente'].lower()))

    for pais_bd in s:
        if p == str(pais_bd[0]):
            cons = "Select idpais into basedatos_pais where=?);"
            cons=("SELECT idpais FROM basedatos_pais WHERE nombrep=?")
            v=cursor.execute(cons, (p,))
            m=v.fetchall()
            #print(m[0][0])
            #print(p+'||'+str(pais_bd[0])+"||")
            insert_reg = "insert into basedatos_region values(?, ?, ?);"
            cursor.execute(insert_reg, (None, str(m[0][0]), region_t,))
con.commit()
con.close()










