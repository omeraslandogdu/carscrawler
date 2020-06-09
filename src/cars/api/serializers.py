from rest_framework import serializers

from src.commentrating.models import EntityType
from src.commentrating.models import Comment


class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = (
            'id',
            'title',
            'key',
            'available_on_ratings',
            'available_on_comments',
            'available_on_likes',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'body',
            'parent',
            'entity_type',
            'user',
            'user_type',
            'entity_id',
        )
