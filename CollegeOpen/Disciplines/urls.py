from django.urls import path
from rest_framework import routers

from CollegeOpen.Disciplines.views import DisciplineViewSet

router = routers.DefaultRouter()
router.register(r'', DisciplineViewSet, basename='DisciplineViewSet')

app_name = 'disciplines'
urlpatterns = []
urlpatterns += router.urls