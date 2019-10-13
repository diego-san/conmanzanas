import datetime
import random

class algoritmo:

    def inicio(data, monto, numero_produc):

        f = algoritmo.lista_random(data, numero_produc)
        #f[0]['producto']['ccc'] = 3

        if len(f) > 0:
            return algoritmo.calcula_cuanto(f,monto)



        return f


        pass

    def lista_random(data, n):
        cantidad = len(data)
        list_elegido = []
        elegidos = []
        if cantidad > 0:

            if cantidad > 1:
                for x in range(0, n):
                    numero_random = random.randint(0, cantidad-1)

                    if algoritmo.comprobar_lista(elegidos,numero_random) == 0:

                        if  algoritmo.comprobar_lista_nombre(list_elegido,data[numero_random]) ==0:
                            elegidos.append(numero_random)
                            list_elegido.append({'producto': {'idbs': data[numero_random]['idbs'],
                                                                'nombrebs': data[numero_random]['nombrebs'],
                                                                'precio': float(data[numero_random]['precio']),
                                                                'fuente': data[numero_random]['fuente'],
                                                                'fechas': data[numero_random]['fechas'],
                                                                'fechapub': data[numero_random]['fechapub'],
                                                                'img': data[numero_random]['imgc'],
                                                              'unidad':data[numero_random]['umed'],
                                                              'cantidad':data[numero_random]['cant_u'],
                                                              }})


                        else:
                            pass






            elif cantidad == 1:
                list_elegido.append({'producto': {'idbs': data[0]['idbs'],
                                                  'nombrebs': data[0]['nombrebs'],
                                                  'precio': float(data[0]['precio']),
                                                  'fuente': data[0]['fuente'],
                                                  'fechas': data[0]['fechas'],
                                                  'fechapub': data[0]['fechapub'],
                                                  'img': data[0]['imgc'],
                                                  'unidad': data[0]['umed'],
                                                  'cantidad': data[0]['cant_u'],
                                                  }})

        return list_elegido

    #funcion que elije la cantidad de productos a mostrar
    def monto_dividir(monto):
        if int(monto) <= 1000:
            cantidad_produc = 1
        elif int(monto) > 1000 and int(monto) <= 10000:
            cantidad_produc = random.randint(1, 2)
        elif int(monto) > 10000 and int(monto) <= 100000:
            cantidad_produc = random.randint(1, 3)
        elif int(monto) > 100000 and int(monto) <= 1000000:
            cantidad_produc = random.randint(1, 4)
        else:
            cantidad_produc = random.randint(1, 5)

        return cantidad_produc

    def comprobar_lista(lista,d):
        com = len(lista)
        if com > 0:
            for l in lista:
                if l == d:
                    return 1
        # 0 cuando no esta en la lista
        return 0

    def comprobar_lista_nombre(lista, data):

        com = len(lista)
        if com > 0:
            for l in lista:
                if l['producto']['nombrebs'] == data['nombrebs']:
                    return 1

        # 0 cuando no esta en la lista
        return 0

    def calcula_cuanto(data, monto):
        cantidad = len(data)
        resto= 0
        if cantidad == 1:
            contador = float(monto)/float(data[0]['producto']['precio'])
            suma = float(data[0]['producto']['precio'])* contador
            resto= float(monto)%float(data[0]['producto']['precio'])

            data[0]['producto']['suma_aproximada'] = suma
            data[0]['producto']['cantidad_veces'] = int(contador)


            return algoritmo.calcula_resto(data, resto)
        elif cantidad > 1 :

            for x in range(0, cantidad):
                contador = (float(monto)/cantidad) / float(data[x]['producto']['precio'])
                suma = data[x]['producto']['precio'] * int(contador)
                resto = float(monto) % float(data[x]['producto']['precio'])

                data[x]['producto']['suma_aproximada'] = int(suma)
                data[x]['producto']['cantidad_veces'] = int(contador)

            return algoritmo.calcula_resto(data, resto)




        pass

    def calcula_resto(data, resto):

        if resto >= 200:
            veces = resto/ 200
            suma = veces * 200
            data.append({'producto': {'idbs': 1,
                                                'nombrebs': 'manzana',
                                                'precio': 200,
                                                'fuente': 'https://www.google.com/search?client=firefox-b-d&q=precio+manzana+chile',
                                                'fechas': datetime.date(2019, 9, 1),
                                                'fechapub': datetime.date(2019, 9, 1),
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(veces),
                                                'img':'apple.png'}})

            return data


        return data