from django.contrib.auth.models import User
from django.db import models

__all__ = [
    'BaseModel',
    'BaseTimestampModel',
]


class BaseTimestampModel(models.Model):
    """
    Base timestamp model
    """
    id = models.AutoField(name='id', primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class BaseModel(BaseTimestampModel):
    """
    Use this model for common functionality
    """

    STATUS_ACTIVE = 1
    STATUS_PASSIVE = 0
    STATUS_DELETED = -1

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_PASSIVE, 'Passive'),
        (STATUS_DELETED, 'Deleted'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_ACTIVE, )

    objects = models.Manager()

    class Meta:
        abstract = True
