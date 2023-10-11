from django.db import models
from account.models import CustomUser


class TripPlanning(models.Model):
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField( null=True, blank=True)
    
    # Define choices for the status field4
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'), 
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

class MainPlace(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    main_place = models.CharField(max_length=20, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True) 
    place_image = models.ImageField(null=True,blank=True)
    note = models.TextField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    trip_planning=models.ManyToManyField(TripPlanning)