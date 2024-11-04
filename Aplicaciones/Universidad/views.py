from django.shortcuts import render, redirect
from .models import Usuarios,Blog
import os

# Create your views here.
def home(request):
    return render(request,"inicio.html")

def principalUsuarios(request):
    usuario = Usuarios.objects.all()
    return render(request,"principalUsuario.html",{"usuarios":usuario})

def registroUsuario(request):
    return render(request,"usuarioRegistrar.html")

def guardarUsuario(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    password = request.POST['txtPassword']    
    archivo = request.FILES.get('txtFoto')
    foto = archivo.name

    usuario = Usuarios.objects.create(Nombre=nombre,Apellido=apellido,Email=email,Password=password,ArchivoU=archivo,FotoU=foto,Perfil=0)
    
    return redirect('/principalUser/')

def eliminarUsuario(request,codigo):
    usuario = Usuarios.objects.get(CodigoU=codigo)
    usuario.delete()
    
    return redirect('/principalUser/')

def edicionUsuario(request,codigo):
    usuario = Usuarios.objects.get(CodigoU=codigo)
    return render(request,"usuarioEditar.html",{'usuario':usuario})

def editar(request):
     
    codigo   = request.POST['txtCodigo']
    nombre   = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email    = request.POST['txtEmail']
    password = request.POST['txtPassword']
    archivo = request.FILES.get('txtFoto')
    foto = archivo.name
    
    usuario = Usuarios.objects.get(CodigoU=codigo)
    usuario.Nombre = nombre
    usuario.Apellido = apellido
    usuario.Email = email
    usuario.Password = password
    usuario.ArchivoU = archivo
    usuario.FotoU = foto
    
    usuario.save()
    return redirect('/principalUser/')

def principalBlog(request):
    entradas = Blog.objects.all()
    return render(request,"principalBlog.html",{"entradas":entradas})

def registroBlog(request):
    return render(request,"BlogRegistrar.html")

def guardarBlog(request):
    titulo    = request.POST['txtTitulo']
    subtitulo = request.POST['txtSubtitulo']
    cuerpo    = request.POST['txtCuerpo']
    autor     = Usuarios.objects.get(CodigoU=request.POST['txtAutor'])
    fecha     = request.POST['txtFecha']
    archivo = request.FILES.get('txtFoto')
    foto = archivo.name
    
    blog = Blog.objects.create(Titulo=titulo,Subtitulo=subtitulo,Cuerpo=cuerpo,Autor=autor,ArchivoB=archivo,FotoB=foto,Fecha=fecha)
    
    return redirect('/principalB/')

def eliminarBlog(request,codigo):
    blog = Blog.objects.get(CodigoB=codigo)
    blog.delete()
    
    return redirect('/principalB/')

def verEntrada(request,codigo):
    blog = Blog.objects.get(CodigoB=codigo)
    return render(request,"blogVer.html",{'blog':blog})

def verAbout(request):
    return render(request,"about.html")

def login(request):
    return render(request,"login.html")
