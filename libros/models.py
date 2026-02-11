from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros',
                              blank=True, null=True
                              )
    fecha_publicacion = models.DateField(auto_now_add=True)
    paginas = models.IntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

        unique_together = (('autor', 'titulo'),)
        # name = 'libro'

    def __str__(self):
        return self.titulo