# Generated by Django 3.2.5 on 2021-08-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='texto',
            field=models.TextField(help_text='Texto de la nota', max_length=1000),
        ),
    ]
