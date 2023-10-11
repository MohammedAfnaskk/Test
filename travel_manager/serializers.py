# serializers.py
from rest_framework import serializers
from .models import MainPlace, TripPlanning
 
class TripPlanningSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TripPlanning
        fields = '__all__'

class MainPlaceSerializer(serializers.ModelSerializer):
    trip_planning = TripPlanningSerializer(many=True,required = False)
    class Meta:
        model = MainPlace
        fields = '__all__'
        
 
