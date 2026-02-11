from rest_framework.viewsets import ModelViewSet
from .serializers import LibroSerializer, AutorSerializer, LibroDetailSerializer
from .models import Libro, Autor

class LibroViewSet(ModelViewSet):

    def get_queryset(self):
        return Libro.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LibroDetailSerializer
        return LibroSerializer




class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer



