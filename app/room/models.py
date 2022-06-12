from django.db import models

from core.models import ModelBase


class Room(ModelBase):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
