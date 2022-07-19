from rest_framework import serializers
from django.core.serializers.json import Serializer as DjangoSerializer
from CollegeOpen.Disciplines.models import Discipline

from CollegeOpen.Disciplines import services

class CreateDisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline 
        fields = [
            'component_type',
            'educational_mode',
            'name',
            'code',
            'students',
            'professor',
            'location',
            'total_exams',
            'flexible_program',
            'online_registry',
            'description',
            'long_description'
        ]