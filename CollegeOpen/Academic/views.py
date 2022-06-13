from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from CollegeOpen.Core.mixins import PermissionsByActionMixin, SerializerClassByActionMixin
from CollegeOpen.Academic.models import Academic
from CollegeOpen.Academic.services import get_from_user 
from CollegeOpen.Academic.serializers import AcademicSerializer

class AcademicViewSet(mixins.CreateModelMixin, PermissionsByActionMixin,
                    SerializerClassByActionMixin, GenericViewSet):

    queryset = Academic.objects.all()
    required_scopes = ['read']
    filter_backends = [DjangoFilterBackend]
    pagination_class = None
    serializer_action_classes = {
        'create': AcademicSerializer,
        'me': AcademicSerializer 
    }
    permission_classes_by_action = {
        'create': [AllowAny],
        'me': [IsAuthenticated]
    }

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) if not self.request.user.is_anonymous \
            else self.queryset.none()

    @swagger_auto_schema(operation_description='Detail current user information')
    @action(detail=False, methods=['get'], name='my-profile')
    def me(self, request):
        instance = get_from_user(request.user.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)