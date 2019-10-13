from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from basedatos.models import Bienesyservicios, Region, Pais, Tipocambio, Categoria, Subcategoria, Historial, Registro
from .forms import PruebaForm
from .calculo import calculo
import random

def test():
    variable = "funca"



test()
