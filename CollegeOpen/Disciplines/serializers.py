from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from CollegeOpen.Academic.serializers import StudentReadSerializer, ProfessorReadSerializer
from CollegeOpen.Locations.serializers import LocationSerializer
from CollegeOpen.Disciplines.models import Discipline, DisciplineReviews
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

class DisciplineReviewsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DisciplineReviews
        fields = [
            'discipline',
            'message',
            'score'
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return services.create_discipline_reviews(**validated_data)
