# views.py
from rest_framework import viewsets
from .models import MainPlace, TripPlanning
from .serializers import MainPlaceSerializer, TripPlanningSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse

class MainPlaceViewSet(viewsets.ModelViewSet):
    queryset = MainPlace.objects.all()
    serializer_class = MainPlaceSerializer
    

class TripPlanningViewSet(viewsets.ModelViewSet):
    queryset = TripPlanning.objects.all()
    serializer_class = TripPlanningSerializer
    
    def create(self, request, *args, **kwargs):
        
        main_place_id = request.data.get('maintable_id')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        if serializer:
            try:
                main_place = MainPlace.objects.get(pk=main_place_id)
                main_place.trip_planning.add(serializer.instance)
            except MainPlace.DoesNotExist:
                pass
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class MainPlaceViewSetsingleView(generics.RetrieveAPIView):
    serializer_class = MainPlaceSerializer
    queryset = MainPlace.objects.all()
    lookup_field = 'id'




