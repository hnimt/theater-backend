from django.db import models

from core.models import ModelPerson


class Director(ModelPerson):
    avatar = models.ImageField(upload_to='uploads/directors/%Y/%m', default=None)

    def __str__(self):
        return self.name
