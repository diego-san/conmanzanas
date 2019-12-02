from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from basedatos.models import Bienesyservicios, Region, Pais, Tipocambio, Categoria, Subcategoria, Historial, Registro
from .forms import PruebaForm
from .algoritmo import algoritmo
from datetime import datetime
from django.urls import reverse
import random



def acerca_de(request):

    context = {}
    return render(request, 'page/acerca_de.html', context)




def index(request):
    lista_categoria = ['salud', 'supermercado', 'educacion','vivienda', 'otros', 'transporte', 'restaurant y hoteles']
    datos= []


    if request.method == 'POST':
        monto = request.POST.get('monto')
        numero_a_letras(int(monto))
        categoria = request.POST.get('categoria')
        return HttpResponseRedirect('app/'+monto+'/'+categoria+'/'+'0'+'#monto')


    histo = select()
    contador = 0

    for h in histo:
        lista_r = []
        datos.append({'historial':{'monto': int(h['monto']), 'titulo': h['titulo'], 'fecha': h['fechh']}})
        regi = Registro.objects.filter(idh_id = h['idh'] ).values()
        canti_producto = len(regi)
        bien= Bienesyservicios.objects.filter(idbs= regi[0]['idbs_id']).values()
        nom_categoria = Categoria.objects.filter(idcat=Subcategoria.objects.filter(idsubc = bien[0]['idsubc_id']).values()[0]['idcat_id']).values()[0]['nomcat']
        datos[contador]['historial']['link'] = 'historial/'+str(h['idh'])+'#monto'
        datos[contador]['historial']['categoria'] = nom_categoria
        datos[contador]['historial']['cantidad'] = canti_producto
        datos[contador]['historial']['img'] = bien[0]['imgc']


        contador= 1+ contador



    context = {'datos': datos}
    return render(request, 'page/inicio.html', context)




def historial(request,id):
    prueba_form = PruebaForm()

    if request.method =='POST':
        variable = request.POST.get('monto')
        seleccion = request.POST.get('categoria').lower()
        titulo = request.POST.get('titulo')
        if titulo == '':
            titulo = '0'

        if str(str(variable).replace('.', '').isdigit()) == 'True' and str(variable).count(".") <= 1:
            variable = float(variable)
            context = {'form': prueba_form, 'dato': variable, 'monto': variable}
            if variable != 0:
                monton_ingresado = str(variable)
                if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                    len(monton_ingresado) - 1] == '0':
                    variable = int(variable)

                return HttpResponseRedirect(reverse('index')+'app/'+str(variable) + '/' + seleccion+'/'+titulo+ '#monto')

                pass

    histo = Historial.objects.filter(idh=int(id)).values()
    regi = Registro.objects.filter(idh_id = int(id)).values()

    cant_regi = len(regi)
    lista_elegidos = []
    print(id)
    for x in range(0, cant_regi):
        suma_apro = regi[x]['momp']
        cant_veces = regi[x]['cant']
        producto = Bienesyservicios.objects.filter(idbs = int(regi[x]['idbs_id'])).values()
        nom_c = Subcategoria.objects.filter(idsubc=producto[0]['idsubc_id']).values()[0]['nomsc']
        lista_elegidos.append({'producto': {'idbs': int(regi[x]['idbs_id']),
                                            'nombrebs': producto[0]['nombrebs'],
                                            'precio': int(producto[0]['precio']),
                                            'fuente': producto[0]['fuente'],
                                            'fechas': producto[0]['fechas'],
                                            'fechapub': producto[0]['fechapub'],
                                            'suma_aproximada': int(suma_apro),
                                            'cantidad_veces': cant_veces*int(producto[0]['cant_u']),
                                            'img': producto[0]['imgc'],
                                            'unidad':producto[0]['umed'],
                                            'nomcate':nom_c}})






    context = {'form': prueba_form, 'monto': histo[0]['monto'], 'consulta': lista_elegidos, 'historial': id, 'titulo': histo[0]['titulo']}

    return render(request, 'page/app.html', context)




def vista(request):
    prueba_form= PruebaForm()
    variable = ''
    context = {'form': prueba_form}
    if request.method =='POST':
        variable = request.POST.get('monto')

        seleccion = request.POST.get('categoria').lower()

        if str(str(variable).replace('.', '').isdigit()) == 'True' and str(variable).count(".") <= 1:
            variable = float(variable)
            context = {'form': prueba_form, 'dato': variable, 'monto': variable}
            if variable != 0:
                monton_ingresado = str(variable)
                if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                    len(monton_ingresado) - 1] == '0':
                    variable = int(variable)

                return HttpResponseRedirect(reverse('index')+'app/'+str(variable) + '/' + seleccion+'/'+'0'+'#monto')

                pass




    return render(request, 'page/app.html', context)



def inicio(request,monto,categoria,titulo):
    prueba_form = PruebaForm()
    variable = ''
    context = {'form': prueba_form}
    if request.method =='POST':
        monto = request.POST.get('monto')
        categoria = request.POST.get('categoria')
        titulo = request.POST.get('titulo')
        if titulo == '':
            titulo = '0'
        return HttpResponseRedirect(reverse('index')+'app/'+monto + '/' + categoria+'/'+ titulo +'#monto')

    else:

        if monto != ' ':
            variable = monto
            seleccion = categoria.lower()

            if str(str(variable).replace('.', '').isdigit()) == 'True' and str(variable).count(".") <= 1:
                variable = float(variable)
                context = {'form': prueba_form, 'dato': variable, 'monto': variable}
                if variable != 0:
                    dato_pais = Pais.objects.filter(nombrep = 'chile').values()
                    lista_id_region = []
                    dato_region = Region.objects.filter(idpais_id=dato_pais[0]['idpais']).values()
                    for id_r in dato_region:
                        lista_id_region.append(int(id_r['idreg']))


                listasubc = []
                cat = Categoria.objects.all()
                sub = Subcategoria.objects.all()

                for categ in cat:
                    nomcat = categ.nomcat
                    idca = categ.idcat

                    if nomcat == seleccion:
                        for subcategoria in sub:
                            subcategorias = subcategoria.idcat_id
                            subcategoriass = subcategoria.idsubc

                            if idca == subcategorias:
                                listasubc.append(subcategoriass)
                cantidad_productos = algoritmo.monto_dividir(float(variable))
                c = Bienesyservicios.objects.filter(precio__lte=float(variable)/cantidad_productos, idreg_id__in=lista_id_region, idsubc_id__in = listasubc).values()

                resultado = algoritmo.inicio(c, float(variable), cantidad_productos)

                if len(resultado)!=0:
                    insertar(resultado, variable, titulo)
                    histo = Historial.objects.order_by('idh').values().last()['idh']


                monton_ingresado = str(variable)
                if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                    len(monton_ingresado) - 1] == '0':
                    variable = int(variable)

                context = {'form': prueba_form, 'dato': variable, 'consulta': resultado, 'monto': variable, 'historial': histo, 'titulo': titulo}

        return render(request, 'page/app.html', context)


def categoria_random(request,monto):


    if (monto < 1000000):
        lista_categoria = ['salud', 'supermercado']
        eleccion = random.randint(0, 1)
    elif (monto > 5000000):
        lista_categoria = ['salud', 'supermercado', 'educacion', 'vivienda', 'otros', 'transporte',
                           'restaurant y hoteles']
        eleccion = random.randint(0, 6)
    else:
        lista_categoria = ['salud', 'supermercado',  'vivienda', 'otros', 'transporte',
                           'restaurant y hoteles']
        eleccion = random.randint(0, 6)


    return HttpResponseRedirect(reverse('index') + 'app/' + str(monto) + '/' + lista_categoria[eleccion] +'/' +'0' +'#monto')

def insertar(h, variable, titulo):
    fecha = datetime.today().strftime("%Y-%m-%d")
    monto = variable
    historial = Historial(None, fecha, monto, titulo)
    historial.save()
    id = Historial.objects.filter().values().last()
    for dat in h:
        guardar(dat,id)

def guardar(dat, id):
    registro = Registro(None, float(dat['producto']['suma_aproximada']), dat['producto']['cantidad_veces'], float(dat['producto']['idbs']), id['idh'])
    registro.save()






def select():
    ultimo = Historial.objects.count()
    menos_tres = ultimo-3
    return Historial.objects.filter()[menos_tres:ultimo].values()





#manejo de errores

def error_404_view(request, exception):
    data = {}
    return render(request,'page/error404.html', data)


def error_500_view(request):
    data = {}
    return render(request,'page/error500.html', data)





MAX_NUMERO = 999999999999

UNIDADES = (
    'cero',
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve'
)

DECENAS = (
    'diez',
    'once',
    'doce',
    'trece',
    'catorce',
    'quince',
    'dieciseis',
    'diecisiete',
    'dieciocho',
    'diecinueve'
)

DIEZ_DIEZ = (
    'cero',
    'diez',
    'veinte',
    'treinta',
    'cuarenta',
    'cincuenta',
    'sesenta',
    'setenta',
    'ochenta',
    'noventa'
)

CIENTOS = (
    '_',
    'ciento',
    'doscientos',
    'trescientos',
    'cuatroscientos',
    'quinientos',
    'seiscientos',
    'setecientos',
    'ochocientos',
    'novecientos'
)

def numero_a_letras(variable):
    numero_entero = int(variable)
    if numero_entero > MAX_NUMERO:
        raise OverflowError('Número demasiado alto')
    if numero_entero < 0:
        return 'menos %s' % numero_a_letras(abs(variable))
    letras_decimal = ''
    parte_decimal = int(round((abs(variable) - abs(numero_entero)) * 100))
    if parte_decimal > 9:
        letras_decimal = 'punto %s' % numero_a_letras(parte_decimal)
    elif parte_decimal > 0:
        letras_decimal = 'punto cero %s' % numero_a_letras(parte_decimal)
    if (numero_entero <= 99):
        resultado = leer_decenas(numero_entero)
    elif (numero_entero <= 999):
        resultado = leer_centenas(numero_entero)
    elif (numero_entero <= 999999):
        resultado = leer_miles(numero_entero)
    elif (numero_entero <= 999999999):
        resultado = leer_millones(numero_entero)
    else:
        resultado = leer_millardos(numero_entero)
    resultado = resultado.replace('uno mil', 'un mil')
    resultado = resultado.strip()
    resultado = resultado.replace(' _ ', ' ')
    resultado = resultado.replace('  ', ' ')
    if parte_decimal > 0:
        resultado = '%s %s' % (resultado, letras_decimal)
    print(resultado)
    return resultado


def leer_decenas(variable):
    if variable < 10:
        return UNIDADES[variable]
    decena, unidad = divmod(variable, 10)
    if variable <= 19:
        resultado = DECENAS[unidad]
    elif variable == 20:
        resultado = 'veinte'
    elif variable <= 29:
        resultado = 'veinti%s' % UNIDADES[unidad]
    else:
        resultado = DIEZ_DIEZ[decena]
        if unidad > 0:
            resultado = '%s y %s' % (resultado, UNIDADES[unidad])
    return resultado

def leer_centenas(variable):
    centena, decena = divmod(variable, 100)
    if variable == 100:
        resultado = 'cien'


    else:
        resultado = CIENTOS[centena]
        if decena > 0:
            resultado = '%s %s' % (resultado, leer_decenas(decena))

    return resultado

def leer_miles(variable):
    millar, centena = divmod(variable, 1000)
    resultado = ''
    if (millar == 1):
        resultado = ''
    if (millar >= 2) and (millar <= 9):
        resultado = UNIDADES[millar]
    elif (millar >= 10) and (millar <= 99):
        resultado = leer_decenas(millar)
    elif (millar >= 100) and (millar <= 999):
        resultado = leer_centenas(millar)
    resultado = '%s mil' % resultado

    if centena > 0:
        resultado = '%s %s' % (resultado, leer_centenas(centena))

    return resultado

def leer_millones(variable):
    millon, millar = divmod(variable, 1000000)
    resultado = ''
    if (millon == 1):
        resultado = ' un millon '
    if (millon >= 2) and (millon <= 9):
        resultado = UNIDADES[millon]
    elif (millon >= 10) and (millon <= 99):
        resultado = leer_decenas(millon)
    elif (millon >= 100) and (millon <= 999):
        resultado = leer_centenas(millon)
    if millon > 1:
        resultado = '%s millones' % resultado
    if (millar > 0) and (millar <= 999):
        resultado = '%s %s' % (resultado, leer_centenas(millar))
    elif (millar >= 1000) and (millar <= 999999):
        resultado = '%s %s' % (resultado, leer_miles(millar))

    return resultado

def leer_millardos(variable):
    millardo, millon = divmod(variable, 1000000)
    return '%s millones %s' % (leer_miles(millardo), leer_millones(millon))
