from django.db import models
from CollegeOpen.Core.models import BaseModel
from CollegeOpen.Academic.models import Student, Professor  
from CollegeOpen.Locations.models import Location



class Discipline(BaseModel):

    students = models.ManyToManyField(Student, verbose_name='Turma de Estudantes', blank=True)
    professor = models.ForeignKey(Professor, verbose_name='Professor', null=True, blank=True, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, verbose_name='Localização', null=True, blank=True, on_delete=models.PROTECT)
    

    class Meta:
        verbose_name = 'Disciplina' 
        verbose_name_plural = 'Disciplinas' 

