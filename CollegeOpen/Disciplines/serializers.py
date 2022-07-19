from rest_framework import serializers

from CollegeOpen.Academic.serializers import StudentReadSerializer, ProfessorReadSerializer
from CollegeOpen.Locations.serializers import LocationSerializer
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


class DisciplineListSerializer(serializers.ModelSerializer):
    discipline_name = serializers.CharField(source='name')
    discipline_code = serializers.CharField(source='code')
    students = StudentReadSerializer(many=True)
    professor = ProfessorReadSerializer()
    location = LocationSerializer()
    

    class Meta:
        model = Discipline
        fields = [
            'discipline_name', 
            'discipline_code', 
            'students', 
            'professor', 
            'location',
            'total_exams',
            'flexible_program',
            'online_registry',
            'description',
            'long_description'
        ]