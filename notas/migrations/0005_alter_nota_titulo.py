# Generated by Django 3.2.5 on 2022-07-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0004_alter_nota_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
