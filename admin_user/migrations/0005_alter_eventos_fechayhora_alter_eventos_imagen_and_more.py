# Generated by Django 4.2.7 on 2023-11-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0004_delete_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fechayhora',
            field=models.DateTimeField(verbose_name='Fecha y Hora'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='imagen',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
    ]
