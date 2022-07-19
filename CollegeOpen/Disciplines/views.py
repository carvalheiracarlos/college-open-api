from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from CollegeOpen.Core.mixins import PermissionsByActionMixin, SerializerClassByActionMixin
from CollegeOpen.Disciplines.serializers import CreateDisciplineSerializer, DisciplineListSerializer
from CollegeOpen.Disciplines.filters import DisciplineFilter
from CollegeOpen.Disciplines.models import Discipline
from CollegeOpen.Academic.models import Professor, Student



class DisciplineViewSet(SerializerClassByActionMixin, 
                        PermissionsByActionMixin, 
                        mixins.CreateModelMixin, 
                        mixins.ListModelMixin, 
                        GenericViewSet,):
                
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'list': [IsAuthenticated],
        'update_professor': [IsAdminUser],
        'update_students': [IsAuthenticated]

    }
    serializer_action_classes = {
        'create': CreateDisciplineSerializer,
        'list': DisciplineListSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filter_class = DisciplineFilter
    queryset = Discipline.objects.all()
    
    @action(detail=True, methods=['put'], name='update_professor')
    def update_professor(self, request, pk, format=None):
        instance = self.get_object()
        try:
            professor= Professor.objects.get(id=self.request.user.professor.id)
            instance.professor = professor 
            instance.save()
            return Response(status=201)
        except:
            return Response(status=403)

    @action(detail=True, methods=['put'], name='update_students')
    def update_students(self, request, pk, format=None):
        instance = self.get_object()
        try:
            student = Student.objects.get(id=self.request.user.student.id)
            instance.students.add(student) 
            instance.save()
            return Response(status=201)
        except:
            return Response(status=403)
