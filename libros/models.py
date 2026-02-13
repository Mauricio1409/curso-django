from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libros',
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