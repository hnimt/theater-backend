from django.db import models

from actor.models import Actor
from core.models import ModelBase
from director.models import Director
from genre.models import Genre


class Movie(ModelBase):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False, blank=False)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='uploads/movies/%Y/%m')
    actors = models.ManyToManyField(Actor, related_name="movies")
    directors = models.ManyToManyField(Director, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies", blank=False)
    trailer = models.TextField(null=False, blank=False, default='https://www.youtube.com/embed/SNkwT1DfmVU')

    def __str__(self):
        return self.title
