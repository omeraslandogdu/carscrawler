from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import *

v1_router = routers.DefaultRouter()

# TODO: viewset ve serializer'lerde ayırabiliriz, modeller gibi...
v1_router.register(r'entity_types', EntityTypeViewSet, base_name='entity_types')
v1_router.register(r'comments', CommentViewSet, base_name='comments')
# v1_router.register(r'ratings', RatingViewSet, base_name='ratings')
# v1_router.register(r'likes', LikeViewSet, base_name='likes')

urlpatterns = [
    url(r'^v1/', include(v1_router.urls)),
]
