from django.contrib import admin
from src.cars.models import Cars

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'year', 'model', 'price', 'transmission')
    fields = ('brand', 'year', 'model', 'price', 'transmission')

    def get_queryset(self, request):
        qs = super(CarsAdmin, self).get_queryset(request)
        return qs
