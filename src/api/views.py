from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer
from rest_framework import filters

class NoteViewSet(ModelViewSet):
    """
    le NoteViewSet est un ViewSet qui fournit des opérations CRUD pour le modèle Note.
    """
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Permet la recherche dans les champs title et content