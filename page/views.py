from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from basedatos.models import Bienesyservicios, Region, Pais, Tipocambio, Categoria, Subcategoria, Historial, Registro
from .forms import PruebaForm
from .calculo import calculo
from .algoritmo import algoritmo
from datetime import datetime
from django.urls import reverse
import random


def index(request):
    lista_categoria = ['salud', 'supermercado', 'educacion','vivienda', 'otros', 'transporte', 'restaurant y hoteles']
    datos= []


    if request.method == 'POST':
        monto = request.POST.get('monto')
        categoria = request.POST.get('categoria')
        return HttpResponseRedirect('app/'+monto+'/'+categoria+'#monto')


    histo = select()
    contador = 0

    for h in histo:

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

        if str(str(variable).replace('.', '').isdigit()) == 'True' and str(variable).count(".") <= 1:
            variable = float(variable)
            context = {'form': prueba_form, 'dato': variable, 'monto': variable}
            if variable != 0:
                monton_ingresado = str(variable)
                if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                    len(monton_ingresado) - 1] == '0':
                    variable = int(variable)

                return HttpResponseRedirect(reverse('index')+'app/'+str(variable) + '/' + seleccion)

                pass

    histo = Historial.objects.filter(idh=int(id)).values()

    regi = Registro.objects.filter(idh_id = int(id)).values()
    print(regi)
    cant_regi = len(regi)
    lista_elegidos = []

    for x in range(0, cant_regi):
        suma_apro = regi[x]['momp']
        cant_veces = regi[x]['cant']
        producto = Bienesyservicios.objects.filter(idbs = int(regi[x]['idbs_id'])).values()

        lista_elegidos.append({'producto': {'idbs': int(regi[x]['idbs_id']),
                                            'nombrebs': producto[0]['nombrebs'],
                                            'precio': int(producto[0]['precio']),
                                            'fuente': producto[0]['fuente'],
                                            'fechas': producto[0]['fechas'],
                                            'fechapub': producto[0]['fechapub'],
                                            'suma_aproximada': suma_apro,
                                            'cantidad_veces': cant_veces,
                                            'img': producto[0]['imgc']}})






    context = {'form': prueba_form, 'monto': histo[0]['monto'], 'consulta': lista_elegidos}

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

                return HttpResponseRedirect(reverse('index')+'app/'+str(variable) + '/' + seleccion+'#monto')

                pass




    return render(request, 'page/app.html', context)



def inicio(request,monto,categoria):
    prueba_form = PruebaForm()
    variable = ''
    context = {'form': prueba_form}
    if request.method =='POST':
        monto = request.POST.get('monto')
        categoria = request.POST.get('categoria')
        return HttpResponseRedirect(reverse('index')+'app/'+monto + '/' + categoria+'#monto')

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
                    insertar(resultado, variable)

                monton_ingresado = str(variable)
                if monton_ingresado[len(monton_ingresado) - 2] == '.' and monton_ingresado[
                    len(monton_ingresado) - 1] == '0':
                    variable = int(variable)

                context = {'form': prueba_form, 'dato': variable, 'consulta': resultado, 'monto': variable}

        return render(request, 'page/app.html', context)


def categoria_random(request,monto):
    lista_categoria = ['salud', 'supermercado', 'educacion', 'vivienda', 'otros', 'transporte', 'restaurant y hoteles']
    eleccion = random.randint(0,6)
    return HttpResponseRedirect(reverse('index') + 'app/' + str(monto) + '/' + lista_categoria[eleccion] + '#monto')

def insertar(h, variable):
    fecha = datetime.today().strftime("%Y-%m-%d")
    titulo = 'titulo'
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


def error_500_view(request, exception):
    data = { }
    return render(request,'page/error500.html', data)