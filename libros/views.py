from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from api_libro.pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import LibroSerializer, LibroDetailSerializer
from .models import Libro

class LibroViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = ['titulo']
    search_fields = ['titulo']
    ordering_fields = ['titulo']

    def get_queryset(self):
        return Libro.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LibroDetailSerializer
        return LibroSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)




# class AutorViewSet(ViewSet):
#     def list(self, request):
#
#         nombre = request.query_params.get('nombre', None)
#
#         autores = Autor.objects.all()
#         if nombre:
#             autores =autores.filter(nombre__icontains=nombre)
#
#         serializer = AutorSerializer(autores, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def create(self, request):
#         serializer = AutorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         autor_existe = Autor.objects.filter(nombre=serializer.validated_data['nombre']).exists()
#
#         if autor_existe:
#             return Response({'error': 'El autor ya existe'}, status=status.HTTP_400_BAD_REQUEST)
#
#         autor = Autor.objects.create(**serializer.validated_data)
#
#         data = AutorSerializer(autor).data
#
#         return Response(data, status=status.HTTP_201_CREATED)
#
#     def update(self, request, pk=None):
#         autor = Autor.objects.filter(id=pk).first()
#         if not autor:
#             return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = AutorSerializer(autor, data=request.data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#
#     def partial_update(self, request, pk=None):
#         autor = Autor.objects.filter(id=pk).first()
#         if not autor:
#             return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = AutorSerializer(autor, data=request.data, partial=True)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def destroy(self, request, pk=None):
#         autor = Autor.objects.filter(id=pk).first()
#         if not autor:
#             return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         autor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=True, methods=['get'], url_path="libros")
#     def get_libros(self, request, pk=None):
#         autor = Autor.objects.filter(id=pk).first()
#         if not autor:
#             return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         libros = autor.libros.all()
#
#         serializer = LibroSerializer(libros, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @action(detail=False, methods=['get'], url_path="cantidad")
#     def get_cantidad_autores(self, request):
#         cantidad = Autor.objects.count()
#         return Response({'cantidad': cantidad}, status=status.HTTP_200_OK)

