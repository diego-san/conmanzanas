from django.contrib import admin
from .models import Bienesyservicios,Region, Pais, Subcategoria,Categoria,Tipocambio


class BienesyserviciosAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idbs', 'nombrebs','precio','imgc','fuente','fechas','fechapub','id_cambio','idreg','idsubc')
    list_filter = ('nombrebs',)
    search_fields = ['nombrebs','precio']

class RegionAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idreg', 'nombreg','idpais')
    list_filter = ('nombreg',)
    search_fields = ['nombreg']

class PaisAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idpais', 'nombrep')
    list_filter = ('nombrep',)
    search_fields = ['nombrep']

class SubcategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idsubc', 'nomsc','idcat')
    list_filter = ('nomsc',)
    search_fields = ['nomsc']

class CategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idcat', 'nomcat')
    list_filter = ('nomcat',)
    search_fields = ['nomcat']




class TipocambioAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('id_cambio', 'nombrecamp')
    list_filter = ('nombrecamp',)

admin.site.register(Bienesyservicios,BienesyserviciosAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Pais,PaisAdmin)
admin.site.register(Subcategoria,SubcategoriaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Tipocambio,TipocambioAdmin)


