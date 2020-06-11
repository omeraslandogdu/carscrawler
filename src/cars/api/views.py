from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
from src.cars.api.serializers import CarsSerializer
from src.cars.models import Cars
from rest_framework import viewsets

class CarsListView(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['brand', 'transmission', 'int_color', 'ext_color', 'drivetrain', 'year']
    serializer_class = CarsSerializer
    queryset = Cars.objects.filter(status=Cars.STATUS_ACTIVE)