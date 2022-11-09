# Generated by Django 4.1.1 on 2022-10-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_login_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='00000', max_length=6)),
                ('nombre', models.CharField(default='arturo', max_length=30)),
                ('apellidop', models.CharField(default='zenteno', max_length=30)),
                ('apellidom', models.CharField(default='lima', max_length=30)),
                ('gender', models.CharField(default='hombre', max_length=10)),
                ('telefono', models.CharField(default='1234567890', max_length=10)),
                ('fecha', models.CharField(default='2/09/18', max_length=15)),
                ('codigopostal', models.CharField(default='90340', max_length=10)),
                ('estado', models.CharField(default='tlaxcala', max_length=30)),
                ('municipio', models.CharField(default='apizaco', max_length=30)),
                ('calle', models.CharField(default='allende # 133', max_length=30)),
                ('numex', models.CharField(default='3-B', max_length=10)),
                ('numint', models.CharField(default='3b', max_length=10)),
            ],
        ),
    ]
