from django.contrib import admin

from main.models import Document

# Register your models here.
admin.site.register(Document)  # добавили модель документов в админку
