from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class EntryModel(models.Model):
    owner = models.ForeignKey(get_user_model(),
                              related_name='entries',
                              on_delete=models.CASCADE,
                              blank=False,
                              null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = PhoneNumberField(blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    is_organisation = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="entries/%Y/%m/%d/")

    def __str__(self):
        return f'{self.name}: {self.phone_number}'
