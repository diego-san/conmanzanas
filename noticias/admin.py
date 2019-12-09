from django.contrib import admin
from .models import Noticia, Tema

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descrip','cifra', 'cifra_abrev', 'link', 'fec_even', 'fec_moneda', 'id_t', 'id_m', 'idreg', 'imagen_n')
    list_filter = ('titulo',  )
    search_fields = ['titulo', 'cifra']

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nom_tema',)
    list_filter = ('nom_tema',)
    search_fields = ['nom_tema']


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Tema, TemaAdmin)

