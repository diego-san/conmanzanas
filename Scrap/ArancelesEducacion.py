import requests
import json
import chardet
import insertar
from datetime import  date
import consulta
#saca acento
def ac(name):
    name = name.replace('á', 'a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)
link = []
link = ['ARANC-DE-REFER-EDUCA-79081', 'ARANC-DE-REFER-EDUCA-30961', 'ARANC-DE-REFER-EDUCA-46146', 'ARANC-DE-REFER-EDUCA-SUPER']
#creo link
for links in link:
    link_completo ='https://api.beta.datos.gob.cl/api/v2/datastreams/' + links + '/data.pjson/?auth_key=aaa74e84977ce81c13e2e760e4e8f03b5761b479&limit=50'
    link_final = requests.get(link_completo)
    lista_aranceles =  json.loads(link_final.content.decode(chardet.detect(link_final.content)['encoding']))
    strDate = lista_aranceles['created_at']
    strDate = lista_aranceles['created_at']
    # con esta tontera saco la fecha!
    for c in range(0, 10):
        fecha = strDate[0] + strDate[1] + strDate[2] + strDate[3] + strDate[4] + strDate[5] + strDate[6] + strDate[7] + strDate[8] + strDate[9]
    if links == 'ARANC-DE-REFER-EDUCA-79081':
        con=0
        for c in range(0, 16):
            con= con+1

            lista_cft = lista_aranceles['result'][c]
            Nom = ac(lista_cft['NOMBRE-CARRERA'].lower())
            Jornada = ac(lista_cft['JORNADA'].lower())
            Nombre_sede = ac(lista_cft['NOMBRE-SEDE'].lower())
            Nombre_ins = ac(lista_cft['NOMBRE-INSTITUCION'].lower())
            Nombre = Nom + "-" + Nombre_sede + "-" + Nombre_ins
            print(Nombre + "| |" + str(con))
            Arancel2 = lista_cft['ARANCEL-ANUAL-2019-28-12-18']
            Arancel = Arancel2.replace(',', '')
            Fuente = link_completo
            Fecha_hoy = date.today()
            Idtipocambio = consulta.get_id_tipocambio_nombre("peso chileno")
            IdRegion = consulta.get_id_reg("santiago")
            IdSub = consulta.get_id_sub_nombre('costo educacion')
            Unidad = "unidad"
            img = insertar.iconos(IdSub[0][0])
            Cantidad = 1
            insertar.in_datos_productos(Arancel, Fuente, Fecha_hoy, fecha, Idtipocambio[0][0], IdRegion[0][0], IdSub[0][0], Nombre, Unidad, Cantidad,img)

    elif (links == 'ARANC-DE-REFER-EDUCA-30961' or links == 'ARANC-DE-REFER-EDUCA-46146' or links == 'ARANC-DE-REFER-EDUCA-SUPER'):
        page = 0
        validar = 0

        while validar == 0:
            link_parte2 = str(link_completo) + "&page=" + str(page)
            lista = requests.get(link_parte2)
            lista_json = json.loads(
            lista.content.decode(chardet.detect(lista.content)['encoding']))
            if len(lista_json['result']) == 1:
                validador = 1
                pass
            page = page+1
            for c in range(0, 49):

                lista_cft = lista_aranceles['result'][c]
                Nom = ac(lista_cft['NOMBRE-CARRERA'].lower())
                Jornada = ac(lista_cft['JORNADA'].lower())
                Nombre_sede = ac(lista_cft['NOMBRE-SEDE'].lower())
                Nombre_ins = ac(lista_cft['NOMBRE-INSTITUCION'].lower())
                Nombre = Nom + "-" + Nombre_sede + "-" + Nombre_ins
                print(Nombre+"| |"+str(page))
                Arancel2 = lista_cft['ARANCEL-ANUAL-2019-28-12-18']
                Arancel = Arancel2.replace(',','')
                Fuente = link_completo
                Fecha_hoy = date.today()
                Idtipocambio = consulta.get_id_tipocambio_nombre("peso chileno")
                IdSub = consulta.get_id_sub_nombre('costo educacion')
                Unidad ="unidad"
                img = insertar.iconos(IdSub[0][0])
                Cantidad = 1
                if Nombre_sede[0:12] == "casa central" and Nombre_sede[14:19] == "temuc":
                    IdRegion = consulta.get_id_reg("la araucania")
                elif Nombre_sede[0:12] == "casa central" and Nombre_sede[14:19] == "conce":
                    IdRegion = consulta.get_id_reg("biobio")
                elif Nombre_sede[0:12] == "casa central" and Nombre_sede[14:19] == "santi":
                    IdRegion = consulta.get_id_reg("santiago")
                elif Nombre_sede[0:12] == "casa central" and Nombre_sede[14:19] == "osorn":
                    IdRegion = consulta.get_id_reg("los lagos")
                elif Nombre_sede[0:4] == "sede" and Nombre_sede[5:11] == "angol":
                    IdRegion = consulta.get_id_reg("la araucania")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:11] == "antofa" or Nombre_sede[5:11] == "calama"):
                    IdRegion = consulta.get_id_reg("antofagasta")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:12] == "san fer" or Nombre_sede[5:12] == "rancagu"):
                    IdRegion = consulta.get_id_reg("libertador general bernardo ohiggins")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:11] == "san jo" or Nombre_sede[5:11] == "bellav" or Nombre_sede[5:11] == "provid" or Nombre_sede[5:11] == "barrio" or Nombre_sede[5:11] == "santia" or Nombre_sede[5:11] == "maipu" or Nombre_sede[5:11] == "san be"):
                    IdRegion = consulta.get_id_reg("santiago")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:11] == "viña d" or Nombre_sede[5:11] == "valpar" or Nombre_sede[5:11] == "san fe" or Nombre_sede[5:11] == "san an"):
                    IdRegion = consulta.get_id_reg("valparaiso")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:11] == "curico" or Nombre_sede[5:10] =="talca"):
                    IdRegion = consulta.get_id_reg("maule")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:11] == "osorno" or Nombre_sede[5:11] =="puerto" or Nombre_sede[5:11] =="castro"):
                    IdRegion = consulta.get_id_reg("los lagos")
                elif Nombre_sede[0:4] == "sede" and (Nombre_sede[5:11] == "concep" or Nombre_sede[5:11] =="los an"):
                    IdRegion = consulta.get_id_reg("biobio")
                elif Nombre_sede[0:4] == "sede" and Nombre_sede[5:11] == "la ser":
                    IdRegion = consulta.get_id_reg("coquimbo")
                elif Nombre_sede[0:4] == "sede" and Nombre_sede[5:11] == "temuco":
                    IdRegion = consulta.get_id_reg("la araucania")
                elif Nombre_sede[0:6] == "campus":
                    IdRegion = consulta.get_id_reg("santiago")
                insertar.in_datos_productos(Arancel, Fuente, Fecha_hoy, fecha, Idtipocambio[0][0], IdRegion[0][0], IdSub[0][0], Nombre, Unidad, Cantidad, img)
