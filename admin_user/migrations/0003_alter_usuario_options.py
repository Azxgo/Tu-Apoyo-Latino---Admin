# Generated by Django 4.2.7 on 2023-11-08 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0002_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['nombre', 'correo', 'password', 'creado'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
