from email import generator
import email
from email.policy import default
from msilib.schema import MsiDigitalSignature
from pyexpat import model
from subprocess import CalledProcessError
from tkinter import commondialog
from turtle import mode
from django.db import models

# Create your models here.

class RegisterGeneral(models.Model):
     codigo = models.CharField(max_length = 10, default='')
     email = models.CharField(max_length = 40, default='')
     password = models.CharField(max_length=15, default='')
     tipo = models.CharField(max_length= 15, default='')

class Login(models.Model):
    nombre = models.CharField(max_length = 30, default = 'arturo')
    apellidop = models.CharField(max_length = 30, default = 'zenteno')
    apellidom = models.CharField(max_length = 30, default = 'lima')
    email = models.CharField(max_length =30, default = 'algo@mail.com')
    password = models.CharField(max_length = 10, default = 'hola123')
    codigo = models.CharField(max_length=6, default= '00000')
    medico = models.BooleanField(default = True)

class LoginPaciente(models.Model):
    nombre = models.CharField(max_length = 30, default='arturo')
    apellidop = models.CharField(max_length = 30, default='zenteno')
    apellidom = models.CharField(max_length = 30, default = 'lima')
    email = models.CharField(max_length=30, default = 'algomas@mail.com') 
    password = models.CharField(max_length=30, default='hola123') 
    codigo = models.CharField(max_length=6, default='1212')
    paciente = models.BooleanField(default = True)

class PacienteDatosPersonales(models.Model):
    codigo = models.CharField(max_length=6, default='01233')
    nombre = models.CharField(max_length=30, default='arturo') 
    apellidop = models.CharField(max_length=30, default='lima')
    apellidom = models.CharField(max_length=30, default='lima')
    gender = models.CharField(max_length=10, default='hombre')
    telefono = models.CharField(max_length=10, default='12345689')
    fecha = models.CharField(max_length=15, default='0909122')
    codigopostal = models.CharField(max_length=10, default='90340')
    estado = models.CharField(max_length=30, default='tlaxcala') 
    municipio = models.CharField(max_length=30, default='apizaco')
    calle = models.CharField(max_length=30, default='allende') 
    numex = models.CharField(max_length=10, default='344')
    numint = models.CharField(max_length=10, default='A')

class PacienteDatosMedicos(models.Model):
    codigo = models.CharField(max_length=6, default='')
    peso = models.CharField(max_length=10, default='')
    estatura = models.CharField(max_length=10, default='')
    diabetes = models.CharField(max_length=20, default='')
    gruposangre = models.CharField(max_length=20, default='')
    padecimientos = models.CharField(max_length=200, default='')
    peso2 = models.CharField(max_length = 10, default='')
    cintura  = models.CharField(max_length = 10, default='')
    alimentacion  = models.CharField(max_length = 200, default='')
    actividad  = models.CharField(max_length = 200, default='')
    antecedentes  = models.CharField(max_length = 200, default='')
    sueno  = models.CharField(max_length = 100, default='')
    humo  = models.CharField(max_length = 100, default='')
    arterial  = models.CharField(max_length = 30, default='')
    colesterol  = models.CharField(max_length = 30, default='')
    triglice = models.CharField(max_length = 30, default='')


class PacienteContactosEmergencia(models.Model):
    codigo = models.CharField(max_length=6, default='') 
    contacto1 = models.CharField(max_length=100, default='')
    contacto2 = models.CharField(max_length=100, default='')
    contacto3 = models.CharField(max_length=100, default='')


class DatosPersonales(models.Model):
    codigo = models.CharField(max_length = 6, default='00000')
    nombre = models.CharField(max_length = 30, default = 'arturo')
    apellidop = models.CharField(max_length = 30, default = 'zenteno')
    apellidom = models.CharField(max_length = 30, default = 'lima')
    gender = models.CharField(max_length = 10, default = 'hombre')
    telefono= models.CharField(max_length = 10, default ='1234567890')
    fecha = models.CharField(max_length = 15, default='2/09/18')
    codigopostal = models.CharField(max_length = 10, default='90340')
    estado = models.CharField(max_length = 30, default= 'tlaxcala')
    municipio = models.CharField(max_length = 30, default= 'apizaco')
    calle = models.CharField(max_length = 30, default = 'allende # 133')
    numex = models.CharField(max_length = 10, default = '3-B')
    numint = models.CharField(max_length = 10, default = '3b')    


class DatosProfesionales(models.Model):
    codigo = models.CharField(max_length=30, default='')
    universidad = models.CharField(max_length=30, default='')
    carrera = models.CharField(max_length = 40, default='')
    especialidad = models.CharField(max_length=30, default='')
    cedula = models.CharField(max_length = 30, default='')

class DatosReferencias(models.Model):
    codigo = models.CharField(max_length=30, default='')
    referencia1 = models.CharField(max_length=100, default='')
    referencia2 = models.CharField(max_length=100, default='')
    referencia3 = models.CharField(max_length=100, default='')


class Person(models.Model):
    cod = models.CharField(max_length=30, default='00001')
    nombre = models.CharField(max_length=40, default="arturoo")


class GeneralDataTable(models.Model):
    cod = models.CharField(max_length=10, default='1')
    estatura = models.CharField(max_length=30, default='100')
    peso = models.CharField(max_length=30, default='90')
    cintura =  models.CharField(max_length=30, default='65')
    arterial = models.CharField(max_length=30, default='120')
    colesterol = models.CharField(max_length=30, default='90')
    triglicelidos = models.CharField(max_length=30, default='190')

    max_estatura = models.CharField(max_length=30, default='140')
    max_peso = models.CharField(max_length=30, default='120')
    max_cintura =  models.CharField(max_length=30, default='85')
    max_arterial = models.CharField(max_length=30, default='150')
    max_colesterol = models.CharField(max_length=30, default='120')
    max_triglicelidos = models.CharField(max_length=30, default='210')



class Carausel(models.Model):
    image = models.ImageField(upload_to = 'media/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class cita(models.Model):
    cod = models.CharField(max_length=15, default="")
    sintomas = models.CharField(max_length=200, default="")
    fecha=  models.CharField(max_length=150, default="")
    hora=  models.CharField(max_length=150, default="")
    cod_user = models.CharField(max_length=10, default="")
    disponibilidad = models.BooleanField(default= True)




    