import django_filters
from CollegeOpen.Disciplines.models import Discipline

class DisciplineFilter(django_filters.FilterSet):
    DisciplineCode = django_filters.CharFilter(field_name='code', lookup_expr='icontains')
    DisciplineName = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Discipline 
        fields = ['DisciplineCode', 'DisciplineName']