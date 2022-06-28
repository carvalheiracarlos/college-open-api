from django.urls import path
from rest_framework import routers

from CollegeOpen.Academic.views import StudentViewSet, ProfessorViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet, basename='StudentViewSet')
router.register(r'professor', ProfessorViewSet, basename='ProfessorViewSet')

app_name = 'academic'
urlpatterns = []
urlpatterns += router.urls