from django.shortcuts import render
from .models import Nota
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from .forms import NotaUsuarioForm, NewUserForm, UserLoginForm
from django.urls import reverse
# Create your views here.

def index(request):
    notas = Nota.objects.filter(privacidad='P').order_by('-fecha')

    context = {
        'notas' : notas,
    }

    return render(request, 'index.html', context)

def landing(request):
    return render(request, 'landing.html')

class NotaDetailView(generic.DetailView):
    model = Nota
"""
class NotaCreate(CreateView):
    model = Nota
    fields = ['titulo', 'texto']
    def save_model(self,request,obj,form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()
"""

class NotaUpdate(UpdateView):
    model = Nota
    # fields = ['titulo', 'texto']
    form_class = NotaUsuarioForm
    

class NotaDelete(LoginRequiredMixin,DeleteView):
    model = Nota
    success_url = reverse_lazy('index')

def UserNotes(request):
    notas = Nota.objects.filter(usuario=request.user).order_by('-fecha')

    context = {
        'notas':notas,
    }
    return render(request, 'notas/notas_de_usuario.html', context)

"""
class NotesListView(generic.ListView,LoginRequiredMixin):
    model = Nota
    context_object_name = "my_notes"
    queryset = Nota.objects.filter(usuario=request.user.id)
    template_name= 'notas/notas_de_usuario.html'
"""

def register(request):
    if request.method == 'POST':
        f = NewUserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,'account created')
            return HttpResponseRedirect(reverse('login'))
    else:
        f = NewUserForm()
    return render(request,'auth/register.html', {'form': f})


def login(request):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,'Login Successful')
            return HttpResponseRedirect(reverse('index'))
    else:
        f = UserLoginForm()
    return render(request,'auth/login.html', {'form': f})

# def login(request):
#     if request.method == "POST":
#         f = UserLoginForm(request.POST)
#         if f.is_valid():
            

def UsuarioNota(request):
    form = NotaUsuarioForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':

        if form.is_valid():
            obj = form.save(commit = False)
            """
            if (request.user == None or not request.user.is_authenticated()):
                obj.usuario = None
            else:
                obj.usuario = request.user"""
            print(obj.usuario)
            if request.user.is_authenticated:
                obj.usuario = request.user
                obj.privacidad = 'X'
            else:
                obj.usuario = None
            obj.save()
            form = NotaUsuarioForm()
            messages.success(request, "successsfully")

            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('mis-notas'))
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'notas/form.html', {'form':form})

