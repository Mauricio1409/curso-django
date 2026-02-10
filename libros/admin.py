from django.contrib import admin

from libros.models import Libro


# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_publicacion', 'paginas')
    list_filter = ('titulo',)
    search_fields = ('titulo', 'autor')
