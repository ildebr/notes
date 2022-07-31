from django.urls import path
from . import views
from django.contrib.auth import views as v
from .forms import UserLoginForm
urlpatterns = [
    path('', views.index, name='index'),
    path('nota/<int:pk>', views.NotaDetailView.as_view(), name='nota-detail'),
    #path('nota/create/', views.NotaCreate.as_view(), name='nota-create'),
    path('nota/<int:pk>/update/', views.NotaUpdate.as_view(), name='nota-update'),
    path('nota/<int:pk>/delete/', views.NotaDelete.as_view(), name='nota-delete'),
    path('notausuario', views.UsuarioNota, name='create-note'),
    path('register', views.register, name='register'),
    path('login', v.LoginView.as_view(template_name='auth/login.html', authentication_form=UserLoginForm), name='login-c'),
    path('misnotas', views.UserNotes, name='mis-notas'),
]