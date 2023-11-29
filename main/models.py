import os

from django.db import models
from django.conf import settings

NULLABLE = {
    'null': True,
    'blank': True
}


# Create your models here.
class Document(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Отправитель',
                              **NULLABLE)  # Привязка к юзеру

    file_load = models.FileField(upload_to='documents/', verbose_name='Файл')  # Сам файл
    check_file = models.BooleanField(default=False, verbose_name='Файл принят')  # Принятие файла, по у молчанию False
    checkout_file = models.BooleanField(default=False, verbose_name='Файл Отклонен')  # Отклонение  файла, по у молчанию False

