# Generated by Django 4.1.1 on 2022-10-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_datosreferencias'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='medico',
            field=models.BooleanField(default=True),
        ),
    ]