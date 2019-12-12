from django.db import models

class Bienesyservicios(models.Model):
   idbs = models.AutoField(primary_key=True,verbose_name="ID bien y servicio")
   nombrebs = models.TextField(max_length=250,verbose_name="Nombre servicio")
   precio = models.DecimalField(max_digits=40, decimal_places=3)
   umed = models.TextField(max_length=250, verbose_name="Tipo de unidad de medida. si no tiene poner (unidad)")
   cant_u=models.DecimalField(max_digits=15, decimal_places=3 , verbose_name="Cantidad de producto o bienes ejemplo 1,5")
   fuente = models.URLField(max_length=200, verbose_name="url de la fuente")
   fechas = models.DateField(verbose_name="Fecha de obtecion del dato")
   fechapub = models.DateField(verbose_name="Fecha de publicacion")
   id_cambio = models.ForeignKey('Tipocambio', on_delete=models.PROTECT, verbose_name="Tipo de moneda")
   idreg = models.ForeignKey('Region',on_delete=models.PROTECT, verbose_name="capitales de los paices, para chile estan todas la regiones")
   idsubc = models.ForeignKey('Subcategoria', on_delete=models.PROTECT, verbose_name="sub-categoria")
   estado = models.BooleanField('activo/inactivo', default=True)


   class Meta:
       verbose_name = "Bienesyservicios"
       verbose_name_plural = 'Bienesyservicios'
       ordering = ["nombrebs"]

   def __str__(self):
       return self.nombrebs


class Region(models.Model):
   idreg = models.AutoField(primary_key=True)
   nombreg = models.TextField(max_length=200,verbose_name="Nombre Region")
   idpais = models.ForeignKey('Pais', on_delete=models.PROTECT)

   class Meta:
       verbose_name = "Region"
       verbose_name_plural = 'Regiones'
       ordering = ["idreg"]

   def __str__(self):
       return self.nombreg

class Pais(models.Model):
   idpais = models.AutoField(primary_key=True,verbose_name="ID Pais")
   nombrep = models.TextField(max_length=200,verbose_name="Nombre Pais")

   class Meta:
       verbose_name = "Pais"
       verbose_name_plural = 'Paises'
       ordering = ["idpais"]

   def __str__(self):
       return self.nombrep

class Subcategoria(models.Model):
   idsubc = models.AutoField(primary_key=True)
   nomsc = models.TextField(max_length=200,verbose_name="Subcategoria")
   idcat = models.ForeignKey('Categoria', on_delete=models.PROTECT)
   img =  models.ImageField(upload_to='bysimg', null=True, default=None)

   class Meta:
       verbose_name = "Subcategoria"
       verbose_name_plural = 'Subcategorias'
       ordering = ["idcat"]

   def __str__(self):
       return self.nomsc

class Categoria(models.Model):
   idcat = models.AutoField(primary_key=True)
   nomcat = models.TextField(max_length=200,verbose_name="Categoria")

   class Meta:
       verbose_name = "Categoria"
       verbose_name_plural = 'Categorias'
       ordering = ["idcat"]

   def __str__(self):
       return self.nomcat



class Tipocambio(models.Model):
   id_cambio = models.AutoField(primary_key=True)
   nombrecamp = models.TextField(max_length=20,verbose_name="Moneda")


   class Meta:
       verbose_name = "Tipocambio"
       verbose_name_plural = 'Tipocambio'
       ordering = ["id_cambio"]

   def __str__(self):
       return self.nombrecamp



class Historial(models.Model):
    idh = models.AutoField(primary_key=True)
    fechh = models.DateField(verbose_name="Fecha de consulta")
    monto = models.DecimalField(max_digits=40, decimal_places=3)
    titulo = models.TextField(max_length=250, verbose_name="Tituo inrgesado", blank=True)

    def __str__(self):
        return self.fechh


class Registro(models.Model):
    idr = models.AutoField(primary_key=True)
    momp = models.DecimalField(max_digits=40, decimal_places=3)
    cant = models.PositiveIntegerField()
    idbs = models.ForeignKey('Bienesyservicios', on_delete=models.PROTECT)
    idh = models.ForeignKey('Historial', on_delete=models.PROTECT)


    def __str__(self):
        return self.idr