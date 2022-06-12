from django.db import models

from core.models import ModelBase


class ShowDate(ModelBase):
    class Meta:
        db_table = 'theater_show_date'

    value = models.DateField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.value)
