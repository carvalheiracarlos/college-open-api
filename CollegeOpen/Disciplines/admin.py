from django.contrib import admin

from CollegeOpen.Disciplines.models import (
    Discipline,
    PreRequirements,
    CoRequirements,
    Equivalences
)


admin.site.register([
    Discipline,
    PreRequirements,
    CoRequirements,
    Equivalences
])