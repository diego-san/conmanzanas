from django.urls import path

from django.conf.urls import handler404, handler500
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/<int:monto>/<categoria>', views.inicio, name='inicio'),
    path('inicio/',views.vista, name="vista2"),
    path('vista/', views.vista, name='vista'),
    path('historial/<int:id>', views.historial, name='historial'),

]



