from django.db import models
from CollegeOpen.Core.models import BaseModel
from CollegeOpen.Academic.models import Student, Professor  
from CollegeOpen.Locations.models import Location



class Discipline(BaseModel):
    name = models.CharField('Nome da Disciplina', null=True, max_length=128)
    students = models.ManyToManyField(Student, verbose_name='Turma de Estudantes', blank=True)
    professor = models.ForeignKey(Professor, verbose_name='Professor', null=True, blank=True, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, verbose_name='Localização', null=True, blank=True, on_delete=models.PROTECT)
    

    class Meta:
        verbose_name = 'Disciplina' 
        verbose_name_plural = 'Disciplinas' 

class PreRequirements(BaseModel):
    disciplines = models.ManyToManyField(Discipline, verbose_name='pre-requesitos', blank=True)

    class Meta:
        verbose_name = 'Pre-requisitos'
        verbose_name_plural = 'Pre-requisitos'

class CoRequirements(BaseModel):
    disciplines = models.ManyToManyField(Discipline, verbose_name='co-requesitos', blank=True)

    class Meta:
        verbose_name = 'Co-requisitos'
        verbose_name_plural = 'Co-requisitos'