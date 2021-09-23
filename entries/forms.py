from django import forms
from .models import EntryModel


class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryModel
        fields = ['name', 'phone_number', 'address', 'is_organisation', 'comment', 'address', 'image']
    