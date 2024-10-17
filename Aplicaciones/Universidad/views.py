from django.shortcuts import render, redirect
from .models import Cursos, Profesores, Estudiantes, Entregables
# Create your views here.
def home(request):
    return render(request,"inicio.html")

def cursos(request):
    return render(request, 'cursoRegistrar.html')

def registrarCursos(request):
    nombre = request.POST['txtNombre']
    camada =  request.POST['numCamada']
    
    curso = Cursos.objects.create(Nombre=nombre, Camada=camada)
    return redirect('/principalCursos/')

def principalCurso (request):
    cursos = Cursos.objects.all()
    return render(request, 'principalCurso.html', {"cursos": cursos})

def principalProfesor(request):
    profesores = Profesores.objects.all()
    return render(request, 'principalProfesor.html', {"profesores": profesores})

def profesores(request):
    return render(request, 'profesorRegistrar.html')

def registrarProfesor(request):
    nombre = request.POST['txtNombre']
    apellido =  request.POST['txtApellido']
    correo =  request.POST['txtEmail']
    
    profesor = Profesores.objects.create(Nombre=nombre, Apellido=apellido, Email=correo )
    return redirect('/principalProfesores/')

def principalEstudiante(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, 'principalEstudiante.html', {"estudiantes": estudiantes})

def estudiante(request):
    return render(request, 'estudianteRegistrar.html')
    
def registrarEstudiante(request):
    nombre = request.POST['txtNombre']
    apellido =  request.POST['txtApellido']
    correo =  request.POST['txtEmail']
    
    estudiante = Estudiantes.objects.create(Nombre=nombre, Apellido=apellido, Email=correo )
    return redirect('/principalEstudiantes/')

def principalEntregable(request):
    entregables =  Entregables.objects.all()
    return render(request, 'principalEntregables.html', {"entregables": entregables})

def entrega(request):
    return render(request, 'entregableRegistrar.html')
    
def registrarEntrega(request):
    nombre = request.POST['txtNombre']
    fechaEntrega =  request.POST['txtentrega']
    entrega =  request.POST['numentrega']
    
    entregable = Entregables.objects.create(Nombre=nombre, FechaDeEntrega=fechaEntrega, Entregado=entrega )
    return redirect('/principalEntregable/')

      
    


    
