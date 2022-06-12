from django.db import models


class ModelBase(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class ModelPerson(ModelBase):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(default=None)
