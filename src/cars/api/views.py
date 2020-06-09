from rest_framework import viewsets

from src.commentrating.api.viewsets import CommentRatingModelViewSet
from .serializers import *


class EntityTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Entity type detail

    list:
    Entity type list.
    """

    queryset = EntityType.objects.filter(status=EntityType.STATUS_ACTIVE)
    serializer_class = EntityTypeSerializer


class CommentViewSet(CommentRatingModelViewSet):
    """
    döküman işte commentleri döner felan filan ingiliççe
    """
    serializer_class = CommentSerializer

    # TODO: user_id -->yerine user_email gönderecek, bu kontrol edilip[get_or_insert] user'a çevirilecek.
    # INFO: client_id --> request.user'dan gelir [ request.user = client ]

    def get_queryset(self):
        # TODO: buna generic bir çözüm bulunacak [æssgn: @cengizhan]
        return Comment.objects.filter(status=Comment.STATUS_ACTIVE).all()