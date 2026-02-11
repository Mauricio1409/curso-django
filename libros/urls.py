from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet

router = DefaultRouter()

router.register(r"libros", LibroViewSet, basename="libros")
router.register(r"autores", AutorViewSet, basename="autores")