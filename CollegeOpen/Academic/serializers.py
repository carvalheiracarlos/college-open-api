from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from CollegeOpen.Academic.models import Student, Professor
from CollegeOpen.Academic import services



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student 
        fields = ['id', 'user', 'name', 'registration',]

    def create(self, validated_data):
        return services.create(**validated_data, Model=Student)

    def update(self, instance, validated_data):
        raise PermissionDenied()


class ProfessorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Professor 
        fields = ['id', 'user', 'name', 'registration',]

    def create(self, validated_data):
        return services.create(**validated_data, Model=Professor)

    def update(self, instance, validated_data):
        raise PermissionDenied()


class StudentReadSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Student
        fields = ['registration', 'name', 'email']


class ProfessorReadSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Professor
        fields = ['registration', 'name', 'email']