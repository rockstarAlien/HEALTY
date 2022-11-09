import code
from curses import erasechar
from distutils.ccompiler import new_compiler
import email
import io
from django.http import FileResponse
from operator import ge
from sqlite3 import DatabaseError
from tempfile import gettempdir
from django.shortcuts import redirect, reverse
from django.shortcuts import render
from django.http import HttpResponse
from .models import DatosPersonales, Login, DatosProfesionales, DatosReferencias, LoginPaciente, PacienteDatosPersonales, PacienteDatosMedicos, PacienteContactosEmergencia, RegisterGeneral, GeneralDataTable, Carausel, cita
from multiprocessing import context
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# Create your views here.
def create_pdf(request):
    #crear el buffer de bytestram
    buf = io.BytesIO()
    #crear el canvas
    c = canvas.Canvas(buf, pagesize =letter, bottomup=0)
    #creando el objeto txt
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    #lines

    lines = [
        "line1",
        "line2",
        "line3"
    ]


    #loop
    for line in lines:
        textob.textLine(line)

    #finish
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    #rreturn somethin

    return FileResponse(buf, as_attachment=True, filename='archivo.pdf')


# Create your views here.
def generatePDF(request, id):
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    x.drawString(100, 100, "Let's generate this pdf file.")
    x.showPage()
    x.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')

def home_view(request):
    obj = Carausel.objects.all()

    logged = False

    context = {
        'iniciado': logged,
        'carousel': obj
    }

    return render(request, 'registros/home.html', context)

def profiel_view(request, pk):
    user_id = RegisterGeneral.objects.get(codigo=pk)
    user_data = DatosPersonales.objects.get(codigo=pk)
    user_profesional = DatosProfesionales.objects.get(codigo=pk)
    

    context = {

        'user':user_data,
        'user2': user_id,
        'profesion': user_profesional
    }

    

    return render(request, 'registros/profile.html', context)

def login_view(request):
    #user = Login.objects.get(all)
    #user_mail = Login.objects.get('email')
    #user = Login.objects.get(id='1')


    if request.POST:

        try_user_mail = request.POST.get('mail')
        try_user_pass = request.POST.get('pass')

        user_pass = RegisterGeneral.objects.filter(email=try_user_mail).order_by('email').values_list('password', flat=True)[:1]
        user_pass = list(user_pass)

        user_id = RegisterGeneral.objects.get(email=try_user_mail)

        neo_userid= user_id.codigo

        getteduser_pass = user_pass[0]

        user_type = RegisterGeneral.objects.get(email=try_user_mail)
        user_type_data = user_type.tipo

        print('--------')
        print(user_type_data)
        

        print('*****')
        print(try_user_mail)
        print('******')
        print('La contraseña es')
        print(user_pass[0])
        print('*******')
        print('el id es')
        print(neo_userid)


        estado = 1

        if try_user_pass == getteduser_pass:
            print("felicidades")

            if user_type_data == 'medico':
                return redirect(reverse('profile-view', args=[neo_userid]))
            if user_type_data == 'paciente':
                #return redirect(reverse('profile-paciente-view', args=[neo_userid]))
                return redirect(reverse('home-dos-view', args=[estado, neo_userid]))



        else:
            print("nooo") 

            context = {
                'message': 'error, no coincidde'
            }
          

            return render(request, 'registros/login.html', context)




    else:
        print('*****')
        print("no hay post")
        print('*****')


    passs = True
    
    return render(request, 'registros/login.html')

    #return render(request, 'registros/login.html', context)

def register_view(request):
    return render(request, 'registros/register.html')

def register2_view(request):

    password = request.POST.get('passwords')
    confirmation = request.POST.get('password2')


    if request.POST:
        #register_name = request.POST.get('names')
        #register_apellidop = request.POST.get('apellidop')
        #register_apellidom = request.POST.get('apellidom')
        #register_email = request.POST.get('email')
        #register_pass = request.POST.get('password')
        #register_pass2 = request.POST.get('password2')
        #register_cod = request.POST.get('codigo')

        #context = {
        #'message': 'hola',
        #'users': Login.objects.all()
        #}

        print(Login.objects.all())


    if request.POST:
        new_user = request.POST.get('names')
        new_apellidop = request.POST.get('apellidops')
        new_apellidom = request.POST.get('apellidoms')
        new_email = request.POST.get('emails')
        new_pass = request.POST.get('passwords')
        new_codigo = request.POST.get('codigo')

        Login.objects.create(nombre = new_user, apellidop = new_apellidop, apellidom = 'lima', email = new_email, password = new_pass,
        codigo = new_codigo)

        DatosPersonales.objects.create(codigo=new_codigo, nombre=new_user, apellidop= new_apellidop, apellidom='lima')

        DatosProfesionales.objects.create(codigo = new_codigo)

        DatosReferencias.objects.create(codigo=new_codigo)

        RegisterGeneral.objects.create(codigo=new_codigo, email=new_email, password=new_pass,tipo='medico')

        print('-------')
        print(new_codigo)

        return redirect(reverse('register3-view', args=[new_codigo]))


    return render(request, 'registros/register2.html')

def register3_view(request, pk):


    user_cod = DatosPersonales.objects.filter(codigo=pk).order_by('codigo').values_list('codigo', flat=True)[:1]
    #neo_usercod = user_cod.codigo
    neo_usercod = list(user_cod)
    nn_usercod = neo_usercod[0]

    user_prof_data = DatosProfesionales.objects.get(codigo=nn_usercod)


    #user_id = Login.objects.get(codigo=pk)
    user_id = DatosPersonales.objects.get(codigo=pk)
    user_prof_id = DatosProfesionales.objects.get(codigo=pk)

    #neo_userid= user_id.id
    user_personal_cod = DatosPersonales.objects.get(codigo=nn_usercod)
    user_personal_id = user_personal_cod.codigo

    user_reference_id = DatosReferencias.objects.get(codigo=pk)


    

    print('**********')
    print(user_cod)
    print('---------')
    print(neo_usercod)
    print('************')
    print(nn_usercod)

    context = {
        'user': user_id,
        'profesion': user_prof_id,
        'reference': user_reference_id
    }

    if request.POST:
        if 'savePersonal' in request.POST:
            userPer = DatosPersonales.objects.get(codigo=nn_usercod)


            new_code = nn_usercod
            new_name = request.POST.get('namess')
            new_apellidop = request.POST.get('apellidopp')
            new_apellidom = request.POST.get('apellidomm')
            new_gender = 'hombre'
            new_telefono = request.POST.get('telefonos')
            new_fecha = '02/09/18'
            new_codigopostal = request.POST.get('cp')
            new_estado = request.POST.get('estado')
            new_municipio = request.POST.get('municipio')
            new_calle = request.POST.get('calle')
            new_numex = request.POST.get('numex')
            new_numint = request.POST.get('numint')

            print("si ghay post")

            userPer.codigo = new_code
            userPer.nombre = new_name
            userPer.apellidop = new_apellidop
            userPer.apellidom = new_apellidom
            userPer.gender = new_gender
            userPer.telefono = new_telefono
            userPer.fecha = new_fecha
            userPer.codigopostal = new_codigopostal
            userPer.estado = new_estado
            userPer.municipio = new_municipio
            userPer.calle = new_calle
            userPer.numex = new_numex
            userPer.numint = new_numint
            userPer.save()
            
            #DatosPersonales.objects.create(codigo=new_code, nombre=new_name, apellidop=new_apellidop, apellidom=new_apellidom, gender=new_gender, telefono=new_telefono,
            #fecha=new_fecha, codigopostal=new_codigopostal, estado=new_estado, municipio=new_municipio, calle=new_calle, numex=new_numex, numint=new_numint)

            #return redirect(reverse('register3-view', args=[new_code]))

        if 'saveProfesional' in request.POST:
            print('hola')
            data_user_profesional= DatosProfesionales.objects.get(codigo=nn_usercod)

            nuevo_codigo = nn_usercod
            new_universidad = request.POST.get('universidad')
            new_carrera = request.POST.get('carrera')
            new_especialidad = request.POST.get('especialidad')
            new_cedula = request.POST.get('cedula')

            #DatosProfesionales.objects.create(codigo=nuevo_codigo, universidad=new_universidad, carrera=new_carrera, especialidad=new_especialidad,cedula='holaaaa')
            data_user_profesional.codigo = nn_usercod
            data_user_profesional.universidad = new_universidad
            data_user_profesional.carrera = new_carrera
            data_user_profesional.especialidad = new_especialidad
            data_user_profesional.cedula = 'xxxxxxsss56'

            data_user_profesional.save()

        if 'saveReferencias' in request.POST:
            data_user_referencia = DatosReferencias.objects.get(codigo=nn_usercod)

            new_refe1 = request.POST.get('referencia')
            new_refe2 = request.POST.get('referencia2')
            new_refe3 = request.POST.get('referencia3')

            data_user_referencia.codigo = nn_usercod
            data_user_referencia.referencia1 = new_refe1
            data_user_referencia.referencia2 = new_refe2
            data_user_referencia.referencia3 = new_refe3

            data_user_referencia.save()


    else:
        print('*****')
        print('no post :(')




    return render(request, 'registros/register3.html', context)

def register_user_view(request, pk):
    
    pacient_code = LoginPaciente.objects.get(codigo=pk)
    pacient_personal = PacienteDatosPersonales.objects.get(codigo=pk)
    paciente_medical_id = PacienteDatosMedicos.objects.get(codigo=pk)
    paciente_contactos_id = PacienteContactosEmergencia.objects.get(codigo=pk)

    context = {
        'paciente': pacient_personal,
        'medical': paciente_medical_id,
        'contacto': paciente_contactos_id,
        
    }

    if request.POST:
        if 'savePacientPersonal' in request.POST:
            print('boton1 om')
            pacient_personal_data = PacienteDatosPersonales.objects.get(codigo=pk)

            gneero = request.POST.get('empname')


            #print('-------')
            #print(gneero)

            if gneero == '1':
                gneero = 'hombre'
            elif gneero == '2':
                gneero = 'mujer'
            elif gneero == '3':
                gneero = 'otro'

            #print('++++++')
            #print(gneero)
            new_code = pk
            new_name = request.POST.get('namess')
            new_apellidop = request.POST.get('apellidopp')
            new_apellidom = request.POST.get('apellidomm')
            new_gender = gneero
            new_telefono = request.POST.get('telefono')
            new_fecha = '090218'
            new_codigoposta = request.POST.get('cp')
            new_estado = request.POST.get('estado')
            new_municipio = request.POST.get('municipio')
            new_calle = request.POST.get('calle')
            new_numex = request.POST.get('numex')
            new_numint = request.POST.get('numint')

            pacient_personal_data.codigo = new_code
            pacient_personal_data.nombre = new_name
            pacient_personal_data.apellidop = new_apellidop
            pacient_personal_data.apellidom = new_apellidom
            pacient_personal_data.gender = new_gender
            pacient_personal_data.telefono = new_telefono
            pacient_personal_data.fecha = new_fecha
            pacient_personal_data.codigopostal = new_codigoposta
            pacient_personal_data.estado = new_estado
            pacient_personal_data.municipio = new_municipio
            pacient_personal_data.calle = new_calle
            pacient_personal_data.numex = new_numex
            pacient_personal_data.numint = new_numint

            pacient_personal_data.save()
        
        if 'saveMedical' in request.POST:
            print('boton 2 ok')
            pacient_medical_data = PacienteDatosMedicos.objects.get(codigo=pk)

            print('*******')
            print(pacient_medical_data)

            sdiabetes = request.POST.get('empdiabetes')
            sSangre = request.POST.get('empsangre')
            sAliment = request.POST.get('empalimentacion')
            sActividad = request.POST.get('empactividad')
            sAntece = request.POST.get('empantecedentes')
            sSueno = request.POST.get('empsueno')
            sHumo = request.POST.get('emphumo')

            if sdiabetes == '1':
                sdiabetes = 'Tipo 1'
            elif sdiabetes == '2':
                sdiabetes = 'Tipo 2'
            elif sdiabetes == '3':
                sdiabetes = 'Gestacional'
            elif sdiabetes == '4':
                sdiabetes = 'LADA'


            if sSangre == '1':
                sSangre = 'A'
            elif sSangre == '2':
                sSangre = 'B'
            elif sSangre == '3':
                sSangre = 'AB'
            elif sSangre == '4':
                sSangre = 'O'

            if sAliment == '1':
                sAliment = 'Mucho'
            elif sAliment == '2':
                sAliment = 'Poco'
            elif sAliment == '3':
                sAliment = 'Nada'

            if sActividad == '1':
                sActividad = 'Mucho'
            elif sActividad == '2':
                sActividad = 'Poco'
            elif sActividad == '3':
                sActividad = 'Nada'

            if sAntece == '1':
                sAntece = 'Mucho'
            elif sAntece == '2':
                sAntece = 'Poco'
            elif sAntece == '3':
                sAntece = 'Nada'

            if sSueno == '1':
                sSueno = 'Mucho'
            elif sSueno == '2':
                sSueno = 'Poco'
            elif sSueno == '3':
                sSueno = 'Nada'

            if sHumo == '1':
                sHumo = 'Mucho'
            elif sHumo == '2':
                sHumo = 'Poco'
            elif sHumo == '3':
                sHumo = 'Nada'





            

            n_codigo = pk
            new_peso = request.POST.get('peso')
            new_estatura = request.POST.get('estatura')
            new_diabetes = sdiabetes
            new_sangre = sSangre
            new_padecimiento = request.POST.get('padecimiento')
            new_cintura = request.POST.get('cintura')
            new_alimentacion = sAliment
            new_actividad = sActividad
            new_antecedentes = sAntece
            new_sueno = sSueno
            new_humo = sHumo
            new_arterial = request.POST.get('arterial')
            new_colesterol = request.POST.get('colesterol')
            new_triglice = request.POST.get('triglicelidos')

            pacient_medical_data.codigo = n_codigo
            pacient_medical_data.peso = new_peso
            pacient_medical_data.estatura = new_estatura
            pacient_medical_data.diabetes = new_diabetes
            pacient_medical_data.gruposangre = new_sangre
            pacient_medical_data.padecimientos = new_padecimiento
            pacient_medical_data.cintura = new_cintura
            pacient_medical_data.alimentacion = new_alimentacion
            pacient_medical_data.actividad = new_actividad
            pacient_medical_data.antecedentes = new_antecedentes
            pacient_medical_data.sueno = new_sueno
            pacient_medical_data.humo = new_humo
            pacient_medical_data.arterial = new_arterial
            pacient_medical_data.colesterol = new_colesterol
            pacient_medical_data.triglice = new_triglice


            pacient_medical_data.save()

        if 'saveContactos' in request.POST:
            pacient_contactos = PacienteContactosEmergencia.objects.get(codigo=pk)

            new_contacto = request.POST.get('referencia')
            new_contacto2 = request.POST.get('referencia2')
            new_contacto3 = request.POST.get('referencia3')

            pacient_contactos.codigo = pk
            pacient_contactos.contacto1 = new_contacto
            pacient_contactos.contacto2 = new_contacto2
            pacient_contactos.contacto3 = new_contacto3

            pacient_contactos.save()




    return render(request, 'registros/registeruser.html', context)

def register_pacient_view(request):

    if request.POST:

        name = request.POST.get('names')
        apellidop = request.POST.get('apellidops')
        apellidom = request.POST.get('apellidoms')
        emails =  request.POST.get('emails')
        password = request.POST.get('passwords')
        codigo = request.POST.get('codigo')

        LoginPaciente.objects.create(nombre=name, apellidop=apellidop, apellidom=apellidom, email=emails, password=password,
        codigo=codigo)

        PacienteDatosPersonales.objects.create(codigo=codigo, nombre=name, apellidop=apellidop, apellidom=apellidom)

        PacienteDatosMedicos.objects.create(codigo=codigo)

        PacienteContactosEmergencia.objects.create(codigo=codigo)

        #create general logins

        RegisterGeneral.objects.create(codigo=codigo, email=emails, password=password, tipo='paciente')



        print('*****')
        print('exito!!!')

        return redirect(reverse('register-user-view', args=[codigo]))

        #return redirect(reverse('register3-view', args=[new_codigo]))



    return  render(request, 'registros/registerpacient.html')

def modify_contact_view(request, pk):

    user_data = DatosPersonales.objects.get(codigo=pk)

    context = {
        'user': user_data

    }

    if request.POST:
        user_data_save = DatosPersonales.objects.get(codigo=pk)

        new_telefono = request.POST.get('telefonos')
        new_fecha = request.POST.get('fecha')
        new_cp = request.POST.get('cp') 
        new_estado = request.POST.get('estado')
        new_municipio = request.POST.get('municipio')
        new_calle = request.POST.get('calle')
        new_numex = request.POST.get('numex')
        new_numint = request.POST.get('numint')

        user_data_save.telefono = new_telefono
        user_data_save.fecha = new_fecha
        user_data_save.codigopostal = new_cp
        user_data_save.estado = new_estado
        user_data_save.municipio = new_municipio
        user_data_save.calle = new_calle
        user_data_save.numex = new_numex
        user_data_save.numint = new_numint

        user_data_save.save()

        return redirect(reverse('profile-view', args=[pk]))


    return  render(request, 'registros/modcontacto.html', context)

def modify_profesion_view(request, pk):
    user_data = DatosProfesionales.objects.get(codigo=pk)

    context = {
        'profesion': user_data
    }

    if request.POST:
        save_data = DatosProfesionales.objects.get(codigo=pk)

        new_universidad = request.POST.get('universidad')
        new_carrera = request.POST.get('carrera')
        new_especialidad = request.POST.get('especialidad')
        new_cedula = request.POST.get('cedula')

        save_data.universidad = new_universidad
        save_data.carrera = new_carrera
        save_data.especialidad = new_especialidad
        save_data.cedula = new_cedula

        save_data.save()

        return redirect(reverse('profile-view', args=[pk]))






    return render(request, 'registros/modprofesion.html', context) 

def profile_pacient_view(request, pk):
    user_data = PacienteDatosPersonales.objects.get(codigo=pk)
    user_medical_data = PacienteDatosMedicos.objects.get(codigo=pk)
    user_second_data = RegisterGeneral.objects.get(codigo=pk)

    iniciado = 1

    context = {
        'user': user_data,
        'user2': user_second_data,
        'medical': user_medical_data,
        'iniciado': iniciado,
        'usercd': pk,
    }

    return render(request, 'registros/profilepaciente.html', context)


def pacient_update_medical(request, pk):


    return render(request, 'registros/pacientupdatemedical.html')



def cultura_view(request):
    medical_data = GeneralDataTable.objects.get(cod='1')

    context={
        'medical': medical_data
    }




    return render(request, 'registros/cultura.html', context)



def home_dos_view(request, pk, cd):
    user_data = PacienteDatosPersonales.objects.get(codigo=cd)




    print('*******')
    print(pk)

    context = {
        'iniciado': pk,
        'usercd': cd,
        'user': user_data
    }



    return render(request, 'registros/home2.html', context)



def cita_view(request,pk):
    user_data = PacienteDatosPersonales.objects.get(codigo=pk)


    if request.POST:
        nuevo_prioridad = request.POST.get('emprioridad')

        if nuevo_prioridad == "1":
            nuevo_prioridad = "Alta"
        elif nuevo_prioridad == "2":
            nuevo_prioridad = "Media"
        elif nuevo_prioridad == "3":
            nuevo_prioridad = "Baja"




        nuevo_sintomas = request.POST.get('sintomas')
        nuevo_hora = request.POST.get('horario')
        nuevo_fecha = request.POST.get('fecha')

        cita.objects.create(cod = pk, sintomas=nuevo_sintomas, fecha=nuevo_fecha, hora=nuevo_hora, cod_user=pk,
        disponibilidad = True)




    context={
        'user': user_data
    }






    return render(request, 'registros/cita.html', context)



def cita_menu_view(request,pk):
    
    context={
        'cod':pk

    }


    return render(request, 'registros/citasmenu.html', context)

def cita_ver_view(request, pk):

    return render(request, 'registros/citaver.html')

