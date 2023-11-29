from rest_framework import serializers

from main.models import Document
from users.models import User
from users.serializers import UserSerializer


class DocumentSerializer(serializers.ModelSerializer):
    """Сериализатор для создания (загрузки документа)"""

    class Meta:
        model = Document
        fields = ['file_load']


class DocumentListSerializer(serializers.ModelSerializer):
    """Сериализатор для прсмотра отправленных файлов"""
    user = UserSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'file_load', 'check_file', 'user']


class DocumentCheckSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'check_file', 'user']


class DocumentIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['id']


class DocumentAllSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'

