from django.contrib import admin

# Register your models here.

from CollegeOpen.Locations.models import Location


admin.site.register([Location])