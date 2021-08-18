from django import forms
from .models import Nota

class NotaUsuarioForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            "titulo",
            "texto"
        ]