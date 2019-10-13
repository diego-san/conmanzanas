from django import forms




class PruebaForm(forms.Form):
    number = forms.FloatField(label='', required=True, widget=forms.TextInput(
        attrs={ 'class': 'form-control form-control-lg', 'placeholder': 'Ingresa Monto'}))







'''

 SELECCION_CATEGORIAS = [
        ('salud', 'Salud'),
        ('educacion', 'Educacion'),
        ('supermercado', 'Supermercado'),
        ('vivienda', 'Vivienda'),
        ('otros', 'Otros'),
        ('transporte', 'Transporte'),
        ('restaurant y hoteles', 'Restaurant y Hoteles'),
    ]

    Categoria = forms.MultipleChoiceField(required=True, label='', choices=SELECCION_CATEGORIAS,widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'form-check form-check-inline ', 'type':'checkbox'}))
        
        
        
        

RESCATAR DATOS DE LA BASE DE DATOS PARA TRABAJAR CON EL MODELO

class obtener(forms.ModelForm):

    class Meta:


        fields = [
            'numero',
        ]
        labels={
            'numero':'Numero'
        }
        widgets = {
            'numero': forms.NumberInput(attrs={'class':'form_control'})
        }


'''