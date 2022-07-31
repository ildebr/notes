from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=1000,help_text="Texto de la nota")
    fecha = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    PRIVACIDAD_NOTAS = (
        ('P', 'Publico'),
        ('X', 'Privado'),
        ('C', 'Compartido'),
    )

    privacidad = models.CharField(
        max_length=1,
        choices=PRIVACIDAD_NOTAS,
        default='P',
        help_text='Privacidad de la nota'
    )

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return self.titulo + " " + str(self.usuario)

    def get_absolute_url(self):
        return reverse('nota-detail', args=[str(self.id)])

    def save_model(self, request, obj, form, change):
        obj.usuario =request.user
        super().save_model(request,obj, form,change)