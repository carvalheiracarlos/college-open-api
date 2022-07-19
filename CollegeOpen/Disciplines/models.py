from django.db import models
from CollegeOpen.Core.models import BaseModel
from CollegeOpen.Academic.models import Student, Professor  
from CollegeOpen.Locations.models import Location



class Discipline(BaseModel):
    component_types = (
        ('0', 'DISCIPLINAS'),
        ('1', 'MODULOS'),
        ('2', 'BLOCOS'),
        ('3', 'ATIVIDADE ACADEMICA'),
    )
    educational_modes_types = (
        ('0', 'PRESENCIAL'),
        ('1', 'REMOTO'),
    )

    compoent_type = models.SmallIntegerField('Tipo do Componente Curricular', choices=component_types, default=0)
    educational_mode = models.SmallIntegerField('Modalidades de Educação', choices=educational_modes_types, default=0)
    name = models.CharField('Nome da Disciplina', null=True, max_length=128)
    code = models.CharField('Código da Disciplina', null=True, max_length=48)
    students = models.ManyToManyField(Student, verbose_name='Turma de Estudantes', blank=True)
    professor = models.ForeignKey(Professor, verbose_name='Professor', null=True, blank=True, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, verbose_name='Localização', null=True, blank=True, on_delete=models.PROTECT)
    total_exams = models.PositiveSmallIntegerField('Quantidade de Avaliações', default=3)
    flexible_program = models.BooleanField('Hoário Flexivel ?', default=True)
    online_registry = models.BooleanField('Matricula Online ?', default=True)
    description = models.TextField('Descrição da Ementa', null=True, blank=True, max_length=512) 
    long_description = models.FileField('Descrição da Ementa', null=True, blank=True, upload_to='disciplines/description/') 

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


class Equivalences(BaseModel):
    disciplines = models.ManyToManyField(Discipline, verbose_name='equivalencias', blank=True)

    class Meta:
        verbose_name = 'Equivalencias'
        verbose_name_plural = 'Equivalencias'