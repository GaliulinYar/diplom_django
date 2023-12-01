from django.urls import path

from main.apps import MainConfig
from main.views import DocumentCreateAPIView, DocumentAPIView, DocumentUpdateAPIView, DocumentDestroyAPIView, \
    DocumentRetrieveAPIView

# Добавили связи с Юзером
app_name = MainConfig.name

urlpatterns = [
    # паттерны для работы с файлами
    path('create/', DocumentCreateAPIView.as_view(), name='create'),  # загрузка документа
    path('', DocumentAPIView.as_view(), name='documents'),  # просмотр всех отправленных документов
    path('<int:pk>/update/', DocumentUpdateAPIView.as_view(), name='update_file'),  # изменение документа
    path('<int:pk>/delete/', DocumentDestroyAPIView.as_view(), name='delete'),  # удаление документа
    path('<int:pk>/detail/', DocumentRetrieveAPIView.as_view(), name='document_detail'),  # просмотр данных конкретного документа
]
