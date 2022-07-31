from django import forms
from .models import Nota
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

class NotaUsuarioForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            "titulo",
            "texto"
        ]

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'name@address.com'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'juan123'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '*********'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '*********'})

    class Meta:
        model = User
        fields = ("username", "email")
    
    def save(self,commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'user', 'placeholder': 'Username', 'id': 'user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': '******'}))