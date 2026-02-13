from rest_framework import serializers
from .models import Libro
from users.serializers import UserSerializer


class LibroDetailSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor', 'fecha_publicacion', 'paginas')
        read_only_fields = ('id','fecha_publicacion')

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'fecha_publicacion', 'paginas')
        read_only_fields = ('id','fecha_publicacion')

    def validate_paginas(self, value):
        if value <= 1:
            raise serializers.ValidationError("El número de páginas debe ser mayor que 1.")
        return value

    def validate_titulo(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El título del libro debe tener al menos 3 caracteres.")
        return value



