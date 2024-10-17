from django.db import models

# Create your models here.

class Cursos(models.Model):
    CodigoC = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Camada = models.SmallIntegerField()
    
    def __str__(self) -> str:
        texto = "{0} {1} {2}"
        return texto.format(self.CodigoC,self.Nombre,self.Camada)
    
class Profesores(models.Model):
    CodigoP = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido =models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        texto = "{0} {1} {2} {3}"
        return texto.format(self.CodigoP,self.Nombre,self.Apellido,self.Email)
    

class Estudiantes(models.Model):
    CodigoE = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=50)
    Apellido =models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        texto = "{0} {1} {2} {3}"
        return texto.format(self.CodigoE,self.Nombre,self.Apellido,self.Email)
    
    
class Entregables(models.Model):
    CodigoEn = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=50)
    FechaDeEntrega= models.DateField()
    Entregado = models.SmallIntegerField()
    
    def __str__(self) -> str:
        texto = "{0} {1} {2} {3}"
        return texto.format(self.CodigoEn,self.Nombre,self.FechaDeEntrega,self.Entregado)
    
    
    