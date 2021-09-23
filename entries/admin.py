from django.contrib import admin

from .models import EntryModel

# Register your models here.

@admin.register(EntryModel)
class EntryAdmin(admin.ModelAdmin): pass
