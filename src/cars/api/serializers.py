from rest_framework import serializers

from src.cars.models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields = ['brand', 'model', 'year', 'price', 'mileage',
                  'ext_color', 'int_color', 'transmission', 'drivetrain', 'url']

