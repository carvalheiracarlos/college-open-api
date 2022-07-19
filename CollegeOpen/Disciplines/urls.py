from django.urls import path
from rest_framework import routers

from CollegeOpen.Disciplines.views import CreateDisciplineView

router = routers.DefaultRouter()
router.register(r'', CreateDisciplineView, basename='CreateDiscipline')

app_name = 'disciplines'
urlpatterns = []
urlpatterns += router.urls