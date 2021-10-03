from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField


# Модель записи (представляет таблицу в БД)
class EntryModel(models.Model):
    RANDOM = 'RD'
    EMPLOYEE = 'EP'
    CLIENT = 'CL'
    PARTNER = 'PT'
    STATUS_CHOICES = [
        (RANDOM, 'Random'),
        (EMPLOYEE, 'Employee'),
        (CLIENT, 'Client'),
        (PARTNER, 'Partner')
    ]
    owner = models.ForeignKey(get_user_model(),
                              related_name='entries',
                              on_delete=models.CASCADE,
                              blank=False,
                              null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = PhoneNumberField(blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=RANDOM)
    comment = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="entries/%Y/%m/%d/")

    def __str__(self):
        return f'{self.name}: {self.phone_number}'
