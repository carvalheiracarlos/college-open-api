from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from CollegeOpen.Core.mixins import PermissionsByActionMixin, SerializerClassByActionMixin
from CollegeOpen.Disciplines.serializers import CreateDisciplineSerializer
from CollegeOpen.Disciplines.models import Discipline



class CreateDisciplineView(mixins.CreateModelMixin, PermissionsByActionMixin, GenericViewSet):
    permission_classes_by_action = {
        'create': [IsAuthenticated],
    }
    filter_backends = [DjangoFilterBackend]
    serializer_class = CreateDisciplineSerializer
    queryset = Discipline.objects.all()