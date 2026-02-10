from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)
    paginas = models.IntegerField()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


    def __str__(self):
        return self.titulo
