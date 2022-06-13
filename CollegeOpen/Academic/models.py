from django.db import models
from django.contrib.auth.models import User
from CollegeOpen.Core.models import BaseModel
from CollegeOpen.Academic.academic_repository import AcademicQueryset 

class Academic(BaseModel):
    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=255)
    registration = models.CharField('Matrícula', max_length=20)
    is_professor = models.BooleanField('Professor', default=False)


    objects = AcademicQueryset.as_manager()

    class Meta:
        verbose_name_plural = 'Academico'
        verbose_name = 'Academicos'
        ordering = ('-created',)