# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'main-place', MainPlaceViewSet)
router.register(r'trip-planning', TripPlanningViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('MainPlaceViewSetsingleView/<int:id>/',MainPlaceViewSetsingleView.as_view(),name="MainPlaceViewSetsingleView")
]
