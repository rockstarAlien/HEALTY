# Generated by Django 4.1.1 on 2022-10-23 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_pacientedatosmedicos_actividad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientedatosmedicos',
            name='peso2',
            field=models.CharField(default='', max_length=10),
        ),
    ]