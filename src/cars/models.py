from django.db import models
from src.core.models import BaseModel

class Cars(BaseModel):
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    model = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    ext_color = models.CharField(max_length=255)
    int_color = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    drivetrain = models.CharField(max_length=255)
    url = models.CharField(max_length=255)