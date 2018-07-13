from django import forms
from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),


        }