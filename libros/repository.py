from libros.models import Libro


class LibroRepository:
    def get_all(self, order_by=None, **filters):

        # Obtengo todos los libros y luego aplico los filtros y el ordenamiento si se proporcionan
        libros = Libro.objects.all()

        # Aplico los filtros si se proporcionan
        if filters:
            libros = libros.filter(**filters)

        # Aplico el ordenamiento si se proporciona
        if order_by:
            libros = libros.order_by(order_by)

        # Devuelvo el queryset resultante
        return libros

    def get_by_id(self, pk):
        return Libro.objects.filter(id=pk).first()

    def create(self, **data):
        return Libro.objects.create(**data)

    def update(self, instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()