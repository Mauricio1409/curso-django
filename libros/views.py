from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LibroSerializer
from .models import Libro
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# /api/libros/ -> GET, POST
class LibroView(APIView):
    def get(self, request):
        libros = Libro.objects.all()
        data = LibroSerializer(libros, many=True).data
        return Response(data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data_validada = serializer.validated_data
        nuevo_libro = Libro.objects.create(**data_validada)
        respuesta = LibroSerializer(nuevo_libro).data
        return Response(respuesta, status=status.HTTP_201_CREATED)


# /api/libros/<id>/ -> GET, PUT, DELETE
class LibroDetailView(APIView):
    def get(self, request, id):
        libro = Libro.objects.filter(id=id).first()
        if not libro:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        respuesta = LibroSerializer(libro).data
        return Response(respuesta, status=status.HTTP_200_OK)

    def put(self, request, id):
        data = LibroSerializer(data=request.data, partial=True)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


        libro = Libro.objects.filter(id=id).first()
        if not libro:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        data_validada = data.validated_data

        for campo, valor in data_validada.items():
            setattr(libro, campo, valor)
        libro.save()

        respuesta = LibroSerializer(libro).data

        return Response(respuesta, status=status.HTTP_200_OK)

    def delete(self, request, id):
        # buscar por id
        libro = Libro.objects.filter(id=id).first()

        # validar que exista el libro
        if not libro:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # eliminar el libro
        libro.delete()

        return Response({"message": "Libro eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class LibroGenericView(ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

