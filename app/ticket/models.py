from django.db import models

from core.constants import SEAT_TYPES
from core.models import ModelBase


class Ticket(ModelBase):
    price = models.DecimalField(max_digits=4, decimal_places=2)
    type = models.CharField(max_length=10, choices=SEAT_TYPES)

    def __str__(self):
        return f"{self.type} | {self.price}$"
