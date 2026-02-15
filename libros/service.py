from django.db import transaction

from api_libro.pagination import CustomPagination
from libros.exceptions import LibroNoEncontradoError, NoTenesPermisosSobreEsteLibroError, DatosInvalidosError
from libros.repository import LibroRepository
from libros.serializers import LibroSerializer, LibroDetailSerializer
import logging

logger = logging.getLogger(__name__)

class LibroService:
    def __init__(self):
        self.repository = LibroRepository()
        self.paginator = CustomPagination()

    def get_all_libros(self, request):
        # Inicializo los filtros vacíos
        logger.debug(f"Obteniendo todos los libros con query params: {request.query_params}")
        filtros = {}

        # Obtengo el query_params del request
        query_params = request.query_params

        # En caso de que exista el parámetro 'titulo' en los query_params, lo agrego a los filtros con la búsqueda insensible a mayúsculas
        titulo = query_params.get('titulo', None)
        if titulo:
            filtros['titulo__icontains'] = titulo

        # En caso de que exista el parámetro 'order_by' en los query_params, lo guardo para pasarlo a la consulta
        order_by = query_params.get('order_by', None)

        # Obtengo los libros aplicando los filtros y el ordenamiento
        libros = self.repository.get_all(order_by=order_by, **filtros)

        # Aplico la paginación a los libros obtenidos, recortamos el query_set
        data = self.paginator.paginate_queryset(libros, request)


        # creo la respuesta paginada utilizando el serializer para convertir los libros a formato JSON
        response = self.paginator.get_paginated_response(LibroSerializer(data, many=True).data)


        logger.debug(f" Libros obtenidos: {response.data}")
        return response.data

    def get_libro_by_id(self, pk):
        libro = self._get_by_id(pk)
        return LibroDetailSerializer(libro).data

    @transaction.atomic
    def create_libro(self, data, user):
        if user.role != 'autor':
            logger.error(f"Usuario {user.email} con rol {user.role} intentó crear un libro sin permisos")
            raise NoTenesPermisosSobreEsteLibroError(f"Solo los usuarios con rol 'autor' pueden crear libros")

        serialzier = LibroSerializer(data=data)
        if not serialzier.is_valid():
            logger.warning(f" Los datos proporcionados invalidos: {serialzier.errors}")
            raise DatosInvalidosError(f"Los datos proporcionados para la creacion del libro son inválidos: {serialzier.errors}")


        libro = self.repository.create(**serialzier.validated_data, autor=user)


        logger.debug(f" Libro creado: {libro}")
        return LibroDetailSerializer(libro).data

    @transaction.atomic
    def update_libro(self, pk, data, user):
        libro = self._get_by_id(pk)

        self._validate_owner(libro, user)

        serialzier = LibroSerializer(libro, data=data, partial=True)
        if not serialzier.is_valid():
            logger.error(f" Usuario {user.email} intentó actualizar el libro {libro.id} sin permisos o con datos inválidos: {serialzier.errors}")
            raise DatosInvalidosError(
                {"message" : "Los datos proporcionados para la actualización del libro son inválidos",
                 "error" : serialzier.errors})

        libro = self.repository.update(libro, serialzier.validated_data)

        return LibroDetailSerializer(libro).data

    @transaction.atomic
    def delete_libro(self, pk, user):
        libro = self._get_by_id(pk)

        self._validate_owner(libro, user)

        self.repository.delete(libro)
        return True

    def _get_by_id(self, pk):
        libro = self.repository.get_by_id(pk)
        if not libro:
            logger.error(f" Libro {pk} no existe")
            raise LibroNoEncontradoError(f"No se encontró el libro con id {pk}")
        return libro

    def _validate_owner(self, libro, user):
        if libro.autor != user:
            logger.error(f" Usuario {user.email} intentó acceder al libro {libro.id} sin ser el autor")
            raise NoTenesPermisosSobreEsteLibroError(f"Solo el autor tiene permisos sobre este libro")
        return True

