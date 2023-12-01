from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from config.settings import EMAIL_HOST_USER
from main.models import Document
from main.serializers import DocumentSerializer, DocumentListSerializer, DocumentCheckSerializer, DocumentIdSerializer, \
    DocumentAllSerializer
from users.models import User


# Create your views here.
class DocumentCreateAPIView(generics.CreateAPIView):
    """Вьюшка для создания - загрузки файла"""
    serializer_class = DocumentSerializer  # Добаляем сериализатор
    permission_classes = [permissions.IsAuthenticated]  # проверка на аутендификацию

    def perform_create(self, serializer):
        # Вызываем стандартный метод perform_create для сохранения объекта
        serializer.save(owner=self.request.user)  # Загружаем файл с присваиванием пользователя, который аудентифицирован в данный момент
        admin_users = User.objects.filter(is_staff=True)  # Ищем пользователя is_staff = True
        admin_email = admin_users.first().email  # Достаем администратора

        # Отправка письма администратору с оповещением
        send_mail(
            subject='Новый документ',
            message=f'Вам пришел новый документ от {self.request.user.email}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[admin_email]
        )


class DocumentAPIView(generics.ListAPIView):
    """Вьюшка для просмотра списка загруженных документов."""
    serializer_class = DocumentListSerializer  # Добаляем сериализатор
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # проверка на аутендификацию


class DocumentRetrieveAPIView(generics.RetrieveAPIView):
    """Вьюшка для просмотра данных одного документа"""
    serializer_class = DocumentAllSerializer  # Добаляем сериализатор
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # проверка на аутендификацию


class DocumentUpdateAPIView(generics.UpdateAPIView):
    """Вьюшка для принятия или отклонения документов, только для админа"""
    serializer_class = DocumentCheckSerializer  # Добаляем сериализатор
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAdminUser]  # Разрешение только для staff - True

    # проверка документа на принятие/отказ и отправка нужных писем
    def perform_update(self, serializer):
        # Получаем исходный объект
        instance = serializer.instance

        # Получаем значения до и после обновления
        check_file_before = instance.check_file
        checkout_file_before = instance.checkout_file

        # Выполняем обновление
        serializer.save()

        # Получаем значения после обновления
        check_file_after = serializer.instance.check_file
        checkout_file_after = serializer.instance.checkout_file

        if check_file_after != checkout_file_after:
            # Проверяем изменения и выполняем нужные действия
            if check_file_before != check_file_after and check_file_after == True:

                # Отправляем письмо владальцу документа о том что документ принят
                print('Документ принят')
                send_mail(
                    subject='Ответ администратора',
                    message=f'Ваш документ принят {self.request.user.email}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[instance.owner.email]
                )

            if checkout_file_before != checkout_file_after and checkout_file_after == True:
                # Отправляем письмо  владальцу файла-документа, о том что документ отклонен

                send_mail(
                    subject='Ответ администратора',
                    message=f'Ваш документ отклонён, попробуйте отправить его еще раз{self.request.user.email}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[instance.owner.email]
                )


class DocumentDestroyAPIView(generics.DestroyAPIView):
    """Удаление данных из БД о загруженных документах(удаление экземпляра)"""
    serializer_class = DocumentIdSerializer
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAdminUser]  # Разрешение только для staff - True
