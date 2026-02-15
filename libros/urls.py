from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, LibroView

router = DefaultRouter()

router.register(r"libros", LibroView, basename="libros")