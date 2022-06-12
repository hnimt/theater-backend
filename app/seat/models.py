from django.db import models

from core.constants import SEAT_TYPES
from core.models import ModelBase
from room.models import Room


class Seat(ModelBase):
    class Meta:
        unique_together = ['row', 'column', 'room']

    row = models.CharField(max_length=1, null=False, blank=False)
    column = models.CharField(max_length=2, null=False, blank=False)
    room = models.ForeignKey(Room, related_name="seats", null=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=SEAT_TYPES)

    def __str__(self):
        return self.row + self.column
