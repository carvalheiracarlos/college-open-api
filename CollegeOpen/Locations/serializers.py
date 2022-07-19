from rest_framework import serializers

from CollegeOpen.Locations.models import Location 

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address']