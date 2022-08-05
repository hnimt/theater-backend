from django.contrib.auth import get_user_model
from django.db import models

from core import constants
from core.models import ModelBase


class Invoice(ModelBase):
    tax = models.DecimalField(default=constants.TAX, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    user = models.ForeignKey(get_user_model(), related_name="invoices", on_delete=models.CASCADE)
    is_pay = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"User: {self.user} | Total: {self.total}$"