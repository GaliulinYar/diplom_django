from django.db import models
from django.conf import settings


# Create your models here.
class Document(models.Model):
    # Класс отправляемого документя
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='postman_user')  # Привязка к юзеру

    file_load = models.FileField(upload_to='documents/', verbose_name='Файл')  # Сам файл
    check_file = models.BooleanField(default=False, verbose_name='Файл принят')  # Принятие файла, по у молчанию False
    checkout_file = models.BooleanField(default=False, verbose_name='Файл Отклонен')  # Отклонение  файла, по у молчанию False

    # Строкое предстваления для разработчиков
    def __str__(self):
        return f'Документ {self.owner} Принятие - {self.check_file} Отклонение - {self.checkout_file}'

    # Мета предстваление, например для админки
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
