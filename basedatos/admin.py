from django.contrib import admin
from .models import Bienesyservicios,Region, Pais, Subcategoria,Categoria,Tipocambio


class BienesyserviciosAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idbs', 'nombrebs','precio','imgc','fuente','fechas','fechapub','id_cambio','idreg','idsubc')
    list_filter = ('nombrebs',)

class RegionAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idreg', 'nombreg','idpais')
    list_filter = ('nombreg',)

class PaisAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idpais', 'nombrep')
    list_filter = ('nombrep',)

class SubcategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idsubc', 'nomsc','idcat')
    list_filter = ('nomsc',)

class CategoriaAdmin(admin.ModelAdmin):
    #readonly_fields = ('idpais', 'nombrep')
    list_display = ('idcat', 'nomcat')
    list_filter = ('nomcat',)




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


