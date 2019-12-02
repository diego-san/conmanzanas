from django.urls import path

from django.conf.urls import handler404, handler500
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:monto>',views.categoria_random, name='iniciocategoria_random'),
    path('app/<int:monto>/<categoria>', views.inicio, name='inicio'),
    path('app/<int:monto>', views.categoria_random, name='categoria_random'),
    path('app/',views.vista, name="vista"),
    path('historial/<int:id>', views.historial, name='historial'),
    path('Acerca_De/', views.acerca_de, name='acerca_de'),

]



