from django.urls import path, include
from .views import home_view, login_view, register_view, register2_view, register3_view, register_user_view, profiel_view, register_pacient_view, modify_contact_view, modify_profesion_view, profile_pacient_view, pacient_update_medical, cultura_view, home_dos_view, generatePDF, create_pdf, cita_view, cita_menu_view, cita_ver_view


urlpatterns = [
   
    path('', home_view, name='home-view'),
    path('login/', login_view, name='login-view'),
    path('registro/', register_view, name='register-view' ),
    path('registro_paso_dos', register2_view, name='register2-view'),
    path('registro_paso_tres/<int:pk>/', register3_view, name='register3-view'),
    path('registro_usuario/<int:pk>', register_user_view, name='register-user-view'),
    path('profile/<int:pk>/', profiel_view, name='profile-view'),
    path('registro_paciente/', register_pacient_view, name='register-pacient-view'),
    path('modificar_contacto/<int:pk>', modify_contact_view, name='modify-contact-view'),
    path('modificar_profesion/<int:pk>', modify_profesion_view, name='modify-profesion-view'),
    path('profile_paciente/<int:pk>', profile_pacient_view, name='profile-paciente-view'),
    path('paciente_actualizar_medicos/<int:pk>', pacient_update_medical, name='update-pacient-medical-view'),
    path('culturas/', cultura_view, name='cultura-view'),
    path('home/<int:pk>/<int:cd>/', home_dos_view, name='home-dos-view'),
    path('<int:id>/generatePDF/', generatePDF, name='generatePDF'),
    path('generar/', create_pdf, name="generar_pdf"),
    path('citas/<int:pk>', cita_view, name="cita-view"),
    path('citamenu/<int:pk>/', cita_menu_view, name='cita-menu-view'),
    path('citas/ver/<int:pk>', cita_ver_view, name='cita-ver-view'),
]