from django import forms
from .models import EntryModel


# Добоаляет форму для модели Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryModel
        fields = ['name', 'phone_number', 'address', 'is_organisation', 'comment', 'address', 'image']
    