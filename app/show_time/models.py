from django.db import models

from core.models import ModelBase


class ShowTime(ModelBase):
    class Meta:
        db_table = 'theater_show_time'

    value = models.TimeField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.value)
