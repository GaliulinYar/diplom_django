from rest_framework import serializers
from main.models import Document
from users.serializers import UserDocSerializer


class DocumentSerializer(serializers.ModelSerializer):
    """Сериализатор для создания (загрузки документа)"""

    class Meta:
        model = Document
        fields = ['file_load']


class DocumentListSerializer(serializers.ModelSerializer):
    """Сериализатор для прсмотра отправленных файлов"""
    owner = UserDocSerializer(read_only=True)  # вложенный сериализатор

    class Meta:
        model = Document
        fields = ['owner', 'id', 'file_load', 'check_file', 'checkout_file']


class DocumentCheckSerializer(serializers.ModelSerializer):
    """Сериализатор для  админов на принятие или отклонение жокумента"""
    user = UserDocSerializer(read_only=True)  # вложенный сериализатор

    class Meta:
        model = Document
        fields = ['id', 'check_file', 'checkout_file', 'user']


class DocumentIdSerializer(serializers.ModelSerializer):
    """Сериализатор для удаления документов"""
    class Meta:
        model = Document
        fields = ['id']


class DocumentAllSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра данных каждого документа отдельно"""
    user = UserDocSerializer(read_only=True) # вложенный сериализатор

    class Meta:
        model = Document
        fields = '__all__'
