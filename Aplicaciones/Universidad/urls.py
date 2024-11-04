from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('principalUser/',views.principalUsuarios),
    path('userRegistro/',views.registroUsuario),
    path('registrarUsuariarios/',views.guardarUsuario),
    path('eliminarUsuarios/<codigo>',views.eliminarUsuario),
    path('editarUsuarios/<codigo>',views.edicionUsuario),
    path('usuarioEditado/',views.editar),
    path('principalB/',views.principalBlog),
    path('blogRegistro/',views.registroBlog),
    path('guardarBlog/',views.guardarBlog),
    path('eliminarBlog/<codigo>',views.eliminarBlog),
    path('verEntrada/<codigo>',views.verEntrada),
    path('verAbout/',views.verAbout),
    path('login/',views.login)
]
