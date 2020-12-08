from django.db import models

# Create your models here.
class DestinationModel(models.Model):
    destination = models.CharField(max_length=50)

    def __str__(self):
        return(self.destination)

class HireModel(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=50)
    pick_date = models.DateField()
    full_address = models.CharField(max_length=120)
    phone = models.CharField(max_length=14)
    country = models.CharField(max_length=50)
    TOUR_CHOICES = (
        ('shared', 'shared'),
        ('private', 'private'),
    )
    tour = models.CharField(choices=TOUR_CHOICES, max_length=20, null=False, default="private")

    def __str__(self):
        return(self.username)