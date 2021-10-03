from django import forms
from .models import EntryModel


# Добоаляет форму для модели Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryModel
        fields = ['name', 'phone_number', 'address', 'status', 'comment', 'address', 'image']
    