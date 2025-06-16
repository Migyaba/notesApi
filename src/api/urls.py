from django.urls import path, include
from .views import NoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # crée un routeur par défaut pour gérer les routes de l'API
router.register(r'note', NoteViewSet, basename='note') # enregistre le NoteViewSet avec le routeur, ce qui crée automatiquement les routes pour les opérations CRUD

urlpatterns = [
    path('', include(router.urls)),  #route principale de l'API qui inclut toutes les routes du routeur
]