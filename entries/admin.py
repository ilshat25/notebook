from django.contrib import admin

from .models import EntryModel


# Добавить модель Entry на панель администрации
@admin.register(EntryModel)
class EntryAdmin(admin.ModelAdmin): pass
