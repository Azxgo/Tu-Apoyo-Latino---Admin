# Generated by Django 4.2.7 on 2023-11-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='asistentes',
            field=models.ManyToManyField(to='admin_user.usuario'),
        ),
    ]
