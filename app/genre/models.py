from django.db import models

from core.models import ModelBase


class Genre(ModelBase):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name
    