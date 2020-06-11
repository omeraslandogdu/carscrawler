from .views import CarsListView

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

v1_router = routers.DefaultRouter()

v1_router.register(r'cars', CarsListView, base_name='cars')

urlpatterns = [
    url(r'^v1/', include(v1_router.urls)),
]