from django.urls import path
from .views import LibroView, LibroDetailView, LibroGenericView, LibroDetailGenericView

urlpatterns = [
    path('libros/', LibroGenericView.as_view()),
    path('libros/<int:pk>/', LibroDetailGenericView.as_view()),
]