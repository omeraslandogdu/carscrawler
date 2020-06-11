from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.urls import (
    path,
    include,
)


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('src.cars.api.urls')),

]
