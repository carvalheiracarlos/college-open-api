from django.urls import path
from rest_framework import routers

from CollegeOpen.Academic.views import AcademicViewSet

router = routers.DefaultRouter()
router.register(r'', AcademicViewSet, basename='AcademicViewSet')

app_name = 'academic'
urlpatterns = []
urlpatterns += router.urls