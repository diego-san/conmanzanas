from django.db import models
import basedatos


# Create your models here.
class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=200)
    descrip = models.TextField(verbose_name='Descripción')
    cifra = models.DecimalField(max_digits=25, decimal_places=4)
    cifra_abrev = models.CharField(max_length=200, verbose_name='Cifra abreviada')
    link = models.CharField(max_length=200)
    fec_even = models.DateField(verbose_name='Fecha del evento')
    fec_moneda = models.DateField(verbose_name='Fecha de moneda')
    idreg = models.ForeignKey(basedatos.models.Region, on_delete=models.PROTECT, null=True)
    id_t = models.ForeignKey('Tema', on_delete=models.PROTECT)
    id_m = models.ForeignKey(basedatos.models.Tipocambio, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='imagen_noticias', null=True, default=None)

    class Meta:
        verbose_name = "Noticias"
        verbose_name_plural = 'Noticias'
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


class Tema (models.Model):
    id = models.AutoField(primary_key=True)
    nom_tema = models.CharField(max_length=200, verbose_name='Nombre del tema')

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = 'Temas'
        ordering = ["nom_tema"]

    def __str__(self):
        return self.nom_tema





