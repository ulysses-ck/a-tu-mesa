from django import forms
from django.contrib.auth.models import User
from apps.persona.models import Persona
from apps.rol.models import Rol

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class PersonaForm(forms.ModelForm):
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        empty_label="Seleccione un Rol",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'correo', 'telefono','documento']