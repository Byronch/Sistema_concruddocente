from django import forms
from.models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'edad', 'email', 'user', 'sexo']

class DocenteFormBasico(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo', max_length=30)