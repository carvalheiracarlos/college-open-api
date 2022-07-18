from django.db import models
from CollegeOpen.Core.models import BaseModel


class Location(BaseModel):
    name = models.CharField('Nome', max_length=255)
    address = models.TextField('Endereço', max_length=500)

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localização'