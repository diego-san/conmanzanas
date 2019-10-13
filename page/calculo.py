import random
class calculo:



    def lista_producto(datos, monto, lista_id_sub):


        data = []
        for dato in datos:
            for id_sub in lista_id_sub:
                if id_sub == dato.idsubc_id:
                    data.append({'producto':{'idbs': dato.idbs, 'nombrebs':dato.nombrebs, 'precio':dato.precio, 'fuente':dato.fuente, 'fechas': dato.fechas, 'fechapub': dato.fechapub, 'img': dato.imgc}})



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


        lista_ramdon = calculo.randon_lista_producto(data, cantidad_produc)

        calculo_final= calculo.calculo_cuanto(lista_ramdon,monto)


        return calculo_final



    def randon_lista_producto(data,n_producto):
        lista_elegidos = []
        cantidad = len(data)
        if cantidad > 0:
            lista_elegidos = []
            #pocision en lista
            elegidos = []
            if cantidad != 1:
                for x in range(0, n_producto):

                    nuemro_ramdon = random.randint(0, cantidad-1)

                    try:
                        o = elegidos.index(nuemro_ramdon)
                    except:
                        elegidos.append(nuemro_ramdon)
                        lista_elegidos.append( {'producto':{'idbs': data[nuemro_ramdon]['producto']['idbs'], 'nombrebs':data[nuemro_ramdon]['producto']['nombrebs'], 'precio':data[nuemro_ramdon]['producto']['precio'], 'fuente':data[nuemro_ramdon]['producto']['fuente'], 'fechas':data[nuemro_ramdon]['producto']['fechas'], 'fechapub': data[nuemro_ramdon]['producto']['fechapub'], 'img':data[nuemro_ramdon]['producto']['img']}})

            else:
                lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                    'nombrebs': data[0]['producto']['nombrebs'],
                                                    'precio': data[0]['producto']['precio'],
                                                    'fuente': data[0]['producto']['fuente'],
                                                    'fechas': data[0]['producto']['fechas'],
                                                    'fechapub': data[0]['producto']['fechapub'],
                                                    'img':data[0]['producto']['img']}})


        else:
            lista_elegidos = data
        return lista_elegidos



    def calculo_cuanto(data,monto):

        cantidad = len(data)
        lista_elegidos= []
        if cantidad == 1:
            precio_p = data[0]['producto']['precio']
            contador = float(monto)/float(precio_p)
            suma = float(precio_p* int(contador))

            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[len(monton_ingresado) - 1] == '0':
                suma = int(suma)


            lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                'nombrebs': data[0]['producto']['nombrebs'],
                                                'precio': int(data[0]['producto']['precio']),
                                                'fuente': data[0]['producto']['fuente'],
                                                'fechas': data[0]['producto']['fechas'],
                                                'fechapub': data[0]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})
        elif cantidad == 2:
            precio_p = data[0]['producto']['precio']
            monto_2 = monto/2
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))

            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)


            lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                'nombrebs': data[0]['producto']['nombrebs'],
                                                'precio': int(data[0]['producto']['precio']),
                                                'fuente': data[0]['producto']['fuente'],
                                                'fechas': data[0]['producto']['fechas'],
                                                'fechapub': data[0]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})
            precio_p = data[1]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[1]['producto']['idbs'],
                                                'nombrebs': data[1]['producto']['nombrebs'],
                                                'precio': int(data[1]['producto']['precio']),
                                                'fuente': data[1]['producto']['fuente'],
                                                'fechas': data[1]['producto']['fechas'],
                                                'fechapub': data[1]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})

        elif cantidad == 3:
            precio_p = data[0]['producto']['precio']
            monto_2 = monto/3
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))

            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)


            lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                'nombrebs': data[0]['producto']['nombrebs'],
                                                'precio': int(data[0]['producto']['precio']),
                                                'fuente': data[0]['producto']['fuente'],
                                                'fechas': data[0]['producto']['fechas'],
                                                'fechapub': data[0]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})
            precio_p = data[1]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[1]['producto']['idbs'],
                                                'nombrebs': data[1]['producto']['nombrebs'],
                                                'precio': int(data[1]['producto']['precio']),
                                                'fuente': data[1]['producto']['fuente'],
                                                'fechas': data[1]['producto']['fechas'],
                                                'fechapub': data[1]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})

            precio_p = data[2]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[2]['producto']['idbs'],
                                                'nombrebs': data[2]['producto']['nombrebs'],
                                                'precio': int(data[2]['producto']['precio']),
                                                'fuente': data[2]['producto']['fuente'],
                                                'fechas': data[2]['producto']['fechas'],
                                                'fechapub': data[2]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})

        elif cantidad == 4:
            precio_p = data[0]['producto']['precio']
            monto_2 = monto/4
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))

            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)


            lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                'nombrebs': data[0]['producto']['nombrebs'],
                                                'precio': int(data[0]['producto']['precio']),
                                                'fuente': data[0]['producto']['fuente'],
                                                'fechas': data[0]['producto']['fechas'],
                                                'fechapub': data[0]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})
            precio_p = data[1]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[1]['producto']['idbs'],
                                                'nombrebs': data[1]['producto']['nombrebs'],
                                                'precio': int(data[1]['producto']['precio']),
                                                'fuente': data[1]['producto']['fuente'],
                                                'fechas': data[1]['producto']['fechas'],
                                                'fechapub': data[1]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),
                                                'img':data[0]['producto']['img']}})

            precio_p = data[2]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[2]['producto']['idbs'],
                                                'nombrebs': data[2]['producto']['nombrebs'],
                                                'precio': int(data[2]['producto']['precio']),
                                                'fuente': data[2]['producto']['fuente'],
                                                'fechas': data[2]['producto']['fechas'],
                                                'fechapub': data[2]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

            precio_p = data[3]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[3]['producto']['idbs'],
                                                'nombrebs': data[3]['producto']['nombrebs'],
                                                'precio': int(data[3]['producto']['precio']),
                                                'fuente': data[3]['producto']['fuente'],
                                                'fechas': data[3]['producto']['fechas'],
                                                'fechapub': data[3]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

        elif cantidad == 4:
            precio_p = data[0]['producto']['precio']
            monto_2 = monto/4
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))

            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)


            lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                'nombrebs': data[0]['producto']['nombrebs'],
                                                'precio': int(data[0]['producto']['precio']),
                                                'fuente': data[0]['producto']['fuente'],
                                                'fechas': data[0]['producto']['fechas'],
                                                'fechapub': data[0]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})
            precio_p = data[1]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[1]['producto']['idbs'],
                                                'nombrebs': data[1]['producto']['nombrebs'],
                                                'precio': int(data[1]['producto']['precio']),
                                                'fuente': data[1]['producto']['fuente'],
                                                'fechas': data[1]['producto']['fechas'],
                                                'fechapub': data[1]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

            precio_p = data[2]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[2]['producto']['idbs'],
                                                'nombrebs': data[2]['producto']['nombrebs'],
                                                'precio': int(data[2]['producto']['precio']),
                                                'fuente': data[2]['producto']['fuente'],
                                                'fechas': data[2]['producto']['fechas'],
                                                'fechapub': data[2]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

            precio_p = data[3]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[3]['producto']['idbs'],
                                                'nombrebs': data[3]['producto']['nombrebs'],
                                                'precio': int(data[3]['producto']['precio']),
                                                'fuente': data[3]['producto']['fuente'],
                                                'fechas': data[3]['producto']['fechas'],
                                                'fechapub': data[3]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

        elif cantidad == 5:
            precio_p = data[0]['producto']['precio']
            monto_2 = monto/5
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))

            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)


            lista_elegidos.append({'producto': {'idbs': data[0]['producto']['idbs'],
                                                'nombrebs': data[0]['producto']['nombrebs'],
                                                'precio': int(data[0]['producto']['precio']),
                                                'fuente': data[0]['producto']['fuente'],
                                                'fechas': data[0]['producto']['fechas'],
                                                'fechapub': data[0]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})
            precio_p = data[1]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[1]['producto']['idbs'],
                                                'nombrebs': data[1]['producto']['nombrebs'],
                                                'precio': int(data[1]['producto']['precio']),
                                                'fuente': data[1]['producto']['fuente'],
                                                'fechas': data[1]['producto']['fechas'],
                                                'fechapub': data[1]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

            precio_p = data[2]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[2]['producto']['idbs'],
                                                'nombrebs': data[2]['producto']['nombrebs'],
                                                'precio': int(data[2]['producto']['precio']),
                                                'fuente': data[2]['producto']['fuente'],
                                                'fechas': data[2]['producto']['fechas'],
                                                'fechapub': data[2]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

            precio_p = data[3]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[3]['producto']['idbs'],
                                                'nombrebs': data[3]['producto']['nombrebs'],
                                                'precio': int(data[3]['producto']['precio']),
                                                'fuente': data[3]['producto']['fuente'],
                                                'fechas': data[3]['producto']['fechas'],
                                                'fechapub': data[3]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})
            precio_p = data[4]['producto']['precio']
            contador = float(monto_2) / float(precio_p)
            suma = float(precio_p * int(contador))
            monton_ingresado = str(suma)
            if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                len(monton_ingresado) - 1] == '0':
                suma = int(suma)

            lista_elegidos.append({'producto': {'idbs': data[4]['producto']['idbs'],
                                                'nombrebs': data[4]['producto']['nombrebs'],
                                                'precio': int(data[4]['producto']['precio']),
                                                'fuente': data[4]['producto']['fuente'],
                                                'fechas': data[4]['producto']['fechas'],
                                                'fechapub': data[4]['producto']['fechapub'],
                                                'suma_aproximada': suma,
                                                'cantidad_veces': int(contador),'img':data[0]['producto']['img']}})

            pass

        return lista_elegidos


