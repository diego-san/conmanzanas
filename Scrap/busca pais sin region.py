import sqlite3
import consulta


lista = consulta.lista_pais_id()

for pais in lista:

    result = consulta.get_region(pais[0])

    if len(result) == 0:
        print('id de pais sin region en bd '+str(pais[0]))
    pass


