from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('cursos/', views.cursos),
    path('registrarCurso/',views.registrarCursos),
    path('principalCursos/', views.principalCurso),
    path('principalProfesores/', views.principalProfesor),
    path('registrarProfesor/',views.profesores),
    path('registrarProfesores/',views.registrarProfesor),
    path('principalEstudiantes/',views.principalEstudiante),
    path('estudianteRegistrar/',views.estudiante),
    path('registrarEstudiantes/',views.registrarEstudiante),
    path('principalEntregable/',views.principalEntregable),
    path('entregableRegistrar/',views.entrega),
    path('registrarEntrega/',views.registrarEntrega)
]
