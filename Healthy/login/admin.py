from django.contrib import admin
from .models import Login, DatosPersonales, DatosProfesionales,DatosReferencias, LoginPaciente, PacienteContactosEmergencia, PacienteDatosPersonales, PacienteDatosMedicos, PacienteContactosEmergencia, RegisterGeneral, GeneralDataTable, Carausel, Person, cita

# Register your models here.

admin.site.register(Login)
admin.site.register(DatosPersonales)
admin.site.register(DatosProfesionales)
admin.site.register(DatosReferencias)
admin.site.register(LoginPaciente)
admin.site.register(PacienteDatosPersonales)
admin.site.register(PacienteDatosMedicos)
admin.site.register(PacienteContactosEmergencia)
admin.site.register(RegisterGeneral)
admin.site.register(GeneralDataTable)
admin.site.register(Carausel)
admin.site.register(cita)


class PersonAdmin(admin.ModelAdmin):
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        url ='templates/admin/person/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    actions = [generatePDF]

admin.site.register(Person, PersonAdmin)


