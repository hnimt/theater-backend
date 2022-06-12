from django.db import models

from core.models import ModelPerson


class Actor(ModelPerson):
    avatar = models.ImageField(upload_to='uploads/actors/%Y/%m', default=None)

    def __str__(self):
        return self.name
