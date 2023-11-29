from django.shortcuts import render
from rest_framework import generics

from main.models import Document
from main.serializers import DocumentSerializer, DocumentListSerializer, DocumentCheckSerializer, DocumentIdSerializer, \
    DocumentAllSerializer


# Create your views here.
class DocumentCreateAPIView(generics.CreateAPIView):
    """Вьюшка для создания - загрузки файла"""
    serializer_class = DocumentSerializer


class DocumentAPIView(generics.ListAPIView):
    """Вьюшка для просмотра списка загруженных документов."""
    serializer_class = DocumentListSerializer
    queryset = Document.objects.all()


class DocumentRetrieveAPIView(generics.RetrieveAPIView):
    """Вьюшка для просмотра данных одного документа"""
    serializer_class = DocumentAllSerializer
    queryset = Document.objects.all()


class DocumentUpdateAPIView(generics.UpdateAPIView):
    """Сериализатор для принятия дкументов, только для админа"""
    serializer_class = DocumentCheckSerializer
    queryset = Document.objects.all()


class DocumentDestroyAPIView(generics.DestroyAPIView):
    """Удаление данных из БД о загруженных документах(удаление экземпляра)"""
    serializer_class = DocumentIdSerializer
    queryset = Document.objects.all()


