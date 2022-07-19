from django.urls import path
from rest_framework import routers

from CollegeOpen.Disciplines.views import DisciplineViewSet, DisciplineReviewsViewSet

router = routers.DefaultRouter()
router.register(r'', DisciplineViewSet, basename='DisciplineViewSet')
router.register(r'reviews', DisciplineReviewsViewSet, basename='DisciplineReviewsViewSet')

app_name = 'disciplines'
urlpatterns = []
urlpatterns += router.urls