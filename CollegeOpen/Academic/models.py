from django.db import models
from django.contrib.auth.models import User
from CollegeOpen.Core.models import BaseModel
from CollegeOpen.Academic.academic_repository import AcademicQueryset 

    
class Student(BaseModel):
    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=255)
    registration = models.CharField('Matrícula', max_length=20)

    objects = AcademicQueryset.as_manager()

    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'


class Professor(BaseModel):
    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE )
    name = models.CharField('Nome', max_length=255)
    registration = models.CharField('Matrícula', max_length=20)

    objects = AcademicQueryset.as_manager()

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
