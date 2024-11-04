from django.db import models

# Create your models here.

class Usuarios(models.Model):
    CodigoU = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=50)
    Apellido =models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password =models.CharField(max_length=20)
    ArchivoU = models.ImageField(upload_to="Aplicaciones/Universidad/static/imagenes/", null=True, blank=True)
    FotoU = models.CharField(max_length=150)
    Perfil = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        texto = "{0} {1} {2} {3} {4} {5}"
        return texto.format(self.CodigoU,self.Nombre,self.Apellido,self.Email,self.Perfil,self.FotoU)

class Blog(models.Model):
    CodigoB   = models.AutoField(primary_key=True)
    Titulo    = models.CharField(max_length=100)
    Subtitulo = models.CharField(max_length=100)
    Cuerpo    = models.CharField(max_length=250)
    Autor     = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Fecha     = models.DateField()
    ArchivoB   = models.ImageField(upload_to="Aplicaciones/Universidad/static/imagenes/", null=True, blank=True)
    FotoB      = models.CharField(max_length=150)

    def __str__(self) -> str:
        texto = "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(self.CodigoB,self.Titulo,self.Subtitulo,self.Cuerpo,self.Autor,self.Fecha,self.FotoB)
    
    
    