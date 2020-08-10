from django.db import models

# Create your models here.
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=35)
    imagen = models.ImageField(upload_to = 'images/')
    descripcion = models.CharField(max_length=100)
    anio = models.CharField(max_length=35)
    genero = models.CharField(max_length=35)

    def __str__(self):
        return  self.titulo

class comententario(models.Model):

    comments = models.TextField(max_length=100)
    movie = models.ForeignKey(to=Pelicula, on_delete=models.CASCADE)
    clasePredecida = models.CharField(max_length=100, null=True, blank=True)
    probabiliad = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return  self.comments
